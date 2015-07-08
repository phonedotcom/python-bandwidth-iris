#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.data.address import Address
from iris_sdk.models.data.listing_name import ListingName
from iris_sdk.models.maps.dlda import DldaMap

class Dlda(DldaMap, BaseData):

    def __init__(self):
        self.address = Address()
        self.listing_name = ListingName()