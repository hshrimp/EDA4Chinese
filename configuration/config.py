#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/10/30 上午10:59
"""
import os
import logging

"""global configuration"""
# 项目路径
PROJECT_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(PROJECT_PATH, 'stopwords/')
STOPWORDS = os.path.join(DATA_DIR, 'hit_stopwords.txt')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

