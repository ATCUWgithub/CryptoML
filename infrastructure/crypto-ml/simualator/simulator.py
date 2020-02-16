#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT


#TODO: add imports

class Simulator:
    def __init__(self, wallet, agent, config):
        if not isinstance(wallet, Wallet):
            raise TypeError("Variable `wallet` need to be of type `Wallet`")
        if not isinstance(agent, Agent):
            raise TypeError("Variable `agent` need to be of type `Agent`")
        
        self.agent = agent
        self.wallet = wallet
        
        self.start = config["test_start"]
        self.end = config["test_end"]
        
        self.current = self.start
        
        self.orders = []
        self._roi = []
        
    def __place_orders(self):
        pass
    
    def __cancel_orders(self):
        pass
    
    def step(self):
        pass

    def run(self):
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
        date_list = [self.start - datetime.datetime.timedelta(minutes=x) for x in range(num_mins)]
        for r, d in zip(self._roi, date_list):
            roi_dict.append({
                "roi": self._roi[len(self._roi) - 1],
                "timestamp": d
            })

        return _roi