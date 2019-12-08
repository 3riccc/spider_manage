import os
import pickle as pk
import time


DATABASE_FOLDER_PATH = './spider_database/'
SPIDER_STATUS_DATABASE = './spider_status_database.pkl'
MANAGE_RECORD_DATABASE = './manage_record_database.pkl'

DFP = DATABASE_FOLDER_PATH
SSD = SPIDER_STATUS_DATABASE
MRD = MANAGE_RECORD_DATABASE


# a greate info should include content id, content result and so on
def spider_status_record(info='nothing to record'):
	database= SSD
	# add time to the info
	t = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
	info = t+'|'+info
	# if folder dont exist
	if not os.path.exists(DFP):
		os.makedirs(DFP)

	# if file dont exist then create
	if not os.path.exists(DFP+database):
		all_info = []
	else:
		with open(DFP+database,'rb') as f:
			all_info = pk.load(f)
		all_info.append(info)
	# save all info
	with open(DFP+database,'wb') as f:
		pk.dump(all_info,f)		
		return 1


# show spider info to [people], means just print the info
def spider_status_show(read_all=False):
	database=SSD
	# if file dont exist
	if not os.path.exists(DFP+database):
		raise NameError('\n\nno recoder file exists, the spider has not run yet')
	with open(DFP+database,'rb') as f:
		all_info = pk.load(f)

	# print the info
	print('Info num:'+str(len(all_info)))
	if len(all_info) > 100 and read_all == False:
		# just print last 100
		print('Info num > 100, we just print last 100 info:')
		print('for all info, please call this function with parameter read_all=True')
		for i in range(100,0,-1):
			print(all_info[-i])
	else:
		for i in range(len(all_info)):
			print(all_info[i])


# read spider info to [mechine], and we will use these info to do something
def spider_status_read():
	database=SSD
	# if file dont exist
	if not os.path.exists(DFP+database):
		raise NameError('\n\nno recoder file exists, the spider has not run yet')
	with open(DFP+database,'rb') as f:
		all_info = pk.load(f)
	return all_info

# run command to the spider
# cmd: just cmd to run
# explain: why you run this cmd
def spider_cmd(cmd = 'ls',explain='no explain'):
	print('Cmd is running:')
	print(cmd)
	os.system(cmd)
	manage_record(cmd=cmd,explain=explain)
	print('cmd has run over')

# once manage something, then record that
def manage_record(cmd='ls',explain='no explain',database = MRD):
	# add time to the info
	t = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
	info = 'time:'+t+'\ncmd:'+cmd+'\nexplain:'+explain

	# if folder dont exist
	if not os.path.exists(DFP):
		os.makedirs(DFP)

	# if file dont exist then create
	if not os.path.exists(DFP+database):
		all_info = []
	else:
		with open(DFP+database,'rb') as f:
			all_info = pk.load(f)
	all_info.append(info)
	# save all info
	with open(DFP+database,'wb') as f:
		pk.dump(all_info,f)		
		return 1


# show manage record to [people], means just print them out
def manage_status_show(read_all=False):
	database=MRD
	# if file dont exist
	if not os.path.exists(DFP+database):
		raise NameError('\n\nno recoder file exists, the manager has not run yet')
	with open(DFP+database,'rb') as f:
		all_info = pk.load(f)

	# print the info
	print('Info num:'+str(len(all_info)))
	if len(all_info) > 100 and read_all == False:
		# just print last 100
		print('Info num > 100, we just print last 100 info:')
		print('for all info, please call this function with parameter read_all=True')
		for i in range(100,0,-1):
			print(all_info[-i])
			print('\n')
	else:
		for i in range(len(all_info)):
			print(all_info[i])
			print('\n')

# clear all record
# dont use it easily, because it needs you to confirm
def clear_all_record():
	print('prepare to run the following command:')
	cmd1 = 'rm -rf '+DFP+SSD
	cmd2 = 'rm -rf '+DFP+MRD
	print(cmd1)
	print(cmd2)
	inp = raw_input('Please input "confirm" to delete them all\n')
	if inp == 'confirm':
		# print(1)
		os.system(cmd1)
		os.system(cmd2)
		print('all record has been deleted')
	else:
		print('delete canceled')