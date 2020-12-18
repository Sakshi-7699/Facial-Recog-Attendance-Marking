from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtPrintSupport import *
import sys

import time
import os
from r import result
import Generating_training_data as gp
import cv2
import numpy as np
import pp as p
import result_analysis as ra
import pandas as pd
import re


d=result()
name1=""
hostelite=""



#*******************************
class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Login")
        self.setMinimumSize(1850, 1020)
        #self.showFullScreen()
        '''
        oImage = QImage("choice_2.jpg")
        sImage = oImage.scaled(QSize(500,300))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        '''
        self.setWindowIcon(QIcon('icon/user.png'))  #window icon  
        self.setStyleSheet("background-image: url(My_Post2.jpg)")      

        name=""
        verticalSpacer = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        verticalSpacer1 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.textName = QLineEdit(self)
        self.textName.setFixedWidth(300)
        self.textName.setFixedHeight(30)
        self.textName.setPlaceholderText("Username")
        self.textPass = QLineEdit(self)
        self.textPass.setFixedWidth(300)
        self.textPass.setFixedHeight(30)
        self.textPass.setPlaceholderText("Password")
        self.textPass.setEchoMode(QLineEdit.Password)
        self.textPass.setStyleSheet('lineedit-password-character: 9679')
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonLogin.setFixedHeight(30)
        self.buttonLogin.setFixedWidth(200)
        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer1)
        layout.addWidget(self.textName,alignment=Qt.AlignCenter)
        layout.addItem(verticalSpacer1)
        layout.addWidget(self.textPass,alignment=Qt.AlignCenter)
        layout.addItem(verticalSpacer)
        layout.addItem(verticalSpacer)
        layout.addWidget(self.buttonLogin,alignment=Qt.AlignCenter)
        layout.addStretch()
        #verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #layout.addItem(verticalSpacer, 6, 0, Qt.AlignBottom)
        #self.setStyleSheet("background-color: white")
        font = QFont()
        font.setPointSize(10)

    def handleLogin(self):
        if (self.textName.text() == 'sdl' and self.textPass.text() == 'sdl'):
            name=self.textName.text()
            self.accept()
        elif (self.textName.text() == 'dbms' and self.textPass.text() == 'dbms'):
            name=self.textName.text()
            self.accept()
        elif (self.textName.text() == 'sepm' and self.textPass.text() == 'sepm'):
            name=self.textName.text()
            self.accept()
        elif (self.textName.text() == 'cn' and self.textPass.text() == 'cn'):
            name=self.textName.text()
            self.accept()
        elif (self.textName.text() == 'isee' and self.textPass.text() == 'isee'):
            name=self.textName.text()
            self.accept()
        elif (self.textName.text() == 'toc' and self.textPass.text() == 'toc'):
            name=self.textName.text()
            self.accept()

        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or Password. Try again.')
		           
#*******************************

class InsertDialog(QDialog):
    
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")
        self.setStyleSheet("QLabel {font: 100pt Comic Sans MS}")
        self.QBtn1 = QPushButton()
        self.QBtn1.setText("Generate Data")    
           
        self.setWindowTitle("Add Student")
        self.setFixedWidth(800)
        self.setFixedHeight(800)

        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(800)
        self.setFixedHeight(800)

        self.QBtn.clicked.connect(self.addstudent)
        self.QBtn1.clicked.connect(self.callgen)
        layout = QVBoxLayout()
        

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)
        
        self.rnoinput = QLineEdit()
        self.rnoinput.setValidator(QIntValidator())
        self.rnoinput.setMaxLength(2)
        self.rnoinput.setPlaceholderText("Rno")
        layout.addWidget(self.rnoinput)
        layout.addWidget(self.QBtn1)
        
        self.pnoinput = QLineEdit()
        self.pnoinput.setValidator(QDoubleValidator())
        self.pnoinput.setMaxLength(10)
        self.pnoinput.setPlaceholderText("Mobile No.")
        layout.addWidget(self.pnoinput)
        
        self.emailinput = QLineEdit()
        self.emailinput.setPlaceholderText("email")
        layout.addWidget(self.emailinput) 
###########################################################
        self.ut1dbmsinput = QLineEdit()
        self.ut1dbmsinput.setValidator(QIntValidator())
        self.ut1dbmsinput.setMaxLength(2)
        self.ut1dbmsinput.setPlaceholderText("ut1dbms")
        layout.addWidget(self.ut1dbmsinput)      

        self.ut1sepminput = QLineEdit()
        self.ut1sepminput.setValidator(QIntValidator())
        self.ut1sepminput.setMaxLength(2)
        self.ut1sepminput.setPlaceholderText("ut1sepm")
        layout.addWidget(self.ut1sepminput)   
             
        self.ut1cninput = QLineEdit()
        self.ut1cninput.setValidator(QIntValidator())
        self.ut1cninput.setMaxLength(2)
        self.ut1cninput.setPlaceholderText("ut1cn")
        layout.addWidget(self.ut1cninput) 
               
        self.ut1iseeinput = QLineEdit()
        self.ut1iseeinput.setValidator(QIntValidator())
        self.ut1iseeinput.setMaxLength(2)
        self.ut1iseeinput.setPlaceholderText("ut1isee")
        layout.addWidget(self.ut1iseeinput)
                
        self.ut1tocinput = QLineEdit()
        self.ut1tocinput.setValidator(QIntValidator())
        self.ut1tocinput.setMaxLength(2)
        self.ut1tocinput.setPlaceholderText("ut1toc")
        layout.addWidget(self.ut1tocinput)
                
        self.ut2dbmsinput = QLineEdit()
        self.ut2dbmsinput.setValidator(QIntValidator())
        self.ut2dbmsinput	.setMaxLength(2)
        self.ut2dbmsinput.setPlaceholderText("ut2dbms")
        layout.addWidget(self.ut2dbmsinput)     
           
        self.ut2sepminput = QLineEdit()
        self.ut2sepminput.setValidator(QIntValidator())
        self.ut2sepminput.setMaxLength(2)
        self.ut2sepminput.setPlaceholderText("ut2sepm")
        layout.addWidget(self.ut2sepminput) 
               
        self.ut2cninput = QLineEdit()
        self.ut2cninput.setValidator(QIntValidator())
        self.ut2cninput.setMaxLength(2)
        self.ut2cninput.setPlaceholderText("ut2cn")
        layout.addWidget(self.ut2cninput) 
               
        self.ut2iseeinput = QLineEdit()
        self.ut2iseeinput.setValidator(QIntValidator())
        self.ut2iseeinput.setMaxLength(2)
        self.ut2iseeinput.setPlaceholderText("ut2isee")
        layout.addWidget(self.ut2iseeinput)
        
        self.ut2tocinput = QLineEdit()
        self.ut2tocinput.setValidator(QIntValidator())
        self.ut2tocinput.setMaxLength(2)
        self.ut2tocinput.setPlaceholderText("ut2toc")
        layout.addWidget(self.ut2tocinput)
###########################################################               
        self.genderinput = QComboBox()
        self.genderinput.addItem("male")
        self.genderinput.addItem("female")
        self.genderinput.addItem("other")

        layout.addWidget(self.genderinput)
        
        self.b1 = QRadioButton("Hostelite?")
        #self.b1.setChecked(True)
        #self.b1.toggled.connect(self.x)
        layout.addWidget(self.b1)
        
        layout.addWidget(self.QBtn)
        
        self.setLayout(layout)
        
    def callgen(self):
        name = self.nameinput.text()
        rno = self.rnoinput.text()
        rno=int(rno)-1
        name1=name+str(rno)
        gp.gen(name1) 
       
    def addstudent(self):
        name=""
        rno=0
        pno=0
        email=""
        ut1dbms=0
        ut2dbms=0
        ut1sepm=0
        ut2sepm=0
        ut1cn=0
        ut2cn=0
        ut1isee=0
        ut2isee=0
        ut1toc=0
        ut2toc=0
        e=0
        try:
        	name = self.nameinput.text()
        	if name.isalpha()==False:
        		raise Exception
        	
        	rno = self.rnoinput.text()
        	pno = self.pnoinput.text()
        	
        	if len(pno)!=10:
        		raise Exception
        	
        	email = self.emailinput.text()
        	gender = self.genderinput.itemText(self.genderinput.currentIndex())
        	ut1dbms = self.ut1dbmsinput.text()
        	ut1sepm = self.ut1sepminput.text()
        	ut1cn = self.ut1cninput.text()
        	ut1isee = self.ut1iseeinput.text()
        	ut1toc = self.ut1tocinput.text()
        	ut2dbms = self.ut2dbmsinput.text()
        	ut2sepm = self.ut2sepminput.text()
        	ut2cn = self.ut2cninput.text()
        	ut2isee = self.ut2iseeinput.text()
        	ut2toc = self.ut2tocinput.text()
        	if int(ut1dbms)>30 or int(ut1dbms)<0 or int(ut1sepm)>30 or int(ut1sepm)<0 or int(ut1cn)>30 or int(ut1cn)<0 or int(ut1isee)>30 or int(ut1isee)<0 or int(ut1toc)>30 or int(ut1toc)<0 or int(ut2dbms)>30 or int(ut2dbms)<0 or int(ut2sepm)>30 or int(ut2sepm)<0 or int(ut2cn)>30 or int(ut2cn)<0 or int(ut2isee)>30 or int(ut2isee)<0 or int(ut2toc)>30 or int(ut2toc)<0:
        		raise Exception
        	
        	if self.b1.isChecked():
        		hostelite="yes"
        	else:
        		hostelite="no"
        		
        	d.db.result.insert_one({"name": name,"rno" : rno,"pno":pno,"email": email,"gender":gender,"hostelite": hostelite,"ut1dbms":ut1dbms,"ut1sepm":ut1sepm,"ut1cn":ut1cn,"ut1isee":ut1isee,"ut1toc":ut1toc,"ut2dbms":ut2dbms,"ut2sepm":ut2sepm,"ut2cn":ut2cn,"ut2isee":ut2isee,"ut2toc":ut2toc})
        	d.db.pa.insert_one({"name": name,"rollno" : rno,"sdl":0,"dbms":0,"sepm":0,"cn":0,"isee":0,"toc":0})
        	QMessageBox.information(QMessageBox(), 'Successful', 'Successfully added student to the database.')
        	self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database. Check the data entered.')
            self.close()

class RecognizerDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(RecognizerDialog, self).__init__(*args, **kwargs)           
        self.setWindowTitle("Mark Attendance")
        self.setFixedWidth(800)
        self.setFixedHeight(800)

        self.subip = QComboBox()
        self.subip.addItem("SDL")
        self.subip.addItem("DBMS")
        self.subip.addItem("SEPM")
        self.subip.addItem("CN")
        self.subip.addItem("ISEE")
        self.subip.addItem("TOC")
        layout = QVBoxLayout()
        layout.addWidget(self.subip)
        self.QBtn = QPushButton()
        self.QBtn.setText("Mark Attendance")
        self.QBtn.clicked.connect(self.mark)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
        
    def mark(self):
     	sub = self.subip.itemText(self.subip.currentIndex())
     	if sub=="SDL":
     		import recog5 as re
     		re.detect("1")
     	elif sub=="DBMS":
     		import recog5 as re
     		re.detect("2")
     	elif sub=="SEPM":
     		import recog5 as re
     		re.detect("3")
     	elif sub=="CN":
     		import recog5 as re
     		re.detect("4")
     	elif sub=="ISEE":
     		import recog5 as re
     		re.detect("5")
     	elif sub=="TOC":
     		import recog5 as re
     		re.detect("6")

class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search Student")
        self.setFixedWidth(800)
        self.setFixedHeight(500)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):

        searchrol =0
        searchrol = self.searchinput.text()
        #searchrol=str(searchrol)
        
        self.name=[]
        self.rno=[]
        self.pno=[]
        self.email=[]
        self.gender=[]
        self.hostelite=[]
        self.ut1dbms=[]
        self.ut2dbms=[]
        self.ut1sepm=[]
        self.ut2sepm=[]
        self.ut1cn=[]
        self.ut2cn=[]
        self.ut1isee=[]
        self.ut2isee=[]
        self.ut1toc=[]
        self.ut2toc=[]
        records=d.db.result.find()
        j=0
        for i in records:
            j+=1
            self.name.append(i["name"])
            self.rno.append(i["rno"])
            self.pno.append(i["pno"])
            self.email.append(i["email"])
            self.gender.append(i["gender"])
            self.hostelite.append(i["hostelite"])
            self.ut1dbms.append(i["ut1dbms"])
            self.ut1sepm.append(i["ut1sepm"])
            self.ut1cn.append(i["ut1cn"])
            self.ut1isee.append(i["ut1isee"])
            self.ut1toc.append(i["ut1toc"])
            self.ut2dbms.append(i["ut2dbms"])
            self.ut2sepm.append(i["ut2sepm"])
            self.ut2cn.append(i["ut2cn"])
            self.ut2isee.append(i["ut2isee"])
            self.ut2toc.append(i["ut2toc"])
            
        for i in range(0,j):
            print(self.rno[i])
            p=self.rno[i]
            print(type(p))
            if p==searchrol:
                try:
                    serachresult = "Rollno : "+str(self.rno[i])+'\n'+"Name : "+str(self.name[i])+'\n'+"Mobile no : "+str(self.pno[i])+'\n'+"Email : "+str(self.email[i])+'\n'+"Gender : "+str(self.gender[i])
                    QMessageBox.information(QMessageBox(), 'Successful', serachresult)
                    break
                except Exception:
                    QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find student from the database.')
#***********************************************UPDATE***************************************************
class UpdateDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Update")

        self.setWindowTitle("Update Student Record")
        self.setFixedWidth(800)
        self.setFixedHeight(500)
        self.QBtn.clicked.connect(self.updatestudent)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.searchinput.setValidator(QIntValidator())
        self.searchinput.setMaxLength(2)
        self.searchinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.searchinput)
        
        
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)
        '''
        self.rnoinput = QLineEdit()
        self.rnoinput.setPlaceholderText("Rno")
        layout.addWidget(self.rnoinput)
        '''
        self.pnoinput = QLineEdit()
        self.pnoinput.setValidator(QDoubleValidator())
        self.pnoinput.setMaxLength(10)
        self.pnoinput.setPlaceholderText("Mobile No.")
        layout.addWidget(self.pnoinput)
        
        self.emailinput = QLineEdit()
        self.emailinput.setPlaceholderText("email")
        layout.addWidget(self.emailinput) 
###########################################################
        self.ut1dbmsinput = QLineEdit()
        self.ut1dbmsinput.setValidator(QIntValidator())
        self.ut1dbmsinput.setMaxLength(2)
        self.ut1dbmsinput.setPlaceholderText("ut1dbms")
        layout.addWidget(self.ut1dbmsinput)      

        self.ut1sepminput = QLineEdit()
        self.ut1sepminput.setValidator(QIntValidator())
        self.ut1sepminput.setMaxLength(2)
        self.ut1sepminput.setPlaceholderText("ut1sepm")
        layout.addWidget(self.ut1sepminput)   
             
        self.ut1cninput = QLineEdit()
        self.ut1cninput.setValidator(QIntValidator())
        self.ut1cninput.setMaxLength(2)
        self.ut1cninput.setPlaceholderText("ut1cn")
        layout.addWidget(self.ut1cninput) 
               
        self.ut1iseeinput = QLineEdit()
        self.ut1iseeinput.setValidator(QIntValidator())
        self.ut1iseeinput.setMaxLength(2)
        self.ut1iseeinput.setPlaceholderText("ut1isee")
        layout.addWidget(self.ut1iseeinput)
                
        self.ut1tocinput = QLineEdit()
        self.ut1tocinput.setValidator(QIntValidator())
        self.ut1tocinput.setMaxLength(2)
        self.ut1tocinput.setPlaceholderText("ut1toc")
        layout.addWidget(self.ut1tocinput)
                
        self.ut2dbmsinput = QLineEdit()
        self.ut2dbmsinput.setValidator(QIntValidator())
        self.ut2dbmsinput.setMaxLength(2)
        self.ut2dbmsinput.setPlaceholderText("ut2dbms")
        layout.addWidget(self.ut2dbmsinput)     
           
        self.ut2sepminput = QLineEdit()
        self.ut2sepminput.setValidator(QIntValidator())
        self.ut2sepminput.setMaxLength(2)
        self.ut2sepminput.setPlaceholderText("ut2sepm")
        layout.addWidget(self.ut2sepminput) 
               
        self.ut2cninput = QLineEdit()
        self.ut2cninput.setValidator(QIntValidator())
        self.ut2cninput.setMaxLength(2)
        self.ut2cninput.setPlaceholderText("ut2cn")
        layout.addWidget(self.ut2cninput) 
               
        self.ut2iseeinput = QLineEdit()
        self.ut2iseeinput.setValidator(QIntValidator())
        self.ut2iseeinput.setMaxLength(2)
        self.ut2iseeinput.setPlaceholderText("ut2isee")
        layout.addWidget(self.ut2iseeinput)
        
        self.ut2tocinput = QLineEdit()
        self.ut2tocinput.setValidator(QIntValidator())
        self.ut2tocinput.setMaxLength(2)
        self.ut2tocinput.setPlaceholderText("ut2toc")
        layout.addWidget(self.ut2tocinput)
###########################################################               
        self.genderinput = QComboBox()
        self.genderinput.addItem("male")
        self.genderinput.addItem("female")
        self.genderinput.addItem("other")

        layout.addWidget(self.genderinput)
        
        self.b1 = QRadioButton("Hostelite?")
        #self.b1.setChecked(True)
        #self.b1.toggled.connect(self.x)
        layout.addWidget(self.b1)
        
        layout.addWidget(self.QBtn)
        
        self.setLayout(layout)

    def updatestudent(self):
    	uprol=""
    	uprol=self.searchinput.text()
    	#uprol=int(uprol)
    	records=d.db.result.find()
    	name=""
    	rno=0
    	pno=0
    	email=""
    	ut1dbms=0
    	ut2dbms=0
    	ut1sepm=0
    	ut2sepm=0
    	ut1cn=0
    	ut2cn=0
    	ut1isee=0
    	ut2isee=0
    	ut1toc=0
    	ut2toc=0
    	
    	if self.b1.isChecked():
    	    hostelite="yes"
    	else:
    	    hostelite="no"
    	try:
        	name = self.nameinput.text()
        	if name.isalpha()==False:
        		raise Exception
        	
        	rno = self.rnoinput.text()
        	pno = self.pnoinput.text()
        	
        	if len(pno)!=10:
        		raise Exception
        	
        	email = self.emailinput.text()
        	gender = self.genderinput.itemText(self.genderinput.currentIndex())
        	ut1dbms = self.ut1dbmsinput.text()
        	ut1sepm = self.ut1sepminput.text()
        	ut1cn = self.ut1cninput.text()
        	ut1isee = self.ut1iseeinput.text()
        	ut1toc = self.ut1tocinput.text()
        	ut2dbms = self.ut2dbmsinput.text()
        	ut2sepm = self.ut2sepminput.text()
        	ut2cn = self.ut2cninput.text()
        	ut2isee = self.ut2iseeinput.text()
        	ut2toc = self.ut2tocinput.text()
        	if int(ut1dbms)>30 or int(ut1dbms)<0 or int(ut1sepm)>30 or int(ut1sepm)<0 or int(ut1cn)>30 or int(ut1cn)<0 or int(ut1isee)>30 or int(ut1isee)<0 or int(ut1toc)>30 or int(ut1toc)<0 or int(ut2dbms)>30 or int(ut2dbms)<0 or int(ut2sepm)>30 or int(ut2sepm)<0 or int(ut2cn)>30 or int(ut2cn)<0 or int(ut2isee)>30 or int(ut2isee)<0 or int(ut2toc)>30 or int(ut2toc)<0:
        		raise Exception
        	
        	if self.b1.isChecked():
        		hostelite="yes"
        	else:
        		hostelite="no"
        	d.db.result.update_many({"rno":uprol},{"$set":{"name":name,"pno":pno,"email":email,"gender":gender,"hostelite":hostelite,"ut1dbms":ut1dbms,"ut1sepm":ut1sepm,"ut1cn":ut1cn,"ut1isee":ut1isee,"ut1toc":ut1toc,"ut2dbms":ut2dbms,"ut2sepm":ut2sepm,"ut2cn":ut2cn,"ut2isee":ut2isee,"ut2toc":ut2toc}})
        	d.db.pa.update_one({"rollno":uprol},{"$set":{"name":name}})
        	QMessageBox.information(QMessageBox(), 'Successful', 'Successfully updated student to the database.')
        	self.close()
    	except Exception:
    	    QMessageBox.warning(QMessageBox(), 'Error', 'Could not update student in the database.')        
#***************************************************************
class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Student")
        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.QBtn.clicked.connect(self.deletestudent)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):

        delrol = ""
        delrol = self.deleteinput.text()

        try:
            records=d.db.result.delete_one({"rno":delrol})
            records=d.db.pa.delete_one({"rollno":delrol})
            QMessageBox.information(QMessageBox(), 'Successful',"Record is succesfully deleted")
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete student from the database.')

#****************************************************GRAPH**********************************************

class PlotGraph(QDialog):
	def __init__(self, *args, **kwargs):
		super(PlotGraph, self).__init__(*args, **kwargs)
		
		
		#self.QBtn.setText("PLOT")
		#self.QBtn.setGeometry(QRect(78, 464, 341, 71))
		#self.setStyleSheet("background-color: white")
		l1=QLabel()
		l1.setText("ATTENDANCE ANALYSIS")
		l1.setAlignment(Qt.AlignCenter)
		l1.setFont(QFont("Arial",15))
		
		l4=QLabel()
		l4.setText("Compare attendance of any two subjects")
		l4.setAlignment(Qt.AlignLeft)
		l4.setFont(QFont("Arial",11))
		
		l2=QLabel()
		l2.setText("RESULT ANALYSIS")
		l2.setAlignment(Qt.AlignCenter)
		l2.setFont(QFont("Arial",15))
		
		l3=QLabel()
		l3.setText("GENRAL ANALYSIS")
		l3.setAlignment(Qt.AlignCenter)
		l3.setFont(QFont("Arial",15))
		
		l5=QLabel()
		l5.setText("DEFAULTER STATISTICS")
		l5.setAlignment(Qt.AlignCenter)
		l5.setFont(QFont("Arial",15))

		
		self.setWindowTitle("STUDENT DATA ANALYSIS : GRPAH PLOTS")
		self.setFixedWidth(500)
		self.setFixedHeight(550)
		
		self.QBtn = QPushButton("Plot",self)
		self.QBtn.clicked.connect(self.plot_attendance)		
		
		
		self.QBtn1 = QPushButton("Plot",self)                    # plot button for result analysis
		self.QBtn1.clicked.connect(self.plot_result)
		
		
		self.QBtn2 = QPushButton("VIEW GENDER DISTRIBUTION",self)                    # plot button for result analysis
		self.QBtn2.clicked.connect(self.gender_analysis)
		
		self.QBtn3= QPushButton("VIEW HOSTELITE COUNT",self)                    # plot button for result analysis
		self.QBtn3.clicked.connect(self.hostel_analysis)
		
		self.QBtn4= QPushButton("DEFAULTER STATISTICS",self)                    # ATTENDANCE DEFAULTER ANALYSIS
		self.QBtn4.clicked.connect(self.default_analysis)
		
		self.plotinput = QComboBox()
		self.plotinput.addItem("SDL")
		self.plotinput.addItem("DBMS")
		self.plotinput.addItem("SEPM")
		self.plotinput.addItem("CN")
		self.plotinput.addItem("ISEE")
		self.plotinput.addItem("TOC")
		
		
		self.plotinput1 = QComboBox()		#    DROP DOWN FOR ATTENDANACE 
		self.plotinput1.addItem("SDL")
		self.plotinput1.addItem("DBMS")
		self.plotinput1.addItem("SEPM")
		self.plotinput1.addItem("CN")
		self.plotinput1.addItem("ISEE")
		self.plotinput1.addItem("TOC")
		
		
		
		self.plotinput2 = QComboBox()			# DROP DOWN FOR RESULT ANALYSIS
		self.plotinput2.addItem("DBMS")
		self.plotinput2.addItem("SEPM")
		self.plotinput2.addItem("CN")
		self.plotinput2.addItem("ISEE")
		self.plotinput2.addItem("TOC")
		
		
		self.plotinput3 = QComboBox()
		self.plotinput3.addItem("SDL")			# DROP DOWN FOR defaulter 
		self.plotinput3.addItem("DBMS")
		self.plotinput3.addItem("SEPM")
		self.plotinput3.addItem("CN")
		self.plotinput3.addItem("ISEE")
		self.plotinput3.addItem("TOC")
		
		verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
		layout = QVBoxLayout()
		layout.addWidget(l1,alignment=Qt.AlignLeft)
		#layout.addWidget(l4)
		layout.addWidget(self.plotinput1)
		layout.addWidget(self.plotinput)
		layout.addWidget(self.QBtn,alignment=Qt.AlignCenter)
		self.QBtn.setFixedWidth(200)
		layout.addWidget(l5,alignment=Qt.AlignLeft)
		layout.addWidget(self.plotinput3)
		layout.addWidget(self.QBtn4,alignment=Qt.AlignCenter)
		self.QBtn4.setFixedWidth(200)
		layout.addWidget(l2,alignment=Qt.AlignLeft)
		layout.addWidget(self.plotinput2) # FOR RESULT ANALYSIS
		layout.addWidget(self.QBtn1,alignment=Qt.AlignCenter)
		self.QBtn1.setFixedWidth(200)
		layout.addWidget(l3,alignment=Qt.AlignLeft)
		layout.addWidget(self.QBtn2,alignment=Qt.AlignCenter) # gender distribution
		self.QBtn2.setFixedWidth(200)
		layout.addItem(verticalSpacer)
		layout.addWidget(self.QBtn3,alignment=Qt.AlignCenter)   # hostel distribution
		self.QBtn3.setFixedWidth(200)
		
		self.setLayout(layout)
        
	def plot_attendance(self):
		p.graph(self.plotinput.itemText(self.plotinput.currentIndex()),self.plotinput1.itemText(self.plotinput1.currentIndex()))
		
	def plot_result(self):
		ra.graph(self.plotinput2.itemText(self.plotinput2.currentIndex()))
	
	def gender_analysis (self):   # gender
		ra.pie_chart(self)
	
	def hostel_analysis (self):    # hostelite count
		ra.host(self)
		
	def default_analysis (self):    # defaaulter - attendance
		p.defaulter(self.plotinput3.itemText(self.plotinput3.currentIndex()))
		
        
	



#***********************************************UPDATE****

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g2.png'))  #window icon
        
        self.setStyleSheet("background-image: url(My_Post.jpg)")
        
        self.setWindowTitle("Student Record Maintainer")
        self.setMinimumSize(1700, 1000)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setFont(QFont('Arial',16))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        #self.tableWidget.setHorizontalHeaderLabels(("Name", "Roll No", "Mobile no", "Email", "Gender","Hostelite","ut1dbms","ut1sepm","UT1cn","UT1isee","UT1toc","UT2dbms","UT2sepm","UT2cn","UT2isee","UT2toc"))
        

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        
        #************** ICON ****************
        toolbar.setIconSize(QSize(72, 72))
        toolbar.setFixedHeight(40)
        
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_spacer = QWidget()
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        toolbar.addWidget(left_spacer)

        
        btn_ac_adduser122 = QAction(QIcon("icon/plot.png"), "Show PLot", self)   #add student icon
        btn_ac_adduser122.triggered.connect(self.plo)
        btn_ac_adduser122.setStatusTip("Show plot")
        toolbar.addAction(btn_ac_adduser122)
        
        btn_ac_adduser12 = QAction(QIcon("icon/show.png"), "Show Attendance", self)   #add student icon
        btn_ac_adduser12.triggered.connect(self.load_data)
        btn_ac_adduser12.setStatusTip("Show Attendance")
        toolbar.addAction(btn_ac_adduser12)
        
        
        
        btn_ac_adduser1 = QAction(QIcon("icon/images.png"), "Train Dataset", self)   #add student icon
        btn_ac_adduser1.triggered.connect(self.train)
        btn_ac_adduser1.setStatusTip("Train Dataset")
        toolbar.addAction(btn_ac_adduser1)

        btn_ac_adduser = QAction(QIcon("icon/add1.jpg"), "Add Student", self)   #add student icon
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add Student")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_adduser1 = QAction(QIcon("icon/attendance1.png"), "Mark Attendance", self)   #add student icon
        btn_ac_adduser1.triggered.connect(self.callrecog)
        btn_ac_adduser1.setStatusTip("Mark Attendance")
        toolbar.addAction(btn_ac_adduser1)

        btn_ac_refresh = QAction(QIcon("icon/r3.png"),"Refresh",self)   #refresh icon
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  #search icon
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)
        
        btn_ac_update = QAction(QIcon("icon/update.png"), "Update Record", self)  #update icon
        btn_ac_update.triggered.connect(self.update)
        btn_ac_update.setStatusTip("Update Record")
        toolbar.addAction(btn_ac_update)

        btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete User")
        toolbar.addAction(btn_ac_delete)

        adduser_action = QAction(QIcon("icon/add1.jpg"),"Insert Student", self)
        adduser_action.triggered.connect(self.insert)
        

        searchuser_action = QAction(QIcon("icon/s1.png"), "Search Student", self)
        searchuser_action.triggered.connect(self.search)
        

        deluser_action = QAction(QIcon("icon/d1.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
        
        toolbar.addWidget(right_spacer)
        
        
        
        
        

    def loaddata(self):
    	
        self.name=[]
        self.rno=[]
        self.pno=[]
        self.email=[]
        self.gender=[]
        self.hostelite=[]
        self.ut1dbms=[]
        self.ut2dbms=[]
        self.ut1sepm=[]
        self.ut2sepm=[]
        self.ut1cn=[]
        self.ut2cn=[]
        self.ut1isee=[]
        self.ut2isee=[]
        self.ut1toc=[]
        self.ut2toc=[]
        self.tableWidget.setFont(QFont('Arial',15))
        self.tableWidget.setHorizontalHeaderLabels(("Name", "Roll No", "Mobile no", "Email", "Gender","Hostelite","ut1dbms","ut1sepm","UT1cn","UT1isee","UT1toc","UT2dbms","UT2sepm","UT2cn","UT2isee","UT2toc"))
        records=d.db.result.find()
        j=0
        for i in records:
            j+=1
            self.name.append(i["name"])
            self.rno.append(i["rno"])
            self.pno.append(i["pno"])
            self.email.append(i["email"])
            self.gender.append(i["gender"])
            self.hostelite.append(i["hostelite"])
            self.ut1dbms.append(i["ut1dbms"])
            self.ut1sepm.append(i["ut1sepm"])
            self.ut1cn.append(i["ut1cn"])
            self.ut1isee.append(i["ut1isee"])
            self.ut1toc.append(i["ut1toc"])
            self.ut2dbms.append(i["ut2dbms"])
            self.ut2sepm.append(i["ut2sepm"])
            self.ut2cn.append(i["ut2cn"])
            self.ut2isee.append(i["ut2isee"])
            self.ut2toc.append(i["ut2toc"])
        self.tableWidget.setRowCount(0)
        k=0
        data={"rno":self.rno,"name":self.name,"pno":self.pno,"email":self.email,"gender":self.gender,"hostelite":self.hostelite,"ut1dbms":self.ut1dbms,"ut1sepm":self.ut1sepm,"ut1cn":self.ut1cn,"ut1isee":self.ut1cn,"ut1toc":self.ut1toc,"ut2dbms":self.ut2dbms,"ut2sepm":self.ut2sepm,"ut2cn":self.ut2cn,"ut2isee":self.ut2cn,"ut2toc":self.ut2toc}
        df=pd.DataFrame(data,columns=["rno","name","pno","email","gender","hostelite","ut1dbms","ut1sepm","ut1cn","ut1isee","ut1toc","ut2dbms","ut2sepm","ut2cn","ut2isee","ut2toc"])
        df.to_csv("result.csv",index=True)
        for i in enumerate(self.name):
            self.tableWidget.insertRow(k)
            for j in range(0,16):
                if j==0:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.name[k])))
                if j==1:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.rno[k])))
                if j==2:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.pno[k])))
                if j==3:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.email[k])))
                if j==4:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.gender[k])))
                if j==5:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.hostelite[k])))
                if j==6:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut1dbms[k])))
                if j==7:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut1sepm[k])))
                if j==8:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut1cn[k])))
                if j==9:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut1isee[k])))
                if j==10:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut1toc[k])))
                if j==11:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut2dbms[k])))
                if j==12:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut2sepm[k])))
                if j==13:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut2cn[k])))
                if j==14:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut2isee[k])))
                if j==15:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.ut2toc[k])))
            k=k+1
            

##############################################

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()
        
    def update(self):
        dlg = UpdateDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def callrecog(self):
        dlg = RecognizerDialog()
        dlg.exec_()
        
    def train(self):
    	import trainer as t
    	t.train1()
    def plo(self):
    	dlg = PlotGraph()
    	dlg.exec_()
    	
    def load_data(self):
    
        self.name=[]
        self.rollno=[]
        self.sdl=[]
        self.dbms=[]
        self.sepm=[]
        self.cn=[]
        self.isee=[]
        self.toc=[]
        self.tableWidget.setHorizontalHeaderLabels(("Rollno", "Name", "SDL","DBMS","SEPM","CN","ISEE","TOC"," "," "," "," "," "," "," "," " ))
        
        records=d.db.pa.find()
        j=0
        for i in records:
            j+=1
            self.name.append(i["name"])
            self.rollno.append(i["rollno"])
            self.sdl.append(i["sdl"])
            self.dbms.append(i["dbms"])
            self.sepm.append(i["sepm"])
            self.cn.append(i["cn"])
            self.isee.append(i["isee"])
            self.toc.append(i["toc"])
        self.tableWidget.setRowCount(0)
        k=0
        data={"rollno":self.rollno,"name":self.name,"sdl":self.sdl,"dbms":self.dbms,"sepm":self.sepm,"cn":self.cn,"isee":self.isee,"toc":self.toc}
        df=pd.DataFrame(data,columns=["rollno","name","sdl","dbms","sepm","cn","isee","toc"])
        df.to_csv("attendance.csv",index=True)
        for i in enumerate(self.name):
            self.tableWidget.insertRow(k)
            for j in range(0,8):
                if j==0:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.rollno[k])))
                if j==1:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.name[k])))
                if j==2:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.sdl[k])))
                if j==3:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.dbms[k])))
                if j==4:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.sepm[k])))
                if j==5:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.cn[k])))
                if j==6:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.isee[k])))
                if j==7:
                    self.tableWidget.setItem(k,j,QTableWidgetItem(str(self.toc[k])))
                
            k=k+1

app = QApplication(sys.argv)

login=Login()
if(login.exec_()==QDialog.Accepted):
	window = MainWindow()
	window.show()
	#window.loaddata()
sys.exit(app.exec_())
