# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserInfoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, envelope_id=None, language=None, seal=None, sender=None, user=None):
        """
        UserInfoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'envelope_id': 'str',
            'language': 'str',
            'seal': 'Seal',
            'sender': 'Sender',
            'user': 'User'
        }

        self.attribute_map = {
            'envelope_id': 'envelopeId',
            'language': 'language',
            'seal': 'seal',
            'sender': 'sender',
            'user': 'user'
        }

        self._envelope_id = envelope_id
        self._language = language
        self._seal = seal
        self._sender = sender
        self._user = user

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this UserInfoResponse.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this UserInfoResponse.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this UserInfoResponse.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this UserInfoResponse.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def language(self):
        """
        Gets the language of this UserInfoResponse.
        

        :return: The language of this UserInfoResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this UserInfoResponse.
        

        :param language: The language of this UserInfoResponse.
        :type: str
        """

        self._language = language

    @property
    def seal(self):
        """
        Gets the seal of this UserInfoResponse.

        :return: The seal of this UserInfoResponse.
        :rtype: Seal
        """
        return self._seal

    @seal.setter
    def seal(self, seal):
        """
        Sets the seal of this UserInfoResponse.

        :param seal: The seal of this UserInfoResponse.
        :type: Seal
        """

        self._seal = seal

    @property
    def sender(self):
        """
        Gets the sender of this UserInfoResponse.

        :return: The sender of this UserInfoResponse.
        :rtype: Sender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this UserInfoResponse.

        :param sender: The sender of this UserInfoResponse.
        :type: Sender
        """

        self._sender = sender

    @property
    def user(self):
        """
        Gets the user of this UserInfoResponse.

        :return: The user of this UserInfoResponse.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this UserInfoResponse.

        :param user: The user of this UserInfoResponse.
        :type: User
        """

        self._user = user

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other