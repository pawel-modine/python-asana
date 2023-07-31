# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectTemplateResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gid': 'str',
        'resource_type': 'str',
        'name': 'str',
        'description': 'str',
        'html_description': 'str',
        'public': 'bool',
        'owner': 'AllOfProjectTemplateResponseOwner',
        'team': 'ProjectTemplateBaseTeam',
        'requested_dates': 'list[ProjectTemplateBaseRequestedDates]',
        'color': 'str',
        'requested_roles': 'list[ProjectTemplateBaseRequestedRoles]'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'name': 'name',
        'description': 'description',
        'html_description': 'html_description',
        'public': 'public',
        'owner': 'owner',
        'team': 'team',
        'requested_dates': 'requested_dates',
        'color': 'color',
        'requested_roles': 'requested_roles'
    }

    def __init__(self, gid=None, resource_type=None, name=None, description=None, html_description=None, public=None, owner=None, team=None, requested_dates=None, color=None, requested_roles=None):  # noqa: E501
        """ProjectTemplateResponse - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._name = None
        self._description = None
        self._html_description = None
        self._public = None
        self._owner = None
        self._team = None
        self._requested_dates = None
        self._color = None
        self._requested_roles = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if html_description is not None:
            self.html_description = html_description
        if public is not None:
            self.public = public
        if owner is not None:
            self.owner = owner
        if team is not None:
            self.team = team
        if requested_dates is not None:
            self.requested_dates = requested_dates
        if color is not None:
            self.color = color
        if requested_roles is not None:
            self.requested_roles = requested_roles

    @property
    def gid(self):
        """Gets the gid of this ProjectTemplateResponse.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this ProjectTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ProjectTemplateResponse.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this ProjectTemplateResponse.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this ProjectTemplateResponse.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this ProjectTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ProjectTemplateResponse.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this ProjectTemplateResponse.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this ProjectTemplateResponse.  # noqa: E501

        Name of the project template.  # noqa: E501

        :return: The name of this ProjectTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectTemplateResponse.

        Name of the project template.  # noqa: E501

        :param name: The name of this ProjectTemplateResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectTemplateResponse.  # noqa: E501

        Free-form textual information associated with the project template  # noqa: E501

        :return: The description of this ProjectTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectTemplateResponse.

        Free-form textual information associated with the project template  # noqa: E501

        :param description: The description of this ProjectTemplateResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def html_description(self):
        """Gets the html_description of this ProjectTemplateResponse.  # noqa: E501

        The description of the project template with formatting as HTML.  # noqa: E501

        :return: The html_description of this ProjectTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._html_description

    @html_description.setter
    def html_description(self, html_description):
        """Sets the html_description of this ProjectTemplateResponse.

        The description of the project template with formatting as HTML.  # noqa: E501

        :param html_description: The html_description of this ProjectTemplateResponse.  # noqa: E501
        :type: str
        """

        self._html_description = html_description

    @property
    def public(self):
        """Gets the public of this ProjectTemplateResponse.  # noqa: E501

        True if the project template is public to its team.  # noqa: E501

        :return: The public of this ProjectTemplateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectTemplateResponse.

        True if the project template is public to its team.  # noqa: E501

        :param public: The public of this ProjectTemplateResponse.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def owner(self):
        """Gets the owner of this ProjectTemplateResponse.  # noqa: E501

        The current owner of the project template, may be null.  # noqa: E501

        :return: The owner of this ProjectTemplateResponse.  # noqa: E501
        :rtype: AllOfProjectTemplateResponseOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProjectTemplateResponse.

        The current owner of the project template, may be null.  # noqa: E501

        :param owner: The owner of this ProjectTemplateResponse.  # noqa: E501
        :type: AllOfProjectTemplateResponseOwner
        """

        self._owner = owner

    @property
    def team(self):
        """Gets the team of this ProjectTemplateResponse.  # noqa: E501


        :return: The team of this ProjectTemplateResponse.  # noqa: E501
        :rtype: ProjectTemplateBaseTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this ProjectTemplateResponse.


        :param team: The team of this ProjectTemplateResponse.  # noqa: E501
        :type: ProjectTemplateBaseTeam
        """

        self._team = team

    @property
    def requested_dates(self):
        """Gets the requested_dates of this ProjectTemplateResponse.  # noqa: E501

        Array of date variables in this project template. Calendar dates must be provided for these variables when instantiating a project.  # noqa: E501

        :return: The requested_dates of this ProjectTemplateResponse.  # noqa: E501
        :rtype: list[ProjectTemplateBaseRequestedDates]
        """
        return self._requested_dates

    @requested_dates.setter
    def requested_dates(self, requested_dates):
        """Sets the requested_dates of this ProjectTemplateResponse.

        Array of date variables in this project template. Calendar dates must be provided for these variables when instantiating a project.  # noqa: E501

        :param requested_dates: The requested_dates of this ProjectTemplateResponse.  # noqa: E501
        :type: list[ProjectTemplateBaseRequestedDates]
        """

        self._requested_dates = requested_dates

    @property
    def color(self):
        """Gets the color of this ProjectTemplateResponse.  # noqa: E501

        Color of the project template.  # noqa: E501

        :return: The color of this ProjectTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ProjectTemplateResponse.

        Color of the project template.  # noqa: E501

        :param color: The color of this ProjectTemplateResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["dark-pink", "dark-green", "dark-blue", "dark-red", "dark-teal", "dark-brown", "dark-orange", "dark-purple", "dark-warm-gray", "light-pink", "light-green", "light-blue", "light-red", "light-teal", "light-brown", "light-orange", "light-purple", "light-warm-gray", ""]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def requested_roles(self):
        """Gets the requested_roles of this ProjectTemplateResponse.  # noqa: E501

        Array of template roles in this project template. User Ids can be provided for these variables when instantiating a project to assign template tasks to the user.  # noqa: E501

        :return: The requested_roles of this ProjectTemplateResponse.  # noqa: E501
        :rtype: list[ProjectTemplateBaseRequestedRoles]
        """
        return self._requested_roles

    @requested_roles.setter
    def requested_roles(self, requested_roles):
        """Sets the requested_roles of this ProjectTemplateResponse.

        Array of template roles in this project template. User Ids can be provided for these variables when instantiating a project to assign template tasks to the user.  # noqa: E501

        :param requested_roles: The requested_roles of this ProjectTemplateResponse.  # noqa: E501
        :type: list[ProjectTemplateBaseRequestedRoles]
        """

        self._requested_roles = requested_roles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProjectTemplateResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other