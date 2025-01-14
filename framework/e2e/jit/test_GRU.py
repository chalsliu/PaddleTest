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


def test_GRU_base():
    """test GRU_base"""
    jit_case = JitTrans(case=yml.get_case_info("GRU_base"))
    jit_case.jit_run()


def test_GRU_0():
    """test GRU_0"""
    jit_case = JitTrans(case=yml.get_case_info("GRU_0"))
    jit_case.jit_run()


def test_GRU_1():
    """test GRU_1"""
    jit_case = JitTrans(case=yml.get_case_info("GRU_1"))
    jit_case.jit_run()


def test_GRU_2():
    """test GRU_2"""
    jit_case = JitTrans(case=yml.get_case_info("GRU_2"))
    jit_case.jit_run()


def test_GRU_3():
    """test GRU_3"""
    jit_case = JitTrans(case=yml.get_case_info("GRU_3"))
    jit_case.jit_run()


def test_GRU_5():
    """test GRU_5"""
    jit_case = JitTrans(case=yml.get_case_info("GRU_5"))
    jit_case.jit_run()


def test_GRU_6():
    """test GRU_6"""
    jit_case = JitTrans(case=yml.get_case_info("GRU_6"))
    jit_case.jit_run()
