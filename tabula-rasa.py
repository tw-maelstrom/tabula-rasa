import csv

from iam import *
from cfn import *
from ec2 import *

regions = ['us-east-1', 'us-west-2', 'us-west-1', 'eu-west-1', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'sa-east-1']

account_keys = csv.reader(open("accounts.csv", "rb"))

for access_key, secret_key in account_keys:
	iam_main(access_key, secret_key);
	cfn_main(access_key, secret_key);
	for region in regions:
		print ("Starting EC2 for " + region)
		ec2_main(region, access_key, secret_key);
		print ("Finished EC2 for " + region)
