#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

from .AgentTemplate import AgentTemplate

class SimpleAgent(AgentTemplate):
	def handle_orders(self, place_order, cancel_order, current_orders, wallet):
		# Do nothing for SimpleAgent
		pass