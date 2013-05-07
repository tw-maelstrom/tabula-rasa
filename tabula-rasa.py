import csv
import iam

from iam import *
f = open('tabula-rasa.log', 'w')


keys = csv.reader(open("accounts.csv", "rb"))

for access_key, secret_key in keys:
	iam_main(access_key, secret_key);
	