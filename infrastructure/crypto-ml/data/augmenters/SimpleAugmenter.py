#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

from .. import DataRaw
from .. import DataTemplate

class SimpleAugmenter(DataTemplate):
    def __init__(self, raw_data):
        for d in raw_data:
            if not isinstance(d, DataRaw):
                raise TypeError("Element in array `raw_data` need to be of type `DataRaw`")
        self.raw_data = raw_data
    
    def get(self, timestamp):
        datum = [rd.get(timestamp) for rd in self.raw_data]
        # TODO: augment datum here
        return datum