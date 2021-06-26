import os ,sys
import time

os.system("aws ec2 create-key-pair --key key")
print("Key Created ")

os.system("aws ec2 create-security-group --group-name S --vpc-id vpc-c44f82af --description security_created --output text > sg.txt")
print("Security Group Created ")
time.sleep(5)
sg_id = open("sg.txt", 'r').read()

print(sg_id)

os.system("aws ec2 authorize-security-group-ingress  --protocol tcp  --port 22  --cidr 0.0.0.0/0 --group-id "+sg_id )
print("Port 22 allowed")

os.system("aws ec2 run-instances --image-id ami-0ad704c126371a549  --instance-type t2.micro --count 1  --subnet-id subnet-5e540f12  --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value=Instance2}]    --key-name key  --security-group-ids "+sg_id)
time.sleep(10)
print("Instance Launched")

os.system("aws ec2 describe-instances  --filters Name=instance-type,Values=t2.micro Name=tag:Name,Values=Instance2  --query Reservations[*].Instances[*].[InstanceId] --output text > instance.txt")
instance_id = open("instance.txt", 'r').read()
instance_id = instance_id[0:len(instance_id)-1]
print(instance_id)


os.system("aws ec2 create-volume --volume-type gp2  --availability-zone ap-south-1b --size 5  --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=Volume3}]")
print("Volume Created")
time.sleep(10)

os.system("aws ec2 describe-volumes   --filters Name=status,Values=available Name=availability-zone,Values=ap-south-1b  Name=tag:Name,Values=Volume3   --query Volumes[*].[VolumeId] --output text > volume.txt")
volume_id = open("volume.txt", 'r').read()
volume_id = volume_id[0:len(volume_id)-1]
print(volume_id)



os.popen('aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/xvdf'.format(volume_id, instance_id))


print("Volume Successfully Attached !!")


'''
===========================================================================================================================================================================================
#AWS TASK
def aws():
    #LANUNCHING AN INSTANCE
    os.popen("aws ec2 run-instances --image-id ami-0ad704c126371a549 --count 1 --instance-type t2.micro --key-name ARTH_KEY --subnet-id subnet-c2656caa --security-group-ids sg-dd5a8eba --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value=SUMMER_INTERN}]")
    print("AWS instance launched!!!\n")
    time.sleep(15)
    
    #CREATING A 5GB VEBS VOLUME
    os.popen("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size 5 --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=SUMMER_INTERN}]")
    print("AWS volume of 5GB created!!!\n")
    time.sleep(15)
    
    #QUERY FOR CREATED VOLUME_ID
    volume_id = os.popen('aws ec2 describe-volumes --filters Name=status,Values=available Name=availability-zone,Values=ap-south-1a --query Volumes[*].VolumeId --output text').read()
    volume_id = volume_id[0:len(volume_id)-1]
    print("The volume id of 5 GB EBS volume: ",volume_id)
    time.sleep(15)
    
    #QUERY FOR RUNNING INSTANCE_ID
    instance_id = os.popen('aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query "Reservations[*].Instances[*].InstanceId" --output text').read()
    instance_id = instance_id[0:len(instance_id)-1]
    print("The current running instance id: ", instance_id)
    time.sleep(15)
    
    #ATTACHING THE 5 GB OF VOLUME TO THE INSTANCE
    os.popen('aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf'.format(volume_id, instance_id))
    
    print("TASK 6 DONE!!!")

'''









