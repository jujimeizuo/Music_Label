# Copyright 2014 Baidu, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
"""
Configuration for bmr samples.
"""

#!/usr/bin/env python
#coding=utf-8

import logging
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

HOST = 'http://bmr.fsh.baidubce.com'
AK = 'e7612edde15f401bbcaac404f0cddc76'
SK = 'd17ed86b93184054bb912036910fd71f'

logger = logging.getLogger('baidubce.services.bmr.bmrclient')
fh = logging.FileHandler('bmr_sample.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

check_cluster_max_retry_time=20
check_cluster_interval_sec=60
