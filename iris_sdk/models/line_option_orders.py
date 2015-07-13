#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.data.line_option_order import LineOptionOrderData

XML_NAME_LINE_OPTION_ORDERS = "LineOptionOrder"
XPATH_LINE_OPTION_ORDERS = "/lineOptionOrders"

class LineOptionOrder(BaseResource, LineOptionOrderData):

    """ Establish Calling Name Display settings for a collection of TNs at a time """

    _node_name = XML_NAME_LINE_OPTION_ORDERS
    _xpath = XPATH_LINE_OPTION_ORDERS

    def __init__(self, parent=None, client=None):
        super().__init__(parent, client)
        LineOptionOrderData.__init__(self)

    def list(self):
        return self._get_data().tn_line_options