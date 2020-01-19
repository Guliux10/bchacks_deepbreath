# -*- coding: utf-8 -*- #
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""`gcloud service-directory services remove-iam-policy-binding` command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.service_directory import services
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iam import iam_util
from googlecloudsdk.command_lib.service_directory import resource_args

_RESOURCE_TYPE = 'service'


@base.Hidden
class RemoveIamPolicyBinding(base.Command):
  """Remove IAM policy binding from a service."""

  @staticmethod
  def Args(parser):
    resource_args.AddServiceResourceArg(
        parser,
        """to remove IAM policy binding from.""")

    iam_util.AddArgsForRemoveIamPolicyBinding(parser, add_condition=True)

  def Run(self, args):
    condition = iam_util.ValidateAndExtractCondition(args)
    client = services.ServicesClient()
    service_ref = args.CONCEPTS.service.Parse()

    iam_util.LogSetIamPolicy(service_ref.Name(), _RESOURCE_TYPE)
    return client.RemoveIamPolicyBinding(service_ref, args.member, args.role,
                                         condition)
