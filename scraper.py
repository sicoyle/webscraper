#This file reads an html file and parses out relevant information on Texas State university professors

import sys
import re

#Open input/output files
fr = open("input1.html", 'r')
page = fr.read()
fw = open("output1.txt", 'w')

#Regular Expression to get information
regexName = '(Mrs|Mr|Dr)\.\s[A-Z]\w*[\s-]+[A-Z]\w*'
regexEducation = 'Education</h3>\s+.+\s+.+<p>((.+?))</p>'
regexResearchInterests = 'Research Interests</h3>\s+.+\s+.+<p>((.+?))</p>'
regexEmail = 'user=([a-zA-Z0-9_]*)'
regexWebpage = 'https?:\/\/[www.]*cs.txstate.edu\/~[a-zA-Z0-9_]*'

#Parse for relevant information
name = re.search(regexName, page)
education = re.search(regexEducation, page)
researchInterests = re.search(regexResearchInterests, page)
email = re.search(regexEmail, page)
webpage = re.search(regexWebpage, page)

#Print information to text file
if not name:
	fw.write('Name: N/A\n')
else:
	fw.write('Name: ' + name.group(0) + '\n')

if not education:
	fw.write('Education: N/A\n')
else:
	fw.write('Education: ' + education.group(1) + '\n')

if not researchInterests:
	fw.write('Research Interests: N/A\n')
else:
	fw.write('Research Interests: ' + researchInterests.group(1) + '\n')

if not email:
	fw.write('Email: N/A\n')
else:
	fw.write('Email: ' + email.group(1) + '@txstate.edu' + '\n')

if not webpage:
	fw.write('Webpage: N/A\n')
else:
	fw.write('Webpage: ' + webpage.group(0) + '\n')

#Close files
fr.close()
fw.close()
