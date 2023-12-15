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

class ProjectStatusesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_project_status_for_project(self, body, project_gid, opts, **kwargs):  # noqa: E501
        """Create a project status  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates` route.*  Creates a new status update on the project.  Returns the full record of the newly created project status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_status_for_project(body, project_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The project status to create. (required)
        :param str project_gid: Globally unique identifier for the project. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectStatusResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.create_project_status_for_project_with_http_info(body, project_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.create_project_status_for_project_with_http_info(body, project_gid, opts, **kwargs)  # noqa: E501
            return data

    def create_project_status_for_project_with_http_info(self, body, project_gid, opts, **kwargs):  # noqa: E501
        """Create a project status  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates` route.*  Creates a new status update on the project.  Returns the full record of the newly created project status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_status_for_project_with_http_info(body, project_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The project status to create. (required)
        :param str project_gid: Globally unique identifier for the project. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectStatusResponseData
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
                    " to method create_project_status_for_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if (body is None):
            raise ValueError("Missing the required parameter `body` when calling `create_project_status_for_project`")  # noqa: E501
        # verify the required parameter 'project_gid' is set
        if (project_gid is None):
            raise ValueError("Missing the required parameter `project_gid` when calling `create_project_status_for_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['project_gid'] = project_gid  # noqa: E501

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
                '/projects/{project_gid}/project_statuses', 'POST',
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
                '/projects/{project_gid}/project_statuses', 'POST',
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
            '/projects/{project_gid}/project_statuses', 'POST',
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

    def delete_project_status(self, project_status_gid, **kwargs):  # noqa: E501
        """Delete a project status  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Deletes a specific, existing project status update.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_status(project_status_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_status_gid: The project status update to get. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.delete_project_status_with_http_info(project_status_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_project_status_with_http_info(project_status_gid, **kwargs)  # noqa: E501
            return data

    def delete_project_status_with_http_info(self, project_status_gid, **kwargs):  # noqa: E501
        """Delete a project status  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Deletes a specific, existing project status update.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_status_with_http_info(project_status_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_status_gid: The project status update to get. (required)
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
                    " to method delete_project_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_status_gid' is set
        if (project_status_gid is None):
            raise ValueError("Missing the required parameter `project_status_gid` when calling `delete_project_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['project_status_gid'] = project_status_gid  # noqa: E501

        query_params = []


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
                '/project_statuses/{project_status_gid}', 'DELETE',
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
                '/project_statuses/{project_status_gid}', 'DELETE',
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
            '/project_statuses/{project_status_gid}', 'DELETE',
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

    def get_project_status(self, project_status_gid, opts, **kwargs):  # noqa: E501
        """Get a project status  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Returns the complete record for a single status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_status(project_status_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_status_gid: The project status update to get. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectStatusResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_project_status_with_http_info(project_status_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_status_with_http_info(project_status_gid, opts, **kwargs)  # noqa: E501
            return data

    def get_project_status_with_http_info(self, project_status_gid, opts, **kwargs):  # noqa: E501
        """Get a project status  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Returns the complete record for a single status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_status_with_http_info(project_status_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_status_gid: The project status update to get. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectStatusResponseData
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
                    " to method get_project_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_status_gid' is set
        if (project_status_gid is None):
            raise ValueError("Missing the required parameter `project_status_gid` when calling `get_project_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['project_status_gid'] = project_status_gid  # noqa: E501

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
                '/project_statuses/{project_status_gid}', 'GET',
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
                '/project_statuses/{project_status_gid}', 'GET',
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
            '/project_statuses/{project_status_gid}', 'GET',
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

    def get_project_statuses_for_project(self, project_gid, opts, **kwargs):  # noqa: E501
        """Get statuses from a project  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates` route.*  Returns the compact project status update records for all updates on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_statuses_for_project(project_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_gid: Globally unique identifier for the project. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectStatusResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_project_statuses_for_project_with_http_info(project_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_statuses_for_project_with_http_info(project_gid, opts, **kwargs)  # noqa: E501
            return data

    def get_project_statuses_for_project_with_http_info(self, project_gid, opts, **kwargs):  # noqa: E501
        """Get statuses from a project  # noqa: E501

        *Deprecated: new integrations should prefer the `/status_updates` route.*  Returns the compact project status update records for all updates on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_statuses_for_project_with_http_info(project_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_gid: Globally unique identifier for the project. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: ProjectStatusResponseArray
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
                    " to method get_project_statuses_for_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_gid' is set
        if (project_gid is None):
            raise ValueError("Missing the required parameter `project_gid` when calling `get_project_statuses_for_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['project_gid'] = project_gid  # noqa: E501

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
                '/projects/{project_gid}/project_statuses', 'GET',
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
                    "resource_path": '/projects/{project_gid}/project_statuses',
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
            '/projects/{project_gid}/project_statuses', 'GET',
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
