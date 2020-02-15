#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

import datetime
from .DataTemplate import DataTemplate
from .DataEnums import OrderType

# TODO: docstring on this class
class DataRaw(DataTemplate):
    def __init__(self, order_type, data):
        if not isinstance(order_type, OrderType):
            raise TypeError("Variable `order_type` need to be of type `OrderType`")
        self.order_type = order_type
        
        self.data = data
        self.data.sort(key=lambda x:x["timestamp"])

    def get(self, timestamp):
        if timestamp < self.data[0]["timestamp"]:
            raise ValueError("`timestamp` requested is lower than the lowest timestamp in the data")

        current_idx = 0
        for idx, d in enumerate(self.data):
        	# TODO: figure out if there are cases where we're predicting the future
            if d["timestamp"] > timestamp:
                current_idx = idx
                break
        return self.data[current_idx - 1]