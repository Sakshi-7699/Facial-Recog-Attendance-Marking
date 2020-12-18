from pymongo import MongoClient
import pandas as pd 
class result:
	def __init__(self):
		self.client=MongoClient()
		self.db=self.client.new
		self.name=[]
		self.rno=[]
		self.pno=[]
		self.email=[]
		self.gender=[]
		self.hostelite=[]
		
	def view (self):
		self.name=[]
		self.rno=[]
		self.pno=[]
		self.email=[]
		self.gender=[]
		self.hostelite=[]
		records=self.db.result.find()
		j=0
		for i in records:
			j+=1 
			self.name.append(i["name"])
			self.rno.append(i["rno"])
			self.pno.append(i["pno"])
			self.email.append(i["email"])
			self.gender.append(i["gender"])
			self.hostelite.append(i["hostelite"])
		
			
	def insert_student_details(self):
		print("\n\t\tENTER STUDENT DETILS\n\n")
		name=input("Name : ")
		rno=input("Roll no : ")
		pno=input("Phone No. : ")
		email=input("Email ID : ")
		gender=input("Gender : ")
		hostelite=input("Hostelite? : ")
		self.db.result.insert({"name": name,"rno" : rno,"pno":pno,"email": email,"gender":gender,"hostelite": hostelite})


		
			
	def export_csv(self):
		self.view()
		data={"name":self.name,"rno":self.rno,"pno":self.pno,"email":self.email,"gender":self.gender,"hostelite":self.hostelite}
		df=pd.DataFrame(data,columns=["name","rno","pno","email","gender","hostelite"])
		df.to_csv("Result.csv",index=True)
		        

        
        
			

		 
