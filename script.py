from datetime import datetime
import time
import boto3


def wait_for_ami_available(ami_id):
    session = boto3.Session()
    ec2_client = session.client('ec2')

    while True:
        response = ec2_client.describe_images(ImageIds=[ami_id])
        ami_state = response['Images'][0]['State']
        if ami_state == 'available':
            break
        time.sleep(10)


def create_ami(instance_id):
    session = boto3.Session()
    ec2_client = session.client('ec2')

    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_name = response['Reservations'][0]['Instances'][0]['Tags'][0]['Value']

    current_datetime = datetime.now()
    ami_name = f"{instance_name}-{current_datetime.strftime('%d-%m-%Y-%H_%M')}"

    response = ec2_client.create_image(
        InstanceId=instance_id,
        Name=ami_name,
        Description='AMI created by automation script',
        NoReboot=True
    )

    ami_id = response['ImageId']
    wait_for_ami_available(ami_id)
    
    return ami_id


def create_launch_template_version(launch_template_name, ami_id):
    session = boto3.Session()
    ec2_client = session.client('ec2')

    response = ec2_client.create_launch_template_version(
        LaunchTemplateName=launch_template_name,
        SourceVersion='$Latest',
        LaunchTemplateData={
            'ImageId': ami_id,
            'Description': ami_name
        }
    )

    return response['LaunchTemplateVersion']['VersionNumber']


def update_auto_scaling_capacity(auto_scaling_group_name, desired_capacity):
    session = boto3.Session()
    autoscaling_client = session.client('autoscaling')

    response = autoscaling_client.update_auto_scaling_group(
        AutoScalingGroupName=auto_scaling_group_name,
        DesiredCapacity=desired_capacity
    )

    return response


def lambda_handler(event, context):
    instance_id = 'i-XXXXXXXXXXXX'
    launch_template_name = 'XXXXXXXXXXXX'
    auto_scaling_group_name = 'XXXXXXXXXXXX'
    desired_capacity = 1  # Set the desired capacity for the autoscaler to 1

    # Create AMI
    created_ami_id = create_ami(instance_id)
    print(f"AMI with ID {created_ami_id} created successfully.")

    # Create new version of launch template
    new_version = create_launch_template_version(launch_template_name, created_ami_id)
    print(f"New version {new_version} of launch template created successfully.")

    # Update autoscaling group capacity
    update_auto_scaling_capacity(auto_scaling_group_name, desired_capacity)
    print(f"Autoscaling group capacity updated to {desired_capacity}.")


# Uncomment the following line if you want to test the Lambda function locally
# lambda_handler(None, None)
