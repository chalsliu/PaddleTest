#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
test jit cases
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "utils"))

from utils.yaml_loader import YamlLoader
from jittrans import JitTrans

yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "yaml", "nn.yml")
yml = YamlLoader(yaml_path)


def test_Silu_base():
    """test Silu_base"""
    jit_case = JitTrans(case=yml.get_case_info("Silu_base"))
    jit_case.jit_run()


def test_Silu():
    """test Silu"""
    jit_case = JitTrans(case=yml.get_case_info("Silu"))
    jit_case.jit_run()


def test_Silu0():
    """test Silu0"""
    jit_case = JitTrans(case=yml.get_case_info("Silu0"))
    jit_case.jit_run()
