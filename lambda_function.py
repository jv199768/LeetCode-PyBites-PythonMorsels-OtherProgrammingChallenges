import json
import boto3


def lambda_handler(event, context):
    # Create an EC2 client object
    ec2 = boto3.client('ec2')

    # Get all running instances
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            },
        ]
    )

    print(instances)

    # Stop each instance
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Stopping instance {instance['InstanceId']}")
