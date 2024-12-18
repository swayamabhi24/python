#BOTO3-AWS S3 Bucket
""" 1. boto3 cli install
2.IAM user Configuration
3.python install 

#pip install aswcli
 #configure IAM user:
IAM > adduser - test-user 
            --programatic access ,not console access
            -- add a group ,if you dont have create -adminstractive access
            -- avoid optional field >next>next> create

cmd>aws configure
  add -aceesskey,secretekey,zone,and tyype to cli
#pip install boto3

##create a s3 bucket:
import boto3
client_s3= boto3.client('s3')
response = client_s3.create_bucket(
    ACL='private',
    Bucket='my-first-s3-7978',

)
print(response)

{
'ResponseMetadata': {
                     'RequestId': 'HPTWX4BRDGKYA4XE',
                      'HostId': 'SvESj+dRoaPFGk0d6lIe2NrYpeZFEkBNODMHip7IMhG/gWeynalB9sxPzgJiL/RtV8w+YFmZuuljQitfSvXb1TtOthgeVhyKOQla0Kjl/A0=', 
                      'HTTPStatusCode': 200, 
                      'HTTPHeaders': {
                                      'x-amz-id-2': 'SvESj+dRoaPFGk0d6lIe2NrYpeZFEkBNODMHip7IMhG/gWeynalB9sxPzgJiL/RtV8w+YFmZuuljQitfSvXb1TtOthgeVhyKOQla0Kjl/A0=', 
                                      'x-amz-request-id': 'HPTWX4BRDGKYA4XE',
                                      'date': 'Tue, 17 Dec 2024 17:09:39 GMT', 
                                      'location': '/my-first-s3-7978',
                                      'content-length': '0',
                                      'server': 'AmazonS3'
                                      },
                     'RetryAttempts': 0
                     }, 
'Location': '/my-first-s3-7978'
}
"""
import boto3
import json
client_s3= boto3.client('s3')
 #create bucket 
""" response = client_s3.create_bucket(
    ACL='private',
    Bucket='my-first-s3-7978',

)
print(response) """
# response = client_s3.create_bucket(
#     ACL='private',
#     Bucket='my-first-s3-dest-bkt',

# )
# print(response)
#How to upload files to S3 using Python (Boto3) | AWS S3 Python API | upload_file() method

""" # "C:\Users\abhiram.sahoo\Desktop\py\bucket_details.json"
response=client_s3.upload_file(r"C:\Users\abhiram.sahoo\Desktop\py\bucket_details.json","my-first-s3-7978","data/bucket_details.json")
print(response) """

# Download a file from S3 bucket  download_file():

""" #bucket_name,resouse,download_location
response=client_s3.download_file("my-first-s3-7978","data/bucket_details.json",r'C:\Users\abhiram.sahoo\Desktop\py\boto3\bucket_details.json')
print(response) """

#Write Data to s3 put_object():
""" data={"Name":"Abhiram Sahoo","Empid":"1356067","Org":"infosys","Location":"Trivandrum"}
my_data=json.dumps(data).encode('UTF-8')
# print(type(my_data))
res=client_s3.put_object(Body=my_data,Bucket="my-first-s3-7978",Key="mydata")
print(res) """

#How to read data from S3 get_object() :
""" response=client_s3.get_object(Bucket="my-first-s3-7978",Key="mydata")
data=response["Body"].read()
json_data=json.loads(data)
print(type(json_data))
print(json_data) """

#Copy data from one s3 bucket to another s3 src.copy():
""" resource_s3=boto3.resource('s3')
copy_sourse={
    "Bucket":"my-first-s3-7978",
    "Key":"mydata"
}
dest_bucket=resource_s3.Bucket("my-first-s3-dest-bkt")
res=dest_bucket.copy(copy_sourse,"mydata.json")
print(res) """

#Delete the Object from Boto3 delete_object()
""" res=client_s3.delete_object(Bucket="my-first-s3-7978",Key="mydata")
print(res) """

#see all the files/folders in s3 bucket list_objects_v2():
""" response=client_s3.list_objects_v2(Bucket="my-first-s3-7978",Prefix="boto3")
 # print(response)
for Key in (response["Contents"]):
    print(Key) """

