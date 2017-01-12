#!usr/bin/python
# -*- coding:utf-8 -*-
from biplist import *
import os

#srcPath=r"/Users/rcadmin/trygit/aaa/ddd/Settings.plist"
#path=os.path.abspath(srcPath)
#print path
try:
	path = os.path.abspath(os.path.join(os.path.dirname('Settings.plist'),os.path.pardir))
	print path
	plist = readPlist(path+"/trygit2/Settings.plist");
	result = plist['BRAND_INFO']['RingCentral']
	print result['EnableWhatsNew']
	
except InvalidPlistException, e:
	print "Not a Plist or Plist Invalid:",e

##修改plist
#if result['EnableWhatsNew']==True:
#	result['EnableWhatsNew']=False
#	
#print result['EnableWhatsNew']
#
#
#try:
#	writePlist(plist,"Settings.plist")
#except (InvalidPlistException,NotBinaryPlistException), e:
#	print "Something bad happened:",e