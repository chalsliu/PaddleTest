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


def test_TransformerEncoderLayer_base():
    """test TransformerEncoderLayer_base"""
    jit_case = JitTrans(case=yml.get_case_info("TransformerEncoderLayer_base"))
    jit_case.jit_run()


def test_TransformerEncoderLayer_0():
    """test TransformerEncoderLayer_0"""
    jit_case = JitTrans(case=yml.get_case_info("TransformerEncoderLayer_0"))
    jit_case.jit_run()


def test_TransformerEncoderLayer_1():
    """test TransformerEncoderLayer_1"""
    jit_case = JitTrans(case=yml.get_case_info("TransformerEncoderLayer_1"))
    jit_case.jit_run()


def test_TransformerEncoderLayer_2():
    """test TransformerEncoderLayer_2"""
    jit_case = JitTrans(case=yml.get_case_info("TransformerEncoderLayer_2"))
    jit_case.jit_run()


def test_TransformerEncoderLayer_3():
    """test TransformerEncoderLayer_3"""
    jit_case = JitTrans(case=yml.get_case_info("TransformerEncoderLayer_3"))
    jit_case.jit_run()


def test_TransformerEncoderLayer_4():
    """test TransformerEncoderLayer_4"""
    jit_case = JitTrans(case=yml.get_case_info("TransformerEncoderLayer_4"))
    jit_case.jit_run()
