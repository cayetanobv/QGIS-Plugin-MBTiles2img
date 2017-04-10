# -*- coding: utf-8 -*-
#
#  A little python library to take an mbtiles file and split it apart
#  into a folder hierarchy of individual image tile files (or pbf files
#  for vector tiles).
#
#  This project is a improved class library version of the command
#  line utility developed by Patrick Barry:
#  https://github.com/pbarry/MBTiles-extractor
#
#  Author: Cayetano Benavent, 2014-2016.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


import os
import sys
import sqlite3
import shutil
import gzip


class MBTilesExtractorException(Exception):
    pass

class MBTilesExtractor(object):
    """
    A little python library to take an mbtiles file and split it apart
    into a folder hierarchy of individual image tile files (or pbf files
    for vector tiles).

    This project is a improved class library version of the command
    line utility developed by Patrick Barry:
    https://github.com/pbarry/MBTiles-extractor

    >>> from mbtilesextractor import MBTilesExtractor
    >>> input_file = '/source_folder/my_file.mbtiles'

    # optional: if not dirname, same folder as input_file
    >>> dest_folder = '/dest_folder'

    >>> ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=False)
    >>> ex_mbt.extractTiles()

    # get total nmber of tiles
    >>> nt = ex_mbt.ntiles
    """

    def __init__(self, input_filename, dirname=None, overwrite=True, decompr=False):
        self.input_filename = input_filename
        self.__ntiles = 0
        self.__decompr = decompr

        if dirname:
            if not os.path.exists(dirname):
                self.dirname = None
                return
            filename = os.path.basename(self.input_filename[0:self.input_filename.index('.')])
            self.dirname =  os.path.join(dirname,filename)

        else:
            self.dirname = self.input_filename[0:self.input_filename.index('.')]

        self.overwrite = overwrite

    @property
    def ntiles(self):
        return self.__ntiles

    def extractTiles(self):
        if not os.path.exists(self.input_filename):
            raise MBTilesExtractorException('MBTiles file does not exist')

        if not self.dirname:
            raise MBTilesExtractorException('Destination folder does not exist')

        if os.path.exists(self.dirname):
            if self.overwrite == False:
                raise MBTilesExtractorException('Data directory exists')

            elif self.overwrite == True:
                shutil.rmtree(self.dirname)
                os.makedirs(self.dirname)
        else:
            os.makedirs(self.dirname)

        try:
            connection = sqlite3.connect(self.input_filename)
            cursor = connection.cursor()

            cursor.execute("SELECT value FROM metadata WHERE name='format'")
            img_format = cursor.fetchone()

            if img_format:
                out_format = '.{}'.format(img_format[0])
            else:
                out_format = ''

            cursor.execute("SELECT * FROM tiles")

            os.chdir(self.dirname)
            for row in cursor:
                self.__setDir(str(row[0]))
                self.__setDir(str(row[1]))

                with open(str(row[2]) + out_format, 'wb') as output_file:
                    output_file.write(row[3])

                if out_format == '.pbf' or self.__decompr:
                    with gzip.open(os.path.join(str(row[2]) + out_format), 'rb') as f:
                        f_dec = f.read()
                        with open(str(row[2]) + out_format, 'wb') as output_file2:
                            output_file2.write(f_dec)

                os.chdir('..')
                os.chdir('..')

            # does not work rowcount for select statements so...
            cursor.execute("SELECT count(*) FROM tiles")
            self.__ntiles = cursor.fetchone()[0]

            connection.close()

        except Exception as e:
            if os.path.exists(self.dirname):
                shutil.rmtree(self.dirname)
            raise

    def __safeMakeDir(self, dir_path):
        if os.path.exists(dir_path):
            return
        os.makedirs(dir_path)

    def __setDir(self, dir_path):
        self.__safeMakeDir(dir_path)
        os.chdir(dir_path)
