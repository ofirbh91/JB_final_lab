import time
import boto3
import os

client = boto3.client("ec2")
ec2 = boto3.resource("ec2")

def scan_ec2():
    response = ec2.instances.all()
    for instance in response:
        if instance.state["Code"]==16:
            for t in instance.tags:
                if t["Key"]=="k8s.io/role/master" and t["Value"]=="1":
                    # print(instance.tags)
                    print("Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\nTags: {6}\n".format(
                        instance.id, instance.platform, instance.instance_type, instance.public_ip_address,
                        instance.image.id, instance.state, instance.tags))


interval = os.environ.get('Interval')
if interval == None:
    scan_ec2()
else:
    while True:
        scan_ec2()
        print("Program wait for {0} seconds.".format(interval))
        time.sleep(int(interval))


