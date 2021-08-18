# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.32
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class MetadataApi(object):
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
        """Add metadata field  # noqa: E501

        Add a new custom metadata field to be indexed for the account.  # noqa: E501
        """
        (data) = self.add_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add metadata field  # noqa: E501

        Add a new custom metadata field to be indexed for the account.  # noqa: E501
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
            '/metadata/add', 'POST',
            body=body_params,
            response_type='InlineResponse20034') # noqa: E501

    def delete(self, body = {}, **kwargs):  # noqa: E501
        """Delete metadata field  # noqa: E501

        Delete an existing custom metadata field. Deletion isn't instataneous, and /metadata/list will continue to return the field until the asynchronous deletion process is complete.  # noqa: E501
        """
        (data) = self.delete_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete metadata field  # noqa: E501

        Delete an existing custom metadata field. Deletion isn't instataneous, and /metadata/list will continue to return the field until the asynchronous deletion process is complete.  # noqa: E501
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
            '/metadata/delete', 'POST',
            body=body_params,
            response_type='InlineResponse20036') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List metadata fields  # noqa: E501

        Get the list of custom metadata fields indexed for the account.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List metadata fields  # noqa: E501

        Get the list of custom metadata fields indexed for the account.  # noqa: E501
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
            '/metadata/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20033]') # noqa: E501

    def update(self, body = {}, **kwargs):  # noqa: E501
        """Update metadata field  # noqa: E501

        Update an existing custom metadata field.  # noqa: E501
        """
        (data) = self.update_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def update_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update metadata field  # noqa: E501

        Update an existing custom metadata field.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/metadata/update', 'POST',
            body=body_params,
            response_type='InlineResponse20035') # noqa: E501
