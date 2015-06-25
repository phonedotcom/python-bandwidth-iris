#!/usr/bin/env python

import requests
from xml.etree import ElementTree

ERROR_TEMPLATE = "{} Iris error: {}"
HEADERS = {"content-type": "application/xml"}
HTTP_OK = 200

class RestError(Exception):
    pass

class RestClient():

    """
    HTTP requests wrapper.
    """

    def request(self, method, url, auth, params=None, data=None):

        assert method in ("GET", "POST", "DELETE", "PUT")

        try:
            response = requests.request(method, url, auth=auth,
                headers=HEADERS, data=data, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_exception:
            # Logical errors in response body.
            if (response.content != b"" ):
                root = ElementTree.fromstring(response.content)
                error_msg = ERROR_TEMPLATE.format(
                    root[0][0].text, root[0][1].text)
                # Suppress the HTTP exception.
                raise RestError(error_msg) from None
            else:
                raise http_exception