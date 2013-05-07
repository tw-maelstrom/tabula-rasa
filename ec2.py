import time
import boto.ec2


#functions

def ec2_terminate(ec2):
	#filters = {'instance-state-name' : 'running'}
	reservations = ec2.get_all_instances()
	instances = [i for r in reservations for i in r.instances]
	for i in instances:
		try:
			print "---Terminating instance: " + i.id
			ec2.terminate_instances(instance_ids=i.id)
		except Exception, e:
			print(e)
			
def ec2_delete_keys(ec2):
	key = ec2.get_all_key_pairs()
	for k in key:
		try:
			print "---Deleting key: " + k.name
			ec2.delete_key_pair(k.name)
		except Exception, e:
			print(e)

def ec2_deregister_ami(ec2):
	images = ec2.get_all_images(owners="self")
	for i in images:
		try:
			print "---Deregistering AMI: " + i.id
			ec2.deregister_image(i.id, delete_snapshot=True)
		except Exception, e:
			print(e)
			
def ec2_release_eip(ec2):
	addresses = ec2.get_all_addresses()
	for a in addresses:
		try:
			if a.domain == 'standard': 
				print "---Releasing EIP: " + a.public_ip
				ec2.release_address(public_ip=a.public_ip)
			elif a.domain == 'vpc':
				print "---Releasing EIP: " + a.public_ip
				ec2.release_address(allocation_id=a.allocation_id) 
		except Exception, e:
			print(e)
			
def ec2_delete_volume(ec2):
	volumes = ec2.get_all_volumes()
	for v in volumes:
		try:
			if v.status == 'available': 
				print "---Deleting Volume: " + v.id
				ec2.delete_volume(v.id)
		except Exception, e:
			print(e)

#main function called by tabula-rasa.py
def ec2_main(region, access_key, secret_key):
	ec2 = boto.ec2.connect_to_region(region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
	
	ec2_terminate(ec2);
	time.sleep(30)
	ec2_delete_keys(ec2);
	ec2_deregister_ami(ec2);
	ec2_release_eip(ec2);
	ec2_delete_volume(ec2);