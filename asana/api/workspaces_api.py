# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
from asana.api_client import ApiClient
from asana.pagination.event_iterator import EventIterator
from asana.pagination.page_iterator import PageIterator

class WorkspacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_user_for_workspace(self, body, workspace_gid, opts, **kwargs):  # noqa: E501
        """Add a user to a workspace or organization  # noqa: E501

        Add a user to a workspace or organization. The user can be referenced by their globally unique user ID or their email address. Returns the full user record for the invited user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_for_workspace(body, workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The user to add to the workspace. (required)
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: UserBaseResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.add_user_for_workspace_with_http_info(body, workspace_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.add_user_for_workspace_with_http_info(body, workspace_gid, opts, **kwargs)  # noqa: E501
            return data

    def add_user_for_workspace_with_http_info(self, body, workspace_gid, opts, **kwargs):  # noqa: E501
        """Add a user to a workspace or organization  # noqa: E501

        Add a user to a workspace or organization. The user can be referenced by their globally unique user ID or their email address. Returns the full user record for the invited user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_for_workspace_with_http_info(body, workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The user to add to the workspace. (required)
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: UserBaseResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user_for_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if (body is None):
            raise ValueError("Missing the required parameter `body` when calling `add_user_for_workspace`")  # noqa: E501
        # verify the required parameter 'workspace_gid' is set
        if (workspace_gid is None):
            raise ValueError("Missing the required parameter `workspace_gid` when calling `add_user_for_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['workspace_gid'] = workspace_gid  # noqa: E501

        query_params = []
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = body

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/workspaces/{workspace_gid}/addUser', 'POST',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/workspaces/{workspace_gid}/addUser', 'POST',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/workspaces/{workspace_gid}/addUser', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workspace(self, workspace_gid, opts, **kwargs):  # noqa: E501
        """Get a workspace  # noqa: E501

        Returns the full workspace record for a single workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace(workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: WorkspaceResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_workspace_with_http_info(workspace_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_with_http_info(workspace_gid, opts, **kwargs)  # noqa: E501
            return data

    def get_workspace_with_http_info(self, workspace_gid, opts, **kwargs):  # noqa: E501
        """Get a workspace  # noqa: E501

        Returns the full workspace record for a single workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_with_http_info(workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: WorkspaceResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_gid' is set
        if (workspace_gid is None):
            raise ValueError("Missing the required parameter `workspace_gid` when calling `get_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['workspace_gid'] = workspace_gid  # noqa: E501

        query_params = []
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/workspaces/{workspace_gid}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/workspaces/{workspace_gid}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/workspaces/{workspace_gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workspaces(self, opts, **kwargs):  # noqa: E501
        """Get multiple workspaces  # noqa: E501

        Returns the compact records for all workspaces visible to the authorized user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: WorkspaceResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_workspaces_with_http_info(opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspaces_with_http_info(opts, **kwargs)  # noqa: E501
            return data

    def get_workspaces_with_http_info(self, opts, **kwargs):  # noqa: E501
        """Get multiple workspaces  # noqa: E501

        Returns the compact records for all workspaces visible to the authorized user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: WorkspaceResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspaces" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/workspaces', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            query_params["limit"] = query_params.get("limit", self.api_client.configuration.page_limit)
            return PageIterator(
                self.api_client,
                {
                    "resource_path": '/workspaces',
                    "method": 'GET',
                    "path_params": path_params,
                    "query_params": query_params,
                    "header_params": header_params,
                    "body": body_params,
                    "post_params": form_params,
                    "files": local_var_files,
                    "response_type": object,
                    "auth_settings": auth_settings,
                    "async_req": params.get('async_req'),
                    "_return_http_data_only": params.get('_return_http_data_only'),
                    "_preload_content": params.get('_preload_content', True),
                    "_request_timeout": params.get('_request_timeout'),
                    "collection_formats": collection_formats
                },
                **kwargs
            ).items()
        else:
            return self.api_client.call_api(
            '/workspaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_user_for_workspace(self, body, workspace_gid, **kwargs):  # noqa: E501
        """Remove a user from a workspace or organization  # noqa: E501

        Remove a user from a workspace or organization. The user making this call must be an admin in the workspace. The user can be referenced by their globally unique user ID or their email address. Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_for_workspace(body, workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The user to remove from the workspace. (required)
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.remove_user_for_workspace_with_http_info(body, workspace_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_user_for_workspace_with_http_info(body, workspace_gid, **kwargs)  # noqa: E501
            return data

    def remove_user_for_workspace_with_http_info(self, body, workspace_gid, **kwargs):  # noqa: E501
        """Remove a user from a workspace or organization  # noqa: E501

        Remove a user from a workspace or organization. The user making this call must be an admin in the workspace. The user can be referenced by their globally unique user ID or their email address. Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_for_workspace_with_http_info(body, workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The user to remove from the workspace. (required)
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_user_for_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if (body is None):
            raise ValueError("Missing the required parameter `body` when calling `remove_user_for_workspace`")  # noqa: E501
        # verify the required parameter 'workspace_gid' is set
        if (workspace_gid is None):
            raise ValueError("Missing the required parameter `workspace_gid` when calling `remove_user_for_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['workspace_gid'] = workspace_gid  # noqa: E501

        query_params = []


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = body

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/workspaces/{workspace_gid}/removeUser', 'POST',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/workspaces/{workspace_gid}/removeUser', 'POST',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/workspaces/{workspace_gid}/removeUser', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_workspace(self, body, workspace_gid, opts, **kwargs):  # noqa: E501
        """Update a workspace  # noqa: E501

        A specific, existing workspace can be updated by making a PUT request on the URL for that workspace. Only the fields provided in the data block will be updated; any unspecified fields will remain unchanged. Currently the only field that can be modified for a workspace is its name. Returns the complete, updated workspace record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_workspace(body, workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The workspace object with all updated properties. (required)
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: WorkspaceResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.update_workspace_with_http_info(body, workspace_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.update_workspace_with_http_info(body, workspace_gid, opts, **kwargs)  # noqa: E501
            return data

    def update_workspace_with_http_info(self, body, workspace_gid, opts, **kwargs):  # noqa: E501
        """Update a workspace  # noqa: E501

        A specific, existing workspace can be updated by making a PUT request on the URL for that workspace. Only the fields provided in the data block will be updated; any unspecified fields will remain unchanged. Currently the only field that can be modified for a workspace is its name. Returns the complete, updated workspace record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_workspace_with_http_info(body, workspace_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The workspace object with all updated properties. (required)
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: WorkspaceResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if (body is None):
            raise ValueError("Missing the required parameter `body` when calling `update_workspace`")  # noqa: E501
        # verify the required parameter 'workspace_gid' is set
        if (workspace_gid is None):
            raise ValueError("Missing the required parameter `workspace_gid` when calling `update_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['workspace_gid'] = workspace_gid  # noqa: E501

        query_params = []
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = body

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/workspaces/{workspace_gid}', 'PUT',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/workspaces/{workspace_gid}', 'PUT',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/workspaces/{workspace_gid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
