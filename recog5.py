import cv2
from face_detection import face
from keras.models import load_model
import numpy as np
from embedding import emb
from retreive_pymongo_data_2 import database
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

def detect(num):
	subno=num
	data=database()
	a={}
	people={}
	def getdata():
	    name=[]
	    records=data.db.pa.find()
	    j=0
	    for i in records:
	        j+=1
	        name.append(i["name"])
	    k=len(name)
	    for i in range(0,k):
	        people[i]=name[i]
	        a[i]=0
	getdata()
	print(a)
	print(people)
	label=None
	abhi=None
	
	x=a
	
	e=emb()
	fd=face()
	model=load_model('face_reco2.MODEL')
	
	def test():
	    test_run=cv2.imread('1.jpg',1)
	    test_run=cv2.resize(test_run,(160,160))
	    #test_run=np.rollaxis(test_run,2,0)
	    test_run=test_run.astype('float')/255.0
	    test_run=np.expand_dims(test_run,axis=0)
	    test_run=e.calculate(test_run)
	    test_run=np.expand_dims(test_run,axis=0)
	    test_run=model.predict(test_run)[0]
	    
	cap=cv2.VideoCapture(-1)
	ret=True
	test()
	while ret:
	    ret,frame=cap.read()
	    frame=cv2.flip(frame,1)
	    det,coor=fd.detectFace(frame)
	    
	    if(det is not None):
	        for i in range(len(det)):
	            detected=det[i]
	            k=coor[i]
	            f=detected
	            detected=cv2.resize(detected,(160,160))
	            #detected=np.rollaxis(detected,2,0)
	            detected=detected.astype('float')/255.0
	            detected=np.expand_dims(detected,axis=0)
	            feed=e.calculate(detected)
	            feed=np.expand_dims(feed,axis=0)
	            prediction=model.predict(feed)[0]
	            
	            result=int(np.argmax(prediction))
	            if(np.max(prediction)>.70):
	                for i in people:
	                    if(result==i):
	                        label=people[i]
	                        if(a[i]==0):
	                            print("a")
	                            data.update(label,subno)
	                            a[i]=1
	                            abhi=i
	            else:
	                label='unknown'
	            cv2.putText(frame,label,(k[0],k[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
	            x=k[0]
	            y=k[1]
	            if(abhi is not None):
	                if(a[abhi]==1):
	                    cv2.putText(frame,"your attendance is complete",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
	                    cv2.rectangle(frame,(k[0],k[1]),(k[0]+k[2],k[1]+k[3]),(252,160,39),3)
	            cv2.imshow('onlyFace',f)
	    cv2.imshow('frame',frame)
	    if(cv2.waitKey(1) & 0XFF==ord('q')):
	        break
	cap.release()
	cv2.destroyAllWindows()
	data.export_csv()
	#from a import App
	#app = QApplication(sys.argv)
	#ex = App()
	#sys.exit(app.exec_())
