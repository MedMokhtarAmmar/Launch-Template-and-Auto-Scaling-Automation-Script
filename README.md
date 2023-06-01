# Launch-Template-and-Auto-Scaling-Automation-Script
# AMI Automation Script

This script automates the process of creating an Amazon Machine Image (AMI), updating a launch template, and updating the desired capacity of an auto scaling group.

## Prerequisites

- Python 3.x
- AWS SDK for Python (Boto3) installed
- AWS credentials configured with appropriate permissions

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies by running the following command:

   ```shell
   pip install boto3
Configuration
Before running the script, you need to update the following variables in the lambda_handler function:

instance_id: The ID of the EC2 instance from which the AMI will be created.
launch_template_name: The name of the launch template to update.
auto_scaling_group_name: The name of the auto scaling group to update.
desired_capacity: The desired capacity for the auto scaling group.
Usage
Open a terminal or command prompt.

Navigate to the directory where the script is located.

Run the script using the following command:

shell
Copy code
python script.py
Testing
To test the script locally, you can uncomment the last line in the lambda_handler function:

python
Copy code
lambda_handler(None, None)
This will simulate the execution of the script locally and test the functionality.

License
This script is licensed under the MIT License.

css
Copy code

You can modify the content as needed, and feel free to include any additional information relevant to testing the script.
