# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from nose.tools import assert_equal
import mock

import botocore.session


REGION = 'us-east-1'

SERVICE_TO_CLASS_NAME = {
    'autoscaling': 'AutoScaling',
    'cloudformation': 'CloudFormation',
    'cloudfront': 'CloudFront',
    'cloudhsm': 'CloudHSM',
    'cloudsearch': 'CloudSearch',
    'cloudsearchdomain': 'CloudSearchDomain',
    'cloudtrail': 'CloudTrail',
    'cloudwatch': 'CloudWatch',
    'codedeploy': 'CodeDeploy',
    'cognito-identity': 'CognitoIdentity',
    'cognito-sync': 'CognitoSync',
    'config': 'ConfigService',
    'datapipeline': 'DataPipeline',
    'directconnect': 'DirectConnect',
    'ds': 'DirectoryService',
    'dynamodb': 'DynamoDB',
    'ec2': 'EC2',
    'ecs': 'ECS',
    'efs': 'EFS',
    'elasticache': 'ElastiCache',
    'elasticbeanstalk': 'ElasticBeanstalk',
    'elastictranscoder': 'ElasticTranscoder',
    'elb': 'ElasticLoadBalancing',
    'emr': 'EMR',
    'glacier': 'Glacier',
    'iam': 'IAM',
    'importexport': 'ImportExport',
    'kinesis': 'Kinesis',
    'kms': 'KMS',
    'lambda': 'Lambda',
    'logs': 'CloudWatchLogs',
    'machinelearning': 'MachineLearning',
    'opsworks': 'OpsWorks',
    'rds': 'RDS',
    'redshift': 'Redshift',
    'route53': 'Route53',
    'route53domains': 'Route53Domains',
    's3': 'S3',
    'sdb': 'SimpleDB',
    'ses': 'SES',
    'sns': 'SNS',
    'sqs': 'SQS',
    'ssm': 'SSM',
    'storagegateway': 'StorageGateway',
    'sts': 'STS',
    'support': 'Support',
    'swf': 'SWF',
    'workspaces': 'WorkSpaces'
}


def test_client_has_correct_class_name():
    session = botocore.session.get_session()
    session.get_credentials = mock.Mock(return_value=mock.Mock())
    for service_name in SERVICE_TO_CLASS_NAME:
        client = session.create_client(service_name, REGION)
        yield (_assert_class_name_matches_ref_class_name, client,
               SERVICE_TO_CLASS_NAME[service_name])


def _assert_class_name_matches_ref_class_name(client, ref_class_name):
    assert_equal(client.__class__.__name__, ref_class_name)
