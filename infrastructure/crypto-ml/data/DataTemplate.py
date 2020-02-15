#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod

# TODO: docstring on this class
class DataTemplate(ABC):
    @abstractmethod
    def get(self, timestamp):
        pass
