#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

import datetime as _datetime

from ..wallet import Wallet
from ..agent import AgentTemplate

# TODO: config determine frequency, hardcoded to 1 minute
class Simulator:
    def __init__(self, wallet, agent, config):
        if not isinstance(wallet, Wallet):
            raise TypeError("Variable `wallet` need to be of type `Wallet`")
        if not isinstance(agent, AgentTemplate):
            raise TypeError("Variable `agent` need to be of type `AgentTemplate`")
        
        self.agent = agent
        self.wallet = wallet

        self.base_value = wallet.crypto_amount
        
        # TODO: config live vs simulated
        self.start = config["test_start"]
        self.end = config["test_end"]
        
        self.current = self.start
        
        self.orders = []
        self._roi = []

        self.live = False
        
    def __place_orders(self):
        # TODO: Write logic
        pass
    
    def __cancel_orders(self):
        # TODO: Write logic
        pass

    def __step_orders(self):
        # TODO: handle open and pending orders here
        pass

    def __roi_order(self):
        # TODO: compute order_roi
        return 0

    def __current_earnings(self):
        wallet_money = self.wallet.crypto_amount
        order_money = self.__roi_order()
        return wallet_money + order_money

    # TODO: allow config to change frequency
    def step(self):
        if self.current >= self.end and not self.live:
            return False

        # Take care of Orders
        self.__step_orders()

        # Call agent to place Orders
        self.agent.synchronize(self.current)
        self.agent.handle_orders(self.__place_orders, self.__cancel_orders, self.orders, self.wallet)
        
        # Update Current Value
        self.current = self.current + _datetime.timedelta(minutes=1)
        
        # Calculate ROI
        earnings = self.__current_earnings()
        roi = (earnings - self.base_value) / self.base_value
        self._roi.append(roi)

        return True

    def run(self):
        while self.step():
            pass
    
    def roi(self):
        if(len(self._roi) == 0):
            return {}
        return {
            "roi": self._roi[len(self._roi) - 1],
            "timestamp": self.current
        }
    
    # always sell puts
    def roi_curve(self):
        roi_dict = []
        delta = (self.current - self.start)
        num_mins = delta.seconds / 60
        date_list = [self.start - _datetime.datetime.timedelta(minutes=x) for x in range(num_mins)]
        for r, d in zip(self._roi, date_list):
            roi_dict.append({
                "roi": self._roi[len(self._roi) - 1],
                "timestamp": d
            })

        return _roi