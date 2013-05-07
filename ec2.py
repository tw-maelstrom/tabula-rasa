import boto.ec2

#functions

def ec2_terminate(ec2):
	#filters = {'instance-state-name' : 'running'}
	reservations = ec2.get_all_instances()
	instances = [i for r in reservations for i in r.instances]
	try:
		for i in instances:
			print "Terminating instance "
			print i.id
			ec2.terminate_instances(instance_ids=i.id)
	except Exception, e:
		print(e)

#main function called by tabula-rasa.py
def ec2_main(region, access_key, secret_key):
	ec2 = boto.ec2.connect_to_region(region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
	
	ec2_terminate(ec2);