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

class MessagesApi(object):
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

    def cancel_scheduled(self, body = {}, **kwargs):  # noqa: E501
        """Cancel scheduled email  # noqa: E501

        Cancels a scheduled email.  # noqa: E501
        """
        (data) = self.cancel_scheduled_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def cancel_scheduled_with_http_info(self, body, **kwargs):  # noqa: E501
        """Cancel scheduled email  # noqa: E501

        Cancels a scheduled email.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_scheduled" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/cancel-scheduled', 'POST',
            body=body_params,
            response_type='list[InlineResponse20035]') # noqa: E501

    def content(self, body = {}, **kwargs):  # noqa: E501
        """Get message content  # noqa: E501

        Get the full content of a recently sent message.  # noqa: E501
        """
        (data) = self.content_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def content_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get message content  # noqa: E501

        Get the full content of a recently sent message.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/content', 'POST',
            body=body_params,
            response_type='InlineResponse20033') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get message info  # noqa: E501

        Get the information for a single recently sent message.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get message info  # noqa: E501

        Get the information for a single recently sent message.  # noqa: E501
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
            '/messages/info', 'POST',
            body=body_params,
            response_type='InlineResponse20032') # noqa: E501

    def list_scheduled(self, body = {}, **kwargs):  # noqa: E501
        """List scheduled emails  # noqa: E501

        Queries your scheduled emails.  # noqa: E501
        """
        (data) = self.list_scheduled_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_scheduled_with_http_info(self, body, **kwargs):  # noqa: E501
        """List scheduled emails  # noqa: E501

        Queries your scheduled emails.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_scheduled" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/list-scheduled', 'POST',
            body=body_params,
            response_type='list[InlineResponse20035]') # noqa: E501

    def parse(self, body = {}, **kwargs):  # noqa: E501
        """Parse mime document  # noqa: E501

        Parse the full MIME document for an email message, returning the content of the message broken into its constituent pieces.  # noqa: E501
        """
        (data) = self.parse_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def parse_with_http_info(self, body, **kwargs):  # noqa: E501
        """Parse mime document  # noqa: E501

        Parse the full MIME document for an email message, returning the content of the message broken into its constituent pieces.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method parse" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/parse', 'POST',
            body=body_params,
            response_type='InlineResponse20034') # noqa: E501

    def reschedule(self, body = {}, **kwargs):  # noqa: E501
        """Reschedule email  # noqa: E501

        Reschedules a scheduled email.  # noqa: E501
        """
        (data) = self.reschedule_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def reschedule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Reschedule email  # noqa: E501

        Reschedules a scheduled email.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reschedule" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/reschedule', 'POST',
            body=body_params,
            response_type='list[InlineResponse20035]') # noqa: E501

    def search(self, body = {}, **kwargs):  # noqa: E501
        """Search messages by date  # noqa: E501

        Search recently sent messages and optionally narrow by date range, tags, senders, and API keys. If no date range is specified, results within the last 7 days are returned. This method may be called up to 20 times per minute. If you need the data more often, you can use /messages/info.json to get the information for a single message, or webhooks to push activity to your own application for querying.  # noqa: E501
        """
        (data) = self.search_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def search_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search messages by date  # noqa: E501

        Search recently sent messages and optionally narrow by date range, tags, senders, and API keys. If no date range is specified, results within the last 7 days are returned. This method may be called up to 20 times per minute. If you need the data more often, you can use /messages/info.json to get the information for a single message, or webhooks to push activity to your own application for querying.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/search', 'POST',
            body=body_params,
            response_type='list[InlineResponse20030]') # noqa: E501

    def search_time_series(self, body = {}, **kwargs):  # noqa: E501
        """Search messages by hour  # noqa: E501

        Search the content of recently sent messages and return the aggregated hourly stats for matching messages.  # noqa: E501
        """
        (data) = self.search_time_series_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def search_time_series_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search messages by hour  # noqa: E501

        Search the content of recently sent messages and return the aggregated hourly stats for matching messages.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_time_series" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/search-time-series', 'POST',
            body=body_params,
            response_type='list[InlineResponse20031]') # noqa: E501

    def send(self, body = {}, **kwargs):  # noqa: E501
        """Send new message  # noqa: E501

        Send a new transactional message through the Transactional API.  # noqa: E501
        """
        (data) = self.send_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def send_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send new message  # noqa: E501

        Send a new transactional message through the Transactional API.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/send', 'POST',
            body=body_params,
            response_type='list[InlineResponse20028]') # noqa: E501

    def send_raw(self, body = {}, **kwargs):  # noqa: E501
        """Send mime document  # noqa: E501

        Take a raw MIME document for a message, and send it exactly as if it were sent through the Transactional API's SMTP servers.  # noqa: E501
        """
        (data) = self.send_raw_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def send_raw_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send mime document  # noqa: E501

        Take a raw MIME document for a message, and send it exactly as if it were sent through the Transactional API's SMTP servers.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_raw" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/send-raw', 'POST',
            body=body_params,
            response_type='object') # noqa: E501

    def send_template(self, body = {}, **kwargs):  # noqa: E501
        """Send using message template  # noqa: E501

        Send a new transactional message through the Transactional API using a template.  # noqa: E501
        """
        (data) = self.send_template_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def send_template_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send using message template  # noqa: E501

        Send a new transactional message through the Transactional API using a template.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_template" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/messages/send-template', 'POST',
            body=body_params,
            response_type='list[InlineResponse20029]') # noqa: E501
