#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from builtins import object
def expr_min(data):
    result = (data[0], 0)
    for i, v in enumerate(data):
        if v < result[0]:
            result = (v, i)
    return result


def expr_max(data):
    result = (data[0], 0)
    for i, v in enumerate(data):
        if v > result[0]:
            result = (v, i)
    return result


def expr_avg(data):
    return (sum(data) / float(len(data)), None)


def expr_sum(data):
    return (sum(data), None)


class Expr(object):

    @classmethod
    def evaluate(self, expr, vars):
        return eval(compile(expr, "<string>", "eval"), vars)
