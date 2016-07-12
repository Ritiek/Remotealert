#!/usr/bin/python

import sys
import json
import os
import urllib, urllib2

if len(sys.argv) <= 2:
	print("Usage: sudo python Remotealert.py <any unique RemoteAlert ID or simply device name> <'message'>")
	exit()

if sys.argv[1] == "device1":
	ID = "device1_id"
elif sys.argv[1] == "device2":
	ID = "device2_id"
elif sys.argv[1] == "device3":
	ID = "device3_id"
elif sys.argv[1] == "device4":
	ID = "device4_id"
elif sys.argv[1] == "device5":
	ID = "device5_id"
#elif ....
#	ID = ...
elif len(sys.argv[1]) == 36:
	ID = sys.argv[1]
else:
	print("Please use a valid device ID or name argument!")
	exit()

Message = sys.argv[2]

class RemoteAlert:
    def send(self, device_id, message ):
        data = { 'message' : message }
        url = 'http://remote-alert.herokuapp.com/post/' + device_id
        req = urllib2.Request( url )
        req.add_header('Content-Type', 'application/json')
        urllib2.urlopen(req, json.dumps(data))
        return 'Sending Remotealert to ' + ID + ' with the Message : ' + Message + '.'
	 
ra = RemoteAlert()

print ra.send(ID, Message)
