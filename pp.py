import numpy as np
from matplotlib import pyplot as plt
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *



def graph(a,b):
	
	rollno=[]
	name=[]
	sdl=[]
	dbms=[]
	sepm=[]
	cn=[]
	isee=[]
	toc=[]
	none=[]
	with open('attendance.csv','r') as csvfile:
		plots=csv.reader(csvfile,delimiter=',')
		for row in plots:
			none.append(row[0])
			rollno.append(row[1])
			name.append(row[2])
			sdl.append(row[3])
			dbms.append(row[4])
			sepm.append(row[5])
			cn.append(row[6])
			isee.append(row[7])
			toc.append(row[8])
	rollno.pop(0)
	sdl.pop(0)
	isee.pop(0)
	dbms.pop(0)
	sepm.pop(0)
	cn.pop(0)
	toc.pop(0)
	
	for i in range(0,len(rollno)):
		sdl[i]=float(sdl[i])
		sepm[i]=float(sepm[i])
		isee[i]=float(isee[i])
		cn[i]=float(cn[i])
		dbms[i]=float(dbms[i])
		toc[i]=float(toc[i])
	
	
	try:
		if (a=="SDL" and b=="SEPM") or (a=="SEPM" and b=="SDL") :
			x=sdl
			y=sepm
		elif (a=="SDL" and b=="TOC") or (a=="TOC" and b=="SDL") :
			x=sdl
			y=toc
		elif (a=="SDL" and b=="ISEE") or (a=="ISEE" and b=="SDL") :
			x=sdl
			y=isee
		elif (a=="SDL" and b=="CN") or (a=="CN" and b=="SDL") :
			x=sdl
			y=cn
		elif (a=="SDL" and b=="DBMS") or (a=="DBMS" and b=="SDL") :
			x=sdl
			y=dbms
			
			
		elif (a=="DBMS" and b=="SEPM") or (a=="SEPM" and b=="DBMS") :
			x=dbms
			y=sepm
		elif (a=="DBMS" and b=="ISEE") or (a=="ISEE" and b=="DBMS") :
			x=dbms
			y=isee
		elif (a=="DBMS" and b=="CN") or (a=="CN" and b=="DBMS") :
			x=dbms
			y=cn
		elif (a=="DBMS" and b=="TOC") or (a=="TOC" and b=="DBMS") :
			x=dbms
			y=toc
			
			
		elif (a=="SEPM" and b=="ISEE") or (a=="ISEE" and b=="SEPM") :
			x=isee
			y=sepm
		elif (a=="SEPM" and b=="CN") or (a=="CN" and b=="SEPM") :
			x=cn
			y=sepm
		elif (a=="SEPM" and b=="TOC") or (a=="TOC" and b=="SEPM") :
			x=toc
			y=sepm
			
			
		elif (a=="ISEE" and b=="TOC") or (a=="TOC" and b=="ISEE") :
			x=toc
			y=isee
		elif (a=="ISEE" and b=="CN") or (a=="CN" and b=="ISEE") :
			x=cn
			y=isee
			
		elif (a=="TOC" and b=="CN") or (a=="CN" and b=="TOC") :
			x=toc
			y=cn
		w=0.3
		index=np.arange(len(rollno))
		
		
		plt.bar(index,y,width=w,color='cyan',label=a)
		plt.bar(index+w,x,width=w ,color='magenta',label=b)
		plt.xticks(index, rollno)
		plt.xlabel("ROLL NO.")
		plt.ylabel("ATTENDANCE")
		plt.title("SUBJECT WISE ATTENDANCE ANALYSIS OF EVERY STUDENT ")
		plt.legend()
		
		plt.show()
	except Exception:
		QMessageBox.warning(QMessageBox(), 'ERROR', 'SAME SUBJECT ANALYSIS NOT ALLOWED.')
		
def defaulter (a):
	rollno=[]
	name=[]
	sdl=[]
	dbms=[]
	sepm=[]
	cn=[]
	isee=[]
	toc=[]
	none=[]
	with open('attendance.csv','r') as csvfile:
		plots=csv.reader(csvfile,delimiter=',')
		for row in plots:
			none.append(row[0])
			rollno.append(row[1])
			name.append(row[2])
			sdl.append(row[3])
			dbms.append(row[4])
			sepm.append(row[5])
			cn.append(row[6])
			isee.append(row[7])
			toc.append(row[8])
	rollno.pop(0)
	j=0
	for i in rollno :
		rollno[j]=int(i)
		j+=1
	
	default=[]
	nd=[]
	w=0.3
	index=np.arange(len(rollno))
	np.delete(a,0)
	
	if a=="SDL":
		sdl.pop(0)
		for i in range(0,len(sdl)) :
			if float(sdl[i])<15 :
				default.append(i+1)
			else :
				nd.append(i)
	
	elif a=="DBMS":
		dbms.pop(0)
		for i in range(0,len(dbms)) :
			if float(dbms[i])<15 :
				default.append(i+1)
			else :
				nd.append(i+1)
	elif a=="CN":
		cn.pop(0)
		for i in range(0,len(cn)) :
			if float(cn[i])<15 :
				default.append(i+1)
			else :
				nd.append(i)
			
	elif a=="TOC":
		toc.pop(0)
		for i in range(0,len(toc)) :
			if float(toc[i])<15 :
				default.append(i+1)
			else :
				nd.append(i)
	elif a=="SEPM":
		sepm.pop(0)
		for i in range(0,len(sepm)) :
			if float(sepm[i])<15 :
				default.append(i+1)
			else :
				nd.append(i)
	elif a=="ISEE":
		isee.pop(0)
		for i in range(0,len(isee)) :
			if float(isee[i])<15 :
				default.append(i+1)
			else :
				nd.append(i)

	serachresult=""
	final=" "
	
	for i in range(0,len(default)) : 
		serachresult = '\n'+"Rollno : "+str(default[i])+'\n'
		final=final+serachresult
	QMessageBox.information(QMessageBox(), 'DEFAULTERS', final)
	

#graph("ISEE","SDL")		
		
	
	
		
		
	
	
	 
	
	
	

