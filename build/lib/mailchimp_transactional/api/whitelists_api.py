# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.41
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class WhitelistsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_key='', api_client = None):
        self.api_key = api_key
        if api_client:
            self.api_client = api_client
        else:
            self.api_client = ApiClient()

    def add(self, body = {}, **kwargs):  # noqa: E501
        """Add email to allowlist  # noqa: E501

        Adds an email to your email rejection allowlist. If the address is currently on your denylist, that denylist entry will be removed automatically.  # noqa: E501
        """
        (data) = self.add_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add email to allowlist  # noqa: E501

        Adds an email to your email rejection allowlist. If the address is currently on your denylist, that denylist entry will be removed automatically.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/whitelists/add', 'POST',
            body=body_params,
            response_type='InlineResponse200') # noqa: E501

    def delete(self, body = {}, **kwargs):  # noqa: E501
        """Remove email from allowlist  # noqa: E501

        Removes an email address from the allowlist.  # noqa: E501
        """
        (data) = self.delete_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Remove email from allowlist  # noqa: E501

        Removes an email address from the allowlist.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/whitelists/delete', 'POST',
            body=body_params,
            response_type='InlineResponse2002') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List allowlisted emails  # noqa: E501

        Retrieves your email rejection allowlist. You can provide an email address or search prefix to limit the results. Returns up to 1000 results.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List allowlisted emails  # noqa: E501

        Retrieves your email rejection allowlist. You can provide an email address or search prefix to limit the results. Returns up to 1000 results.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/whitelists/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse2001]') # noqa: E501
