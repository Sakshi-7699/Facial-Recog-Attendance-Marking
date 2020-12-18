import numpy as np
from matplotlib import pyplot as plt
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import time




def graph(a):
	
	none=[]
	name=[]
	rollno=[]
	mob=[]
	email=[]
	gender=[]
	hostelite=[]
	
	ut1dbms=[]
	ut1sepm=[]
	ut1cn=[]
	ut1isee=[]
	ut1toc=[]
	
	
	ut2dbms=[]
	ut2sepm=[]
	ut2cn=[]
	ut2isee=[]
	ut2toc=[]
	with open('result.csv','r') as csvfile:
		plots=csv.reader(csvfile,delimiter=',')
		for row in plots:
			none.append(row[0])
			name.append(row[1])
			rollno.append(row[2])
			mob.append(row[3])
			email.append(row[4])
			gender.append(row[5])
			hostelite.append(row[6])
			
			ut1dbms.append(row[7])
			ut1sepm.append(row[8])
			ut1cn.append(row[9])
			ut1isee.append(row[10])
			ut1toc.append(row[11])
			
			ut2dbms.append(row[12])
			ut2sepm.append(row[13])
			ut2cn.append(row[14])
			ut2isee.append(row[15])
			ut2toc.append(row[16])
			
			
	
	
	if a=="DBMS":
		x=ut1dbms
		y=ut2dbms
	elif a=="SEPM":
		x=ut1sepm
		y=ut2sepm
	elif a=="CN":
		x=ut1cn
		y=ut2cn
	elif a=="TOC":
		x=ut1toc
		y=ut2toc
	elif a=="ISEE":
		x=ut1isee
		y=ut2isee
	 
	w=0.3
	plt.ion()
	index=np.arange(len(name))
	plt.scatter(rollno,x,label="UNIT TEST MARKS 1",color="blue",marker="*",s=150)
	plt.scatter(rollno,y,label="UNIT TEST MARKS 2",color="red",marker="*",s=150)
	minut1dbms=min(ut1dbms)
	minut1toc=min(ut1toc)
	minut1isee=min(ut1isee)
	minut1cn=min(ut1cn)
	minut1sepm=min(ut1sepm)
	minut2dbms=min(ut2dbms)
	plt.show()
	'''
	time.sleep(5)
	plt.close("all")
	'''	
#graph("TOC")		
		
def pie_chart (self) :
	none=[]
	name=[]
	rollno=[]
	mob=[]
	email=[]
	gender=[]
	hostelite=[]
	
	ut1dbms=[]
	ut1sepm=[]
	ut1cn=[]
	ut1isee=[]
	ut1toc=[]
	
	
	ut2dbms=[]
	ut2sepm=[]
	ut2cn=[]
	ut2isee=[]
	ut2toc=[]
	with open('result.csv','r') as csvfile:
		plots=csv.reader(csvfile,delimiter=',')
		for row in plots:
			none.append(row[0])
			name.append(row[1])
			rollno.append(row[2])
			mob.append(row[3])
			email.append(row[4])
			gender.append(row[5])
			hostelite.append(row[6])
			
			ut1dbms.append(row[7])
			ut1sepm.append(row[8])
			ut1cn.append(row[9])
			ut1isee.append(row[10])
			ut1toc.append(row[11])
			
			ut2dbms.append(row[12])
			ut2sepm.append(row[13])
			ut2cn.append(row[14])
			ut2isee.append(row[15])
			ut2toc.append(row[16])
	count_male=0
	count_female=0
	
	for i in gender :
		if i=="male": count_male+=1
		else : count_female+=1
		
	slices=[count_male,count_female]
	color = ['cyan', 'pink']#, 'g', 'b']	
	l=['male','female']
	plt.pie(slices,labels=l,colors=color,startangle=90,autopct='%.1f%%', shadow = True)
	plt.title("GENDER DISTRIBUTION")
	plt.legend() 
	plt.show()
	
def host (self) :
	none=[]
	name=[]
	rollno=[]
	mob=[]
	email=[]
	gender=[]
	hostelite=[]
	
	ut1dbms=[]
	ut1sepm=[]
	ut1cn=[]
	ut1isee=[]
	ut1toc=[]
	
	
	ut2dbms=[]
	ut2sepm=[]
	ut2cn=[]
	ut2isee=[]
	ut2toc=[]
	with open('result.csv','r') as csvfile:
		plots=csv.reader(csvfile,delimiter=',')
		for row in plots:
			none.append(row[0])
			name.append(row[1])
			rollno.append(row[2])
			mob.append(row[3])
			email.append(row[4])
			gender.append(row[5])
			hostelite.append(row[6])
			
			ut1dbms.append(row[7])
			ut1sepm.append(row[8])
			ut1cn.append(row[9])
			ut1isee.append(row[10])
			ut1toc.append(row[11])
			
			ut2dbms.append(row[12])
			ut2sepm.append(row[13])
			ut2cn.append(row[14])
			ut2isee.append(row[15])
			ut2toc.append(row[16])
	count_yes=0
	count_no=0
	
	for i in hostelite :
		if i=="yes": count_yes+=1
		else : count_no+=1
		
	slices=[count_yes,count_no]
	color = ['blue', 'green']#, 'g', 'b']	
	l=['hostelite','not hostelite']
	plt.pie(slices,labels=l,colors=color,startangle=90,autopct='%.1f%%', shadow = True)
	plt.title("HOSTELITE STATUS ")
	plt.legend() 
	plt.show()
