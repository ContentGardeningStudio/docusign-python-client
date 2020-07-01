# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CommentHistoryResult(object):
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
        'comments': 'list[Comment]',
        'count': 'int',
        'end_timetoken': 'str',
        'start_timetoken': 'str'
    }

    attribute_map = {
        'comments': 'comments',
        'count': 'count',
        'end_timetoken': 'endTimetoken',
        'start_timetoken': 'startTimetoken'
    }

    def __init__(self, comments=None, count=None, end_timetoken=None, start_timetoken=None):  # noqa: E501
        """CommentHistoryResult - a model defined in Swagger"""  # noqa: E501

        self._comments = None
        self._count = None
        self._end_timetoken = None
        self._start_timetoken = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if count is not None:
            self.count = count
        if end_timetoken is not None:
            self.end_timetoken = end_timetoken
        if start_timetoken is not None:
            self.start_timetoken = start_timetoken

    @property
    def comments(self):
        """Gets the comments of this CommentHistoryResult.  # noqa: E501

          # noqa: E501

        :return: The comments of this CommentHistoryResult.  # noqa: E501
        :rtype: list[Comment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CommentHistoryResult.

          # noqa: E501

        :param comments: The comments of this CommentHistoryResult.  # noqa: E501
        :type: list[Comment]
        """

        self._comments = comments

    @property
    def count(self):
        """Gets the count of this CommentHistoryResult.  # noqa: E501

          # noqa: E501

        :return: The count of this CommentHistoryResult.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CommentHistoryResult.

          # noqa: E501

        :param count: The count of this CommentHistoryResult.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def end_timetoken(self):
        """Gets the end_timetoken of this CommentHistoryResult.  # noqa: E501

          # noqa: E501

        :return: The end_timetoken of this CommentHistoryResult.  # noqa: E501
        :rtype: str
        """
        return self._end_timetoken

    @end_timetoken.setter
    def end_timetoken(self, end_timetoken):
        """Sets the end_timetoken of this CommentHistoryResult.

          # noqa: E501

        :param end_timetoken: The end_timetoken of this CommentHistoryResult.  # noqa: E501
        :type: str
        """

        self._end_timetoken = end_timetoken

    @property
    def start_timetoken(self):
        """Gets the start_timetoken of this CommentHistoryResult.  # noqa: E501

          # noqa: E501

        :return: The start_timetoken of this CommentHistoryResult.  # noqa: E501
        :rtype: str
        """
        return self._start_timetoken

    @start_timetoken.setter
    def start_timetoken(self, start_timetoken):
        """Sets the start_timetoken of this CommentHistoryResult.

          # noqa: E501

        :param start_timetoken: The start_timetoken of this CommentHistoryResult.  # noqa: E501
        :type: str
        """

        self._start_timetoken = start_timetoken

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
        if issubclass(CommentHistoryResult, dict):
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
        if not isinstance(other, CommentHistoryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other