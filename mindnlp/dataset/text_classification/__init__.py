# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
TextClassification dataset init
"""

from .agnews import AG_NEWS, AG_NEWS_Process
from .cola import CoLA
from .sst2 import SST2
from .amazonreviewfull import AmazonReviewFull, AmazonReviewFull_Process
from .amazonreviewpolarity import AmazonReviewPolarity, AmazonReviewPolarity_Process
from .stsb import STSB
from .dbpedia import DBpedia
from .imdb import IMDB
from .mnli import MNLI
from .mrpc import MRPC
from .qnli import QNLI
from .qqp import QQP
from .wnli import WNLI
from .rte import RTE
from .sogounews import SogouNews
from .yelpreviewpolarity import YelpReviewPolarity
from .yelpreviewfull import YelpReviewFull
from .yahooanswers import YahooAnswers