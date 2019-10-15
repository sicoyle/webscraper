#This code reads an html file and parses out relevant information for txst faculty
import sys
import re

##############################################################################
#				Regular Expressions			     #
##############################################################################
regexName = '(Mrs|Mr|Dr)\.\s[A-Z]\w*[\s-]+[A-Z]\w*'
regexEducation = 'Education</h3>\s+.+\s+.+<p>((.+?))</p>'
regexResearchInterests = 'Research Interests</h3>\s+.+\s+.+<p>((.+?))</p>'
regexEmail = 'user=([a-zA-Z0-9_]*)'
regexWebpage = 'https?:\/\/[www.]*cs.txstate.edu\/~[a-zA-Z0-9_]*'


##############################################################################
#				HTML File #1				     #
##############################################################################

#Open input/output files
fr = open("input1.html", 'r')
page = fr.read()
fr.close()

#Parse for relevant information
name = re.search(regexName, page)
education = re.search(regexEducation, page)
researchInterests = re.search(regexResearchInterests, page)
email = re.search(regexEmail, page)
webpage = re.search(regexWebpage, page)

#Print information to text file
fw = open("output1.txt", 'w')

if not name:
	fw.write('Name: N/A\n')
else:
	fw.write('Name: ' + name.group(0) + '\n')

if not education:
	fw.write('Education: N/A\n')
else:
	fw.write('Education: ' + education.group(1) + '\n')

if not researchInterests:
	fw.write('Research Interests: N\A\n')
else:
	fw.write('Research Interests: ' + researchInterests.group(1) + '\n')

if not email:
	fw.write('Email: N/A\n')
else:
	fw.write('Email: ' + email.group(1) + '@txstate.edu' + '\n')

if not webpage:
	fw.write('Webpage: N/A\n\n')
else:
	fw.write('Webpage: ' + webpage.group(0) + '\n\n')

#Close files
fw.close()



##############################################################################
#				HTML File #2				     #
##############################################################################

#Open input/output files
fr = open("input2.html", 'r')
page = fr.read()
fr.close()

#Parse for relevant information
name = re.search(regexName, page)
education = re.search(regexEducation, page)
researchInterests = re.search(regexResearchInterests, page)
email = re.search(regexEmail, page)
webpage = re.search(regexWebpage, page)

#Print information to text file
fw = open("output2.txt", 'w')

if not name:
	fw.write('Name: N/A\n')
else:
	fw.write('Name: ' + name.group(0) + '\n')

if not education:
	fw.write('Education: N/A\n')
else:
	fw.write('Education: ' + education.group(1) + '\n')

if not researchInterests:
	fw.write('Research Interests: N\A\n')
else:
	fw.write('Research Interests: ' + researchInterests.group(1) + '\n')

if not email:
	fw.write('Email: N/A\n')
else:
	fw.write('Email: ' + email.group(1) + '@txstate.edu' + '\n')

if not webpage:
	fw.write('Webpage: N/A\n\n')
else:
	fw.write('Webpage: ' + webpage.group(0) + '\n\n')

#Close files
fw.close()


##############################################################################
#				HTML File #3				     #
##############################################################################

#Open input/output files
fr = open("input3.html", 'r')
page = fr.read()
fr.close()

#Parse for relevant information
name = re.search(regexName, page)
education = re.search(regexEducation, page)
researchInterests = re.search(regexResearchInterests, page)
email = re.search(regexEmail, page)
webpage = re.search(regexWebpage, page)

#Print information to text file
fw = open("output3.txt", 'w')

if not name:
	fw.write('Name: N/A\n')
else:
	fw.write('Name: ' + name.group(0) + '\n')

if not education:
	fw.write('Education: N/A\n')
else:
	fw.write('Education: ' + education.group(1) + '\n')

if not researchInterests:
	fw.write('Research Interests: N\A\n')
else:
	fw.write('Research Interests: ' + researchInterests.group(1) + '\n')

if not email:
	fw.write('Email: N/A\n')
else:
	fw.write('Email: ' + email.group(1) + '@txstate.edu' + '\n')

if not webpage:
	fw.write('Webpage: N/A\n\n')
else:
	fw.write('Webpage: ' + webpage.group(0) + '\n\n')

#Close files
fw.close()
