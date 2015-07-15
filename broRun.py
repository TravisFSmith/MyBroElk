#!/usr/bin/env python

import os

if __name__=="__main__":
	for name in os.listdir("/opt/nsm/pcap/"):
		if name.endswith(".pcap"):
			os.system("bro -r " + name)
			for logfile in os.listdir("/opt/nsm/pcap/"):
				if logfile.endswith(".log"):
					logfilereader = open(logfile, 'r')
					logfilewriter = open('/opt/nsm/pcap/logs/' + logfile, 'a')
					for line in logfilereader:
						if not line.startswith("#"):
							logfilewriter.write(line)
					logfilereader.close()
					logfilewriter.close()
