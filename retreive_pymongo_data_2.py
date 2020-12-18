
from pymongo import MongoClient
import pandas as pd
class database:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.new
        self.name=[]
        self.attendance=[]
        self.rollno=[]
		
    def update(self,name,subno):
    	if subno=="1":
        	self.db.pa.update_one({"name":name},{"$inc":{"sdl":1}})
    	elif subno=="2":
        	self.db.pa.update_one({"name":name},{"$inc":{"dbms":1}})
    	elif subno=="3":
        	self.db.pa.update_one({"name":name},{"$inc":{"sepm":1}})
    	elif subno=="4":
        	self.db.pa.update_one({"name":name},{"$inc":{"cn":1}})
    	elif subno=="5":
        	self.db.pa.update_one({"name":name},{"$inc":{"isee":1}})
    	elif subno=="6":
        	self.db.pa.update_one({"name":name},{"$inc":{"toc":1}})


    def view(self):
        self.name=[]
        self.sdl=[]
        self.dbms=[]
        self.sepm=[]
        self.cn=[]
        self.isee=[]
        self.toc=[]
        self.rollno=[]
        records=self.db.pa.find()
        j=0
        for i in records:
            j=j+1
            self.name.append(i["name"])
            self.sdl.append(i["sdl"])
            self.dbms.append(i["dbms"])
            self.sepm.append(i["sepm"])
            self.cn.append(i["cn"])
            self.isee.append(i["isee"])
            self.toc.append(i["toc"])
            self.rollno.append(i["rollno"])
            
        for i in range(j):
            print(self.rollno[i],self.name[i],self.sdl[i],self.dbms[i],self.sepm[i],self.cn[i],self.isee[i],self.toc[i])

    def export_csv(self):
        self.view()
        data={"rollno":self.rollno,"name":self.name,"sdl":self.sdl,"dbms":self.dbms,"sepm":self.sepm,"cn":self.cn,"isee":self.isee,"toc":self.toc}
        df=pd.DataFrame(data,columns=["rollno","name","sdl","dbms","sepm","cn","isee","toc"])
        df.to_csv("attendance.csv",index=True)
