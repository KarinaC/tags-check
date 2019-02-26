# /usr/bin/python3
import boto3

## Variables
ids = []
mandatory_tags = ["eo:user:department", "eo:user:team", "eo:user:contact", "eo:ops:tier", "eo:ops:environment", "eo:ops:application"]
tdata = []

## Script
session = boto3.Session(region_name='us-west-1',profile_name='upwork')
ec2_client = session.client('ec2')
response = ec2_client.describe_instances(
    Filters=[
        {
            'Name':'instance-state-name',
            'Values':[
                'running',
                'stopped',
            ]
        },
    ]
)

flag=0
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This will print will output the value of the Dictionary key 'InstanceId'
        print("\n")
        # print(instance["InstanceId"])
        try:
            #print("######################")
            print("- "+instance["InstanceId"]+" -")
            #print("######################")
            for y in mandatory_tags:
                for tags in instance["Tags"]: 
                    if y == tags["Key"]:
                       flag=1
                if flag == 0:
                    print ("Field does not exist "+str(y))
                flag=0

                    #tdata = tags["Key"]
                    #print("KEY:   " + tags["Key"])
                    #print("VALUE: " + tags["Value"])
                    #print(tdata)
            
                
        except KeyError:
             print("THIS INSTANCE HAS NO TAGS!!!!")
             print(instance["InstanceId"])
             pass

           #  tdata = []

        




            


