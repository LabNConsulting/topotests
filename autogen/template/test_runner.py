#!/usr/bin/env python

#
# Part of NetDEF Topology Tests
#
# Copyright (c) 2017 by
# Network Device Education Foundation, Inc. ("NetDEF")
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
#

"""
<template>.py: Test <template>.
"""

import os
import sys
import pytest

# this dir, holds auto generated content
AUTOCWD = os.path.dirname(os.path.realpath(__file__))
# the top dir
ROOT = os.path.dirname(os.path.realpath(os.path.join(AUTOCWD, '..')))
# test name based on directory
TEST = os.path.basename(AUTOCWD)
# CWD - source of test, holds configuration files and customized topology
CWD = os.path.join(ROOT, TEST)

sys.path.append(ROOT)
sys.path.append(CWD)
sys.path.append(AUTOCWD)

# pylint: disable=C0413
# Import topogen and topotest helpers
from lib import topotest
from lib.topogen import Topogen, TopoRouter, get_topogen
from lib.topolog import logger

# Required to instantiate the topology builder class.
from mininet.topo import Topo
from customize import *
from autogen_tests import *

def setup_module(mod):
    "Sets up the pytest environment"
    # This function initiates the topology build with Topogen...
    tgen = Topogen(ThisTestTopo, mod.__name__)
    # ... and here it calls Mininet initialization functions.
    tgen.start_topology()

    logger.info('Topology started')
    # This is a sample of configuration loading.
    router_list = tgen.routers()

    # For all registred routers, load the zebra configuration file
    for rname, router in router_list.iteritems():
        print("Setting up %s" % rname)
        config = os.path.join(CWD, '{}/zebra.conf'.format(rname))
        if os.path.exists(config):
            router.load_config(TopoRouter.RD_ZEBRA, config)
        config = os.path.join(CWD, '{}/ospfd.conf'.format(rname))
        if os.path.exists(config):
            router.load_config(TopoRouter.RD_OSPF, config)
        config = os.path.join(CWD, '{}/ldpd.conf'.format(rname))
        if os.path.exists(config):
            router.load_config(TopoRouter.RD_LDP, config)
        config = os.path.join(CWD, '{}/bgpd.conf'.format(rname))
        if os.path.exists(config):
            router.load_config(TopoRouter.RD_BGP, config)

    # After loading the configurations, this function loads configured daemons.
    logger.info('Starting routers')
    tgen.start_router()

    # For debugging after starting daemons, uncomment the next line
    #tgen.mininet_cli()

def teardown_module(mod):
    "Teardown the pytest environment"
    tgen = get_topogen()

    # This function tears down the whole topology.
    tgen.stop_topology()

# Memory leak test template
def test_memory_leak():
    "Run the memory leak test and report results."
    tgen = get_topogen()
    if not tgen.is_memleak_enabled():
        pytest.skip('Memory leak test/report is disabled')

    tgen.report_memory_leaks()

if __name__ == '__main__':
    args = ["-s"] + sys.argv[1:]
    sys.exit(pytest.main(args))
