#!/usr/bin/python

import urllib
import urllib2
import sys
import re

with open(sys.argv[1], 'r') as f:
    for line in f:
        mail = re.search("(?<=<)(.*)(?=>)", line)
        data = { 'email': mail }
        data = urllib.urlencode(data)
        response = urllib2.urlopen('http://mailtester.com/testmail.php', data)
        print response.read()
'''
# print str(sys.argv[1])

# open file sys.argv[1]
f = file_object = open(sys.argv[1], "r") # read-only

#read file data
filedata = f.read()

# close file for security
f.close

# sanitize data
for line in filedata

# check each email

# save new list
'''
