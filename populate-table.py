import argparse
import json
import time

import boto3


parser = argparse.ArgumentParser()
parser.add_argument("key", help="AWS_ACCESS_KEY_ID")
parser.add_argument("secret", help="AWS_SECRET_ACCESS_KEY")
parser.add_argument("region", help="aws region")

args = parser.parse_args()

session = boto3.Session(
    aws_access_key_id=args.key,
    aws_secret_access_key=args.secret,
    region_name=args.region,
)
dynamodb = session.resource("dynamodb", region_name=args.region)

time.sleep(5)

table_1 = dynamodb.Table("blog-users")
db_file_json_1 = open("blog-users.json")
db_file_1 = json.loads(db_file_json_1.read())
for db_item_1 in db_file_1:
    table_1.put_item(Item=db_item_1)

table_2 = dynamodb.Table("blog-posts")
db_file_json_2 = open("blog-posts.json")
db_file_2 = json.loads(db_file_json_2.read())
for db_item_2 in db_file_2:
    table_2.put_item(Item=db_item_2)

print("Items Updated")
