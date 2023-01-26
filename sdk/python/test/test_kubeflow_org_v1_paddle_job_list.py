# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.6.0rc0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.kubeflow_org_v1_paddle_job_list import KubeflowOrgV1PaddleJobList  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV1PaddleJobList(unittest.TestCase):
    """KubeflowOrgV1PaddleJobList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV1PaddleJobList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v1_paddle_job_list.KubeflowOrgV1PaddleJobList()  # noqa: E501
        if include_optional :
            return KubeflowOrgV1PaddleJobList(
                api_version = '0', 
                items = [
                    kubeflow_org_v1_paddle_job.KubeflowOrgV1PaddleJob(
                        api_version = '0', 
                        kind = '0', 
                        metadata = None, 
                        spec = kubeflow_org_v1_paddle_job_spec.KubeflowOrgV1PaddleJobSpec(
                            elastic_policy = kubeflow_org_v1_paddle_elastic_policy.KubeflowOrgV1PaddleElasticPolicy(
                                max_replicas = 56, 
                                max_restarts = 56, 
                                metrics = [
                                    None
                                    ], 
                                min_replicas = 56, ), 
                            paddle_replica_specs = {
                                'key' : V1ReplicaSpec(
                                    replicas = 56, 
                                    restart_policy = '0', 
                                    template = None, )
                                }, 
                            run_policy = V1RunPolicy(
                                active_deadline_seconds = 56, 
                                backoff_limit = 56, 
                                clean_pod_policy = '0', 
                                scheduling_policy = V1SchedulingPolicy(
                                    min_available = 56, 
                                    min_resources = {
                                        'key' : None
                                        }, 
                                    priority_class = '0', 
                                    queue = '0', 
                                    schedule_timeout_seconds = 56, ), 
                                ttl_seconds_after_finished = 56, ), ), 
                        status = V1JobStatus(
                            completion_time = None, 
                            conditions = [
                                V1JobCondition(
                                    last_transition_time = None, 
                                    last_update_time = None, 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            last_reconcile_time = None, 
                            replica_statuses = {
                                'key' : V1ReplicaStatus(
                                    active = 56, 
                                    failed = 56, 
                                    label_selector = None, 
                                    selector = '0', 
                                    succeeded = 56, )
                                }, 
                            start_time = None, ), )
                    ], 
                kind = '0', 
                metadata = None
            )
        else :
            return KubeflowOrgV1PaddleJobList(
                items = [
                    kubeflow_org_v1_paddle_job.KubeflowOrgV1PaddleJob(
                        api_version = '0', 
                        kind = '0', 
                        metadata = None, 
                        spec = kubeflow_org_v1_paddle_job_spec.KubeflowOrgV1PaddleJobSpec(
                            elastic_policy = kubeflow_org_v1_paddle_elastic_policy.KubeflowOrgV1PaddleElasticPolicy(
                                max_replicas = 56, 
                                max_restarts = 56, 
                                metrics = [
                                    None
                                    ], 
                                min_replicas = 56, ), 
                            paddle_replica_specs = {
                                'key' : V1ReplicaSpec(
                                    replicas = 56, 
                                    restart_policy = '0', 
                                    template = None, )
                                }, 
                            run_policy = V1RunPolicy(
                                active_deadline_seconds = 56, 
                                backoff_limit = 56, 
                                clean_pod_policy = '0', 
                                scheduling_policy = V1SchedulingPolicy(
                                    min_available = 56, 
                                    min_resources = {
                                        'key' : None
                                        }, 
                                    priority_class = '0', 
                                    queue = '0', 
                                    schedule_timeout_seconds = 56, ), 
                                ttl_seconds_after_finished = 56, ), ), 
                        status = V1JobStatus(
                            completion_time = None, 
                            conditions = [
                                V1JobCondition(
                                    last_transition_time = None, 
                                    last_update_time = None, 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            last_reconcile_time = None, 
                            replica_statuses = {
                                'key' : V1ReplicaStatus(
                                    active = 56, 
                                    failed = 56, 
                                    label_selector = None, 
                                    selector = '0', 
                                    succeeded = 56, )
                                }, 
                            start_time = None, ), )
                    ],
        )

    def testKubeflowOrgV1PaddleJobList(self):
        """Test KubeflowOrgV1PaddleJobList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
