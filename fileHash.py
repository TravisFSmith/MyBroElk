()#!/usr/bin/env python

import re

def writeYAML():
	yamlFileMD5 = open('/etc/logstash/conf.d/badMD5.yaml','w')
	yamlFileSHA1 = open('/etc/logstash/conf.d/badSHA1.yaml','w')
	hashFile = open('/etc/logstash/conf.d/NSRLFile.txt','r')
	count=0
	for line in hashFile:
		if not line.startswith("\"SHA-1"):
			line = re.sub('\\r|\\n','',line)
			sha1 = re.sub(',\".*', '', line)
			#print(sha1)
			yamlFileSHA1.write(sha1 + ": \"YES\"\n")
			md5 = re.sub('\"[\w\d]{40}\",', '', line)
			md5 = re.sub(',.*', '', md5)
			yamlFileMD5.write(md5 + ": \"YES\"\n")
			#print(md5)
			count=count+1
	yamlFileMD5.close()
	yamlFileSHA1.close()

if __name__=="__main__":
	writeYAML()
