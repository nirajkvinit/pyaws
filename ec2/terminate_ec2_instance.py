import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.resource('ec2')
for instance_id in sys.argv[1:]:
    instance = ec2.Instance(instance_id)
    try:
        response = instance.terminate()
        print response
    except ClientError as e:
        print "This operation is not permitted. Find the error description below:"
        print e
    except Exception as e:
        print "Instance could not be terminated. Error occured: "
        print e
