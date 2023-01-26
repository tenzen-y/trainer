# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.6.0rc0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class KubeflowOrgV1XGBoostJobSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'run_policy': 'V1RunPolicy',
        'xgb_replica_specs': 'dict(str, V1ReplicaSpec)'
    }

    attribute_map = {
        'run_policy': 'runPolicy',
        'xgb_replica_specs': 'xgbReplicaSpecs'
    }

    def __init__(self, run_policy=None, xgb_replica_specs=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV1XGBoostJobSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._run_policy = None
        self._xgb_replica_specs = None
        self.discriminator = None

        self.run_policy = run_policy
        self.xgb_replica_specs = xgb_replica_specs

    @property
    def run_policy(self):
        """Gets the run_policy of this KubeflowOrgV1XGBoostJobSpec.  # noqa: E501


        :return: The run_policy of this KubeflowOrgV1XGBoostJobSpec.  # noqa: E501
        :rtype: V1RunPolicy
        """
        return self._run_policy

    @run_policy.setter
    def run_policy(self, run_policy):
        """Sets the run_policy of this KubeflowOrgV1XGBoostJobSpec.


        :param run_policy: The run_policy of this KubeflowOrgV1XGBoostJobSpec.  # noqa: E501
        :type: V1RunPolicy
        """
        if self.local_vars_configuration.client_side_validation and run_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `run_policy`, must not be `None`")  # noqa: E501

        self._run_policy = run_policy

    @property
    def xgb_replica_specs(self):
        """Gets the xgb_replica_specs of this KubeflowOrgV1XGBoostJobSpec.  # noqa: E501


        :return: The xgb_replica_specs of this KubeflowOrgV1XGBoostJobSpec.  # noqa: E501
        :rtype: dict(str, V1ReplicaSpec)
        """
        return self._xgb_replica_specs

    @xgb_replica_specs.setter
    def xgb_replica_specs(self, xgb_replica_specs):
        """Sets the xgb_replica_specs of this KubeflowOrgV1XGBoostJobSpec.


        :param xgb_replica_specs: The xgb_replica_specs of this KubeflowOrgV1XGBoostJobSpec.  # noqa: E501
        :type: dict(str, V1ReplicaSpec)
        """
        if self.local_vars_configuration.client_side_validation and xgb_replica_specs is None:  # noqa: E501
            raise ValueError("Invalid value for `xgb_replica_specs`, must not be `None`")  # noqa: E501

        self._xgb_replica_specs = xgb_replica_specs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubeflowOrgV1XGBoostJobSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV1XGBoostJobSpec):
            return True

        return self.to_dict() != other.to_dict()
