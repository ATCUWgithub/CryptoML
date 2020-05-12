#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

import pytest
import datetime as _datetime

from data import DataEnums
from data import DataRaw
from data import OrderType


# TODO: Document test
def test_pass_data_raw():
	dict_ts = _datetime.time(12, 30, 12)
	data_obj = DataRaw(OrderType.CONTINOUS, [{"timestamp": dict_ts}])
	current_ts = _datetime.time(12, 30, 45)
	element = data_obj.get(current_ts)
	assert len(element) == 1

def test_fail_data_raw():
	dict_ts = _datetime.time(12, 30, 45)
	data_obj = DataRaw(OrderType.CONTINOUS, [{"timestamp": dict_ts}])
	current_ts = _datetime.time(12, 30, 12)
	with pytest.raises(ValueError):
		element = data_obj.get(current_ts)