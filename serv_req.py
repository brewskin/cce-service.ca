from docx import Document
from sys import argv
import os.path
from datetime import datetime


script, req_date,req_time,req_client,req_department,req_address,req_phone,req_contact,req_system,type,req_desc = argv

#file_name = "output_text.txt"
#txt = open(file_name,"a")
#print "-------------------File is Opening--------</br>"
#print "------------------------------------------</br>" 
#txt.write(req_date + " is the date!\n")

template = Document('S_R_F.docx')

newFile = template
tab = newFile.tables[0]


tab.cell(0,1).paragraphs[0].clear()
tab.cell(0,1).paragraphs[0].text = req_date

tab.cell(1,1).paragraphs[0].clear()
tab.cell(1,1).paragraphs[0].text = req_time

tab.cell(2,1).paragraphs[0].clear()
tab.cell(2,1).paragraphs[0].text = req_client

tab.cell(3,1).paragraphs[0].clear()
tab.cell(3,1).paragraphs[0].text = req_department

tab.cell(4,1).paragraphs[0].clear()
tab.cell(4,1).paragraphs[0].text = req_address

tab.cell(5,1).paragraphs[0].clear()
tab.cell(5,1).paragraphs[0].text = req_phone

tab.cell(6,1).paragraphs[0].clear()
tab.cell(6,1).paragraphs[0].text = req_contact

tab.cell(7,1).paragraphs[0].clear()
tab.cell(7,1).paragraphs[0].text = req_system

tab.cell(8,1).paragraphs[0].clear()
tab.cell(8,1).paragraphs[0].text = type

tab.cell(9,1).paragraphs[0].clear()
tab.cell(9,1).paragraphs[0].text = req_desc

newFileName = req_client+'_'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")
newFileName = 'S_Req_'+newFileName.replace(" ", "_")+'.docx'
newFile.save(newFileName)
print (newFileName)
#newFile.close()

"""/*
print req_date," is Date</br>"
print req_time," is Time</br>"
print req_client," is Client</br>"
print req_department," is department</br>"
print req_address," is address</br>"
print req_phone," is Phone</br>"
print req_contact," is Contact</br>"
print req_system," is System</br>"
print type," is Type</br>"
print req_desc," is Description</br>"
"""

#txt.close()
#print "-------------------File Closed-------------</br>"
#print "-------------------------------------------</br>"

#print("This is fun.</br>")
#print('Yay! Printing')
#print("I'd much rather you </br>")
#print('I "said" do not touch this.</br>')
