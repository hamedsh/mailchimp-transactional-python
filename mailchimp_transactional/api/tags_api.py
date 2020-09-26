# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.19
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class TagsApi(object):
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

    def all_time_series(self, body = {}, **kwargs):  # noqa: E501
        """View all tags history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for all tags.  # noqa: E501
        """
        (data) = self.all_time_series_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def all_time_series_with_http_info(self, body, **kwargs):  # noqa: E501
        """View all tags history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for all tags.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_time_series" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/tags/all-time-series', 'POST',
            body=body_params,
            response_type='list[InlineResponse20028]') # noqa: E501

    def delete(self, body = {}, **kwargs):  # noqa: E501
        """Delete tag  # noqa: E501

        Deletes a tag permanently. Deleting a tag removes the tag from any messages that have been sent, and also deletes the tag's stats. There is no way to undo this operation, so use it carefully.  # noqa: E501
        """
        (data) = self.delete_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete tag  # noqa: E501

        Deletes a tag permanently. Deleting a tag removes the tag from any messages that have been sent, and also deletes the tag's stats. There is no way to undo this operation, so use it carefully.  # noqa: E501
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
            '/tags/delete', 'POST',
            body=body_params,
            response_type='InlineResponse20055') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get tag info  # noqa: E501

        Return more detailed information about a single tag, including aggregates of recent stats.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get tag info  # noqa: E501

        Return more detailed information about a single tag, including aggregates of recent stats.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method info" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/tags/info', 'POST',
            body=body_params,
            response_type='InlineResponse20056') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List tags  # noqa: E501

        Return all of the user-defined tag information.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List tags  # noqa: E501

        Return all of the user-defined tag information.  # noqa: E501
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
            '/tags/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20054]') # noqa: E501

    def time_series(self, body = {}, **kwargs):  # noqa: E501
        """View tag history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a tag.  # noqa: E501
        """
        (data) = self.time_series_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def time_series_with_http_info(self, body, **kwargs):  # noqa: E501
        """View tag history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a tag.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method time_series" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/tags/time-series', 'POST',
            body=body_params,
            response_type='list[InlineResponse20028]') # noqa: E501
