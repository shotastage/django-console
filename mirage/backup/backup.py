# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import shutil
import sys
import time
import distutils

from mirage import system as mys
from mirage import proj

from mirage              import project
from mirage              import fileable
from mirage.flow         import Workflow

from mirage.workspace import storage

class DjangoBackupAppWorkFlow(Workflow):

    def constructor(self):
        self._app_name = self._values[0]


    def main(self):

        mys.log("Backing up application \"{0}\"...".format(self._app_name))
        storage.MirageWorkspace.initialize()
        storage.MirageWorkspace.persist(self._app_name, "mi_backup")
