#!/usr/bin/env python
#
# Copyright 2013 Carter Bain Wealth Management
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from datetime import datetime

import pytz

from alephnull.algorithm import TradingAlgorithm
from alephnull.utils.factory import load_from_yahoo


syms = ['GS', 'AAPL', 'XOM', 'GOOG']
start = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc)
end = datetime(2014, 2, 24, 0, 0, 0, 0, pytz.utc)
data = load_from_yahoo(stocks=syms, indexes={}, start=start,
                       end=end)


class BuyStock(TradingAlgorithm):
    def initialize(self):
        self.allocated = False
        self.orders = []

    def handle_data(self, data):
        print self.portfolio
        if not self.allocated:
            for sym in data:
                ref = self.order(sym, 50)
                self.orders.append(ref)
            self.allocated = True


simple_algo = BuyStock(live_execution=True)
print simple_algo.portfolio
results = simple_algo.run(data)
simple_algo.live_execution.disconnect()

