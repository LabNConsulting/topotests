#!/usr/bin/env python

# Copyright (c) 2017, LabN Consulting, L.L.C.
# Authored by Lou Berger <lberger@labn.net>
#
# Permission to use, copy, modify, and/or distribute this software
# for any purpose with or without fee is hereby granted, provided
# that the above copyright notice and this permission notice appear
# in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND NETDEF DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL NETDEF BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY
# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.

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
    auAddTest('scripts/vrfs.py', False, CliOnFail, CheckFunc)
    auAddTest('scripts/adjacencies.py', True, CliOnFail, CheckFunc)
    CheckFunc = 'versionCheck(\'3.1\', cli=True)'
    auAddTest('scripts/add_routes.py', True, CliOnFail, CheckFunc)
    CheckFunc = 'versionCheck(\'3.1\')'
    auAddTest('scripts/check_routes.py', True, CliOnFail, CheckFunc)
    #uncomment next line to start cli *before* script is run
    #CheckFunc = 'versionCheck(\'3.1\', cli=True)'
    auAddTest('scripts/cleanup_all.py', True, CliOnFail, CheckFunc)
    auClose()
    sys.exit(auRun())

