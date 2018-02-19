__author__ = "Daniele Capocefalo, Mauro Truglio, Tommaso Mazza"
__copyright__ = "Copyright 2018, The pyntacle Project"
__credits__ = ["Ferenc Jordan"]
__version__ = "0.0.1"
__maintainer__ = "Daniele Capocefalo"
__email__ = "d.capocefalo@css-mendel.it"
__status__ = "Development"
__date__ = "27 February 2018"
__license__ = u"""
  Copyright (C) 2016-2018  Tommaso Mazza <t.mazza@css-mendel.it>
  Viale Regina Margherita 261, 00198 Rome, Italy

  This program is free software; you can use and redistribute it under
  the terms of the BY-NC-ND license as published by
  Creative Commons; either version 4 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  License for more details.

  You should have received a copy of the license along with this
  work. If not, see http://creativecommons.org/licenses/by-nc-nd/4.0/.
  """

import logging
import datetime
import importlib
import seaborn as sns
import threading
import time
import sys
import os

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
format_dictionary = {"adjmat": "adjm", "edgelist": "egl", "sif": "sif", "dot": "dot", "bin": "graph", "adjm": "adjm",
                     "graph": "graph", "edgl": "egl", "egl": "egl", "binary": "bin", "adjacencymatrix": "adjm",
                     "edge_list": "egl", "adjacency_matrix": "adjm"}
runtime_date = datetime.datetime.now().strftime("%d%m%Y%H%M")


class CursorAnimation(threading.Thread):
    """
    Just a waiting animation, common to several commands.
    """
    def __init__(self):
        self.flag = True

        if os.name == "nt":
            self.animation_char = u'|/-\\'
        else:
            self.animation_char = u'⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
        self.idx = 0
        threading.Thread.__init__(self)

    def run(self):
        while self.flag:
            sys.stdout.write("Processing...", )
            sys.stdout.write(self.animation_char[self.idx % len(self.animation_char)] + "\r", )
            self.idx += 1
            time.sleep(0.1)

    def stop(self):
        self.flag = False
