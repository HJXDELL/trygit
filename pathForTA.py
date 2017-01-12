import codecs
import json
from biplist import *


#Modifly whatsNew
def modiflyWhatsNew(fname):
	try:
	 	plist = readPlist("Settings.plist");
		result = plist['BRAND_INFO']['RingCentral']
	
	except InvalidPlistException, e:
		print "Not a Plist or Plist Invalid:",e

#modifly plist
	if result['EnableWhatsNew']==True:
		result['EnableWhatsNew']=False
	
	print result['EnableWhatsNew']


	try:
		writePlist(plist,"Settings.plist")
	except (InvalidPlistException,NotBinaryPlistException), e:
		print "Something bad happened:",e



#replace pre_env XMN_LAB
def replace(fname, idx):
	with codecs.open(fname, 'r', encoding='GBK') as fp:
		data = json.load(fp)
		objs = data['data']

		for o in objs:
			if o['name'] == 'XMN-Lab':
				o['id'] = 1
			elif o['id'] == 1 and o['name'] != 'XMN_LAB':
				o['id'] = idx

		# json.dump(data, fp)

	with codecs.open(fname, 'w', encoding='GBK') as fp:
		json.dump(data, fp, indent=4)


#Run
replace('pre_env.txt', 8)
modiflyWhatsNew('Settings.plist')

