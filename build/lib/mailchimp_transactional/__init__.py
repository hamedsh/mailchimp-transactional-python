# coding: utf-8

# flake8: noqa

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.50
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from mailchimp_transactional.api.allowlists_api import AllowlistsApi
from mailchimp_transactional.api.exports_api import ExportsApi
from mailchimp_transactional.api.inbound_api import InboundApi
from mailchimp_transactional.api.ips_api import IpsApi
from mailchimp_transactional.api.messages_api import MessagesApi
from mailchimp_transactional.api.metadata_api import MetadataApi
from mailchimp_transactional.api.rejects_api import RejectsApi
from mailchimp_transactional.api.senders_api import SendersApi
from mailchimp_transactional.api.subaccounts_api import SubaccountsApi
from mailchimp_transactional.api.tags_api import TagsApi
from mailchimp_transactional.api.templates_api import TemplatesApi
from mailchimp_transactional.api.urls_api import UrlsApi
from mailchimp_transactional.api.users_api import UsersApi
from mailchimp_transactional.api.webhooks_api import WebhooksApi
from mailchimp_transactional.api.whitelists_api import WhitelistsApi


from mailchimp_transactional.api_client import ApiClient

class Client(object):
  def __init__(self, api_key = ''):
    self.api_key = api_key
    self.api_client = ApiClient()

    self.allowlists = AllowlistsApi(self.api_key, self.api_client)
    self.exports = ExportsApi(self.api_key, self.api_client)
    self.inbound = InboundApi(self.api_key, self.api_client)
    self.ips = IpsApi(self.api_key, self.api_client)
    self.messages = MessagesApi(self.api_key, self.api_client)
    self.metadata = MetadataApi(self.api_key, self.api_client)
    self.rejects = RejectsApi(self.api_key, self.api_client)
    self.senders = SendersApi(self.api_key, self.api_client)
    self.subaccounts = SubaccountsApi(self.api_key, self.api_client)
    self.tags = TagsApi(self.api_key, self.api_client)
    self.templates = TemplatesApi(self.api_key, self.api_client)
    self.urls = UrlsApi(self.api_key, self.api_client)
    self.users = UsersApi(self.api_key, self.api_client)
    self.webhooks = WebhooksApi(self.api_key, self.api_client)
    self.whitelists = WhitelistsApi(self.api_key, self.api_client)
    

  def set_api_key(self, api_key = ''):
    self.api_key = api_key
    self.allowlists = AllowlistsApi(self.api_key, self.api_client)
    self.exports = ExportsApi(self.api_key, self.api_client)
    self.inbound = InboundApi(self.api_key, self.api_client)
    self.ips = IpsApi(self.api_key, self.api_client)
    self.messages = MessagesApi(self.api_key, self.api_client)
    self.metadata = MetadataApi(self.api_key, self.api_client)
    self.rejects = RejectsApi(self.api_key, self.api_client)
    self.senders = SendersApi(self.api_key, self.api_client)
    self.subaccounts = SubaccountsApi(self.api_key, self.api_client)
    self.tags = TagsApi(self.api_key, self.api_client)
    self.templates = TemplatesApi(self.api_key, self.api_client)
    self.urls = UrlsApi(self.api_key, self.api_client)
    self.users = UsersApi(self.api_key, self.api_client)
    self.webhooks = WebhooksApi(self.api_key, self.api_client)
    self.whitelists = WhitelistsApi(self.api_key, self.api_client)
    

  def set_default_output_format(self, output_format):
    self.api_client.set_default_output_format(output_format)

  def set_timeout(self, timeout):
    self.api_client.set_timeout(timeout)