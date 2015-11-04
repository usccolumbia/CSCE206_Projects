"""
Web crawler of class schedule from university of illinois

University of South Carolina 
CSCE206  Scientific Application Programming
Spring 2015  Final project
Created on Thu Apr 23 12:12:08 2015

Installation:  
You need to install beautifulsoup4 package to run this code
on linux:  pip install beautifulsoup4
"""

from bs4 import BeautifulSoup
import urllib2
import os
import sys
import requests
import argparse
import subprocess



parser = argparse.ArgumentParser()
parser.add_argument('-y', action='store', dest='year',default=2014, help='year of the semester')
parser.add_argument('-t', action='store', dest='semester',default="Fall", help='semester')                            
parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

count=0
year=str(args.year)
semester=args.semester
numOfSections = 0

f = open("schedule_illinois_" + year + "_" + semester +".csv", "w")
f.write("Year, Term, Subject, CourseNo, Name, Section, Category, Days, WeekFreq, StartWeek, Time, Location, Instructor, Credits, MaxSeat, OpenSeat, Session, Email, EndWeek\n")

url = "https://courses.illinois.edu/schedule/" + year +"/" + semester.lower()
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

aTagList = soup.find_all('a')

for tag in aTagList:
	if "/schedule/" +year +"/" + semester.lower() in tag.get('href'):
		url = "https://courses.illinois.edu" + tag.get('href')
		r  = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data)

		temp = soup.find_all('a')
		linksToCourse =[]
		for item in temp:
			if "/schedule/" +year +"/" + semester.lower() +"/" in item.get('href') and "pdf" not in item.get('href'):
				linksToCourse.append("https://courses.illinois.edu" + item.get('href'))
				url = "https://courses.illinois.edu" + item.get('href')
				r  = requests.get(url)
				data = r.text
				soup = BeautifulSoup(data)
				# print url

				pTageList = soup.find_all('p')
				s = soup.find("script" ,  {'type':'text/javascript'})
				subjectAndNum = soup.find("h1" ,  {'class':'app-inline'}).getText()
				title = soup.find("span" ,  {'class':'app-label app-text-engage'}).getText()

				subject = subjectAndNum.split(' ',1)[0]
				courseNumber = subjectAndNum.split(' ',1)[1]
				
				times = str(s).split('time":"<span class=\\"hide\\">')
				daysList = str(s).split('"day":"<div class=\\"app-meeting\\">') 
				sections = str(s).split('"section":"<div class=\\"app-meeting\\">')
				locations = str(s).split('"location":"<div class=\\"app-meeting\\">') 
				teachers = str(s).split('"instructor":"<div class=\\"app-meeting\\">') 

				times.pop(0)
				sections.pop(0)
				teachers.pop(0)
				daysList.pop(0)
				locations.pop(0)

				credit = pTageList[0].getText().replace('Credit:','').replace(' OR ','-').replace(' TO ','-').replace('hours.','').replace(' ','')

				for i,txt in enumerate(times):
					f.write(
						year + ',' 
						+ semester +',' 
						+ subject.replace("," , ";") +','
						+ courseNumber.replace("," , ";") + ',' 
						+ title.replace("," , ";") + ',' 
						+ sections[i].split("<",1)[0].replace("," , ";") + ','
						+ 'undergraduate'+','
						+ daysList[i].split("<",1)[0].replace("," , ";").replace("n.a","") + ','
						+'1' + ','
						+'1' + ','
						+ times[i].split("<",3)[2].split('app-meeting\\">',1)[1].replace("ARRANGED","") + ',' 
						+ locations[i].split("<",1)[0].replace("," , ';').replace("n.a","TBA") + ','
						+ teachers[i].split("<",1)[0].strip().replace("," , ';') + ','
						+ credit + ','
						+ '0,'
						+ '0,'
						+'Full semester,' 
						+ ' ,'
						+ '\n'
					)
					f.flush()
					numOfSections = numOfSections + 1 
					print "Courses processed: " , numOfSections
