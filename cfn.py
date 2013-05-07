import boto

#functions

#delete CFN stacks
def cfn_delete(cfn):
	stacks = cfn.describe_stacks()
	for s in stacks:
		try:
			cfn.delete_stack(s.stack_name)
		except Exception, e:
			print(e)

#main function called by tabula-rasa.py
def cfn_main(access_key, secret_key):
	cfn = boto.connect_cloudformation(access_key, secret_key)
	
	cfn_delete(cfn);
	