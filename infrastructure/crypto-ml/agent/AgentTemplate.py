#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod
from data import DataTemplate

class AgentTemplate(ABC):
    def __init__(self, data_array):
        for d in data_array:
            if not isinstance(d, DataTemplate):
                raise TypeError("Element in array `data_array` need to be of type `DataTemplate`")
        self.data_array = data_array
    
    @abstractmethod
    def handle_orders(self, place_order, cancel_order, current_orders, wallet):
        pass