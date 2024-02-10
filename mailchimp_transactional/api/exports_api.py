# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.59
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class ExportsApi(object):
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

    def activity(self, body = {}, **kwargs):  # noqa: E501
        """Export activity history  # noqa: E501

        Begins an export of your activity history. The activity will be exported to a zip archive containing a single file named activity.csv in the same format as you would be able to export from your account's activity view. It includes the following fields: Date, Email Address, Sender, Subject, Status, Tags, Opens, Clicks, Bounce Detail. If you have configured any custom metadata fields, they will be included in the exported data.  # noqa: E501
        """
        (data) = self.activity_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def activity_with_http_info(self, body, **kwargs):  # noqa: E501
        """Export activity history  # noqa: E501

        Begins an export of your activity history. The activity will be exported to a zip archive containing a single file named activity.csv in the same format as you would be able to export from your account's activity view. It includes the following fields: Date, Email Address, Sender, Subject, Status, Tags, Opens, Clicks, Bounce Detail. If you have configured any custom metadata fields, they will be included in the exported data.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activity" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/exports/activity', 'POST',
            body=body_params,
            response_type='InlineResponse2007') # noqa: E501

    def allowlist(self, body = {}, **kwargs):  # noqa: E501
        """Export Allowlist  # noqa: E501

        Begins an export of your rejection allowlist. The allowlist will be exported to a zip archive containing a single file named allowlist.csv that includes the following fields: email, detail, created_at.  # noqa: E501
        """
        (data) = self.allowlist_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def allowlist_with_http_info(self, body, **kwargs):  # noqa: E501
        """Export Allowlist  # noqa: E501

        Begins an export of your rejection allowlist. The allowlist will be exported to a zip archive containing a single file named allowlist.csv that includes the following fields: email, detail, created_at.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method allowlist" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/exports/allowlist', 'POST',
            body=body_params,
            response_type='InlineResponse2006') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """View export info  # noqa: E501

        Returns information about an export job. If the export job's state is 'complete', the returned data will include a URL you can use to fetch the results. Every export job produces a zip archive, but the format of the archive is distinct for each job type. The api calls that initiate exports include more details about the output format for that job type.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """View export info  # noqa: E501

        Returns information about an export job. If the export job's state is 'complete', the returned data will include a URL you can use to fetch the results. Every export job produces a zip archive, but the format of the archive is distinct for each job type. The api calls that initiate exports include more details about the output format for that job type.  # noqa: E501
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
            '/exports/info', 'POST',
            body=body_params,
            response_type='InlineResponse2003') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List exports  # noqa: E501

        Returns a list of your exports.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List exports  # noqa: E501

        Returns a list of your exports.  # noqa: E501
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
            '/exports/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse2004]') # noqa: E501

    def rejects(self, body = {}, **kwargs):  # noqa: E501
        """Export denylist  # noqa: E501

        Begins an export of your rejection denylist. The denylist will be exported to a zip archive containing a single file named rejects.csv that includes the following fields: email, reason, detail, created_at, expires_at, last_event_at, expires_at.  # noqa: E501
        """
        (data) = self.rejects_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def rejects_with_http_info(self, body, **kwargs):  # noqa: E501
        """Export denylist  # noqa: E501

        Begins an export of your rejection denylist. The denylist will be exported to a zip archive containing a single file named rejects.csv that includes the following fields: email, reason, detail, created_at, expires_at, last_event_at, expires_at.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rejects" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/exports/rejects', 'POST',
            body=body_params,
            response_type='InlineResponse2005') # noqa: E501

    def whitelist(self, body = {}, **kwargs):  # noqa: E501
        """Export Allowlist  # noqa: E501

        Begins an export of your rejection allowlist. The allowlist will be exported to a zip archive containing a single file named allowlist.csv that includes the following fields: email, detail, created_at.  # noqa: E501
        """
        (data) = self.whitelist_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def whitelist_with_http_info(self, body, **kwargs):  # noqa: E501
        """Export Allowlist  # noqa: E501

        Begins an export of your rejection allowlist. The allowlist will be exported to a zip archive containing a single file named allowlist.csv that includes the following fields: email, detail, created_at.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method whitelist" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/exports/whitelist', 'POST',
            body=body_params,
            response_type='InlineResponse2006') # noqa: E501
