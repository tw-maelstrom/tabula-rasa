import boto

#functions

#remove group policys from all groups
def rm_group_policies(iam, groups, users):
        for g in groups.groups:
                policy = iam.get_all_group_policies(g['group_name'])
                for p in policy.list_group_policies_result.policy_names:
                        iam.delete_group_policy(g['group_name'], p)

#remove users from all groups
def rm_group_users(iam, groups, users):
        for u in users.users:
                groups = iam.get_groups_for_user(u['user_name'])
                for g in groups.list_groups_for_user_result.groups:
                        iam.remove_user_from_group(g['group_name'], u['user_name'])

#delete groups
def rm_groups(iam, groups, users):
        for g in groups.groups:
                iam.delete_group(g['group_name'])

#remove user policies
def rm_user_policies(iam, groups, users):
        for u in users.users:
                policy = iam.get_all_user_policies(u['user_name'])
                for p in policy.list_user_policies_result.policy_names:
                        iam.delete_user_policy(u['user_name'], p)

#remove user login profile
def rm_user_login_profile(iam, groups, users):
        for u in users.users:
                try:
                        iam.delete_login_profile(u['user_name'])
                except Exception, e:
                        print(e)

#remove user keys
def rm_user_keys(iam, groups, users):
        for u in users.users:
                key = iam.get_all_access_keys(u['user_name'])
                for k in key.list_access_keys_result.access_key_metadata:
                        iam.delete_access_key(k['access_key_id'], user_name=u['user_name'])
  					
#remove users
def rm_user(iam, groups, users):
        for u in users.users:
                iam.delete_user(u['user_name'])

#main function called by main.py
def iam_main(access_key, secret_key):
        iam = boto.connect_iam(access_key, secret_key)
        users = iam.get_all_users()
        groups = iam.get_all_groups()

        rm_group_policies(iam, groups, users);
        rm_group_users(iam, groups, users);
        rm_groups(iam, groups, users);
        rm_user_policies(iam, groups, users);
        rm_user_login_profile(iam, groups, users);
        rm_user_keys(iam, groups, users);
        rm_user(iam, groups, users);
