#!/usr/bin/env python

# Copyright 2017, LabN Consulting, L.L.C.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; see the file COPYING; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

import os
import sys
import shutil
CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(CWD, '../'))
# test name based on directory
TEST = os.path.basename(CWD)

from lib.autogen import *

if __name__ == '__main__':
    CliOnFail = None
    # For debugging, uncomment the next line
    #CliOnFail = 'tgen.mininet_cli'

    CheckFunc = 'versionCheck(\'3.1\')'

    logDir = '/tmp/topotests/{}.test_runner'.format(TEST)
    auInit(baseScriptDir="'"+CWD+"'", baseLogDir="'"+logDir+"'", net='tgen.net')
    auAddTest('scripts/adjacencies.py', False, CliOnFail, CheckFunc)
    auAddTest('scripts/add_routes.py', True, CliOnFail, CheckFunc)
    auAddTest('scripts/check_routes.py', True, CliOnFail, CheckFunc)
    #uncomment next line to start cli *before* script is run
    #CheckFunc = 'versionCheck(\'3.1\', cli=True)'
    auAddTest('scripts/cleanup_all.py', True, CliOnFail, CheckFunc)
    auClose()
    sys.exit(auRun())

