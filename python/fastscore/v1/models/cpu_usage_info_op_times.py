# coding: utf-8

"""
    FastScore API (proxy)

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CpuUsageInfoOpTimes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'unwrap_envelope': 'float',
        'unwrap_envelope_n': 'float',
        'wrap_envelope': 'float',
        'wrap_envelope_n': 'float',
        'decode_input_record': 'float',
        'decode_input_record_n': 'float',
        'type_check_input': 'float',
        'type_check_input_n': 'float'
    }

    attribute_map = {
        'unwrap_envelope': 'unwrap_envelope',
        'unwrap_envelope_n': 'unwrap_envelope_n',
        'wrap_envelope': 'wrap_envelope',
        'wrap_envelope_n': 'wrap_envelope_n',
        'decode_input_record': 'decode_input_record',
        'decode_input_record_n': 'decode_input_record_n',
        'type_check_input': 'type_check_input',
        'type_check_input_n': 'type_check_input_n'
    }

    def __init__(self, unwrap_envelope=None, unwrap_envelope_n=None, wrap_envelope=None, wrap_envelope_n=None, decode_input_record=None, decode_input_record_n=None, type_check_input=None, type_check_input_n=None):
        """
        CpuUsageInfoOpTimes - a model defined in Swagger
        """

        self._unwrap_envelope = None
        self._unwrap_envelope_n = None
        self._wrap_envelope = None
        self._wrap_envelope_n = None
        self._decode_input_record = None
        self._decode_input_record_n = None
        self._type_check_input = None
        self._type_check_input_n = None

        if unwrap_envelope is not None:
          self.unwrap_envelope = unwrap_envelope
        if unwrap_envelope_n is not None:
          self.unwrap_envelope_n = unwrap_envelope_n
        if wrap_envelope is not None:
          self.wrap_envelope = wrap_envelope
        if wrap_envelope_n is not None:
          self.wrap_envelope_n = wrap_envelope_n
        if decode_input_record is not None:
          self.decode_input_record = decode_input_record
        if decode_input_record_n is not None:
          self.decode_input_record_n = decode_input_record_n
        if type_check_input is not None:
          self.type_check_input = type_check_input
        if type_check_input_n is not None:
          self.type_check_input_n = type_check_input_n

    @property
    def unwrap_envelope(self):
        """
        Gets the unwrap_envelope of this CpuUsageInfoOpTimes.

        :return: The unwrap_envelope of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._unwrap_envelope

    @unwrap_envelope.setter
    def unwrap_envelope(self, unwrap_envelope):
        """
        Sets the unwrap_envelope of this CpuUsageInfoOpTimes.

        :param unwrap_envelope: The unwrap_envelope of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._unwrap_envelope = unwrap_envelope

    @property
    def unwrap_envelope_n(self):
        """
        Gets the unwrap_envelope_n of this CpuUsageInfoOpTimes.

        :return: The unwrap_envelope_n of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._unwrap_envelope_n

    @unwrap_envelope_n.setter
    def unwrap_envelope_n(self, unwrap_envelope_n):
        """
        Sets the unwrap_envelope_n of this CpuUsageInfoOpTimes.

        :param unwrap_envelope_n: The unwrap_envelope_n of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._unwrap_envelope_n = unwrap_envelope_n

    @property
    def wrap_envelope(self):
        """
        Gets the wrap_envelope of this CpuUsageInfoOpTimes.

        :return: The wrap_envelope of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._wrap_envelope

    @wrap_envelope.setter
    def wrap_envelope(self, wrap_envelope):
        """
        Sets the wrap_envelope of this CpuUsageInfoOpTimes.

        :param wrap_envelope: The wrap_envelope of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._wrap_envelope = wrap_envelope

    @property
    def wrap_envelope_n(self):
        """
        Gets the wrap_envelope_n of this CpuUsageInfoOpTimes.

        :return: The wrap_envelope_n of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._wrap_envelope_n

    @wrap_envelope_n.setter
    def wrap_envelope_n(self, wrap_envelope_n):
        """
        Sets the wrap_envelope_n of this CpuUsageInfoOpTimes.

        :param wrap_envelope_n: The wrap_envelope_n of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._wrap_envelope_n = wrap_envelope_n

    @property
    def decode_input_record(self):
        """
        Gets the decode_input_record of this CpuUsageInfoOpTimes.

        :return: The decode_input_record of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._decode_input_record

    @decode_input_record.setter
    def decode_input_record(self, decode_input_record):
        """
        Sets the decode_input_record of this CpuUsageInfoOpTimes.

        :param decode_input_record: The decode_input_record of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._decode_input_record = decode_input_record

    @property
    def decode_input_record_n(self):
        """
        Gets the decode_input_record_n of this CpuUsageInfoOpTimes.

        :return: The decode_input_record_n of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._decode_input_record_n

    @decode_input_record_n.setter
    def decode_input_record_n(self, decode_input_record_n):
        """
        Sets the decode_input_record_n of this CpuUsageInfoOpTimes.

        :param decode_input_record_n: The decode_input_record_n of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._decode_input_record_n = decode_input_record_n

    @property
    def type_check_input(self):
        """
        Gets the type_check_input of this CpuUsageInfoOpTimes.

        :return: The type_check_input of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._type_check_input

    @type_check_input.setter
    def type_check_input(self, type_check_input):
        """
        Sets the type_check_input of this CpuUsageInfoOpTimes.

        :param type_check_input: The type_check_input of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._type_check_input = type_check_input

    @property
    def type_check_input_n(self):
        """
        Gets the type_check_input_n of this CpuUsageInfoOpTimes.

        :return: The type_check_input_n of this CpuUsageInfoOpTimes.
        :rtype: float
        """
        return self._type_check_input_n

    @type_check_input_n.setter
    def type_check_input_n(self, type_check_input_n):
        """
        Sets the type_check_input_n of this CpuUsageInfoOpTimes.

        :param type_check_input_n: The type_check_input_n of this CpuUsageInfoOpTimes.
        :type: float
        """

        self._type_check_input_n = type_check_input_n

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
        if not isinstance(other, CpuUsageInfoOpTimes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
