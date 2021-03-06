import re
import pandas as pd
from matplotlib import pyplot as plt
import html


class SignalMessageProcessor():
	"""
		I needed to parse the XML file generated by the signal (formerly textsecure)
		app and was having waaay too much trouble than it was worth to get the built-in (?)
		python xml parser to do it for me
	"""
	def readFile(self, filename):
		with open(filename, 'r') as file:
			self.xml = file.readlines()

	def parseXML(self):
		self.xml = self.xml[3:-1]; #remove first 3 lines and last line

		self.messages = [];

		for i in self.xml:
			d = {}
			props=re.findall('[^ \"]*=\"[^\"]*\"', i)
			for prop in props:
				temp = prop.split("=");
				d[temp[0]] = temp[1][1:-1]
			self.messages.append(d);

def analysis(SMP):
	pass

def main():
	SMP = SignalMessageProcessor();
	SMP.readFile('second.xml');
	SMP.parseXML();
	analysis(SMP)

if __name__ == '__main__':
	main();
