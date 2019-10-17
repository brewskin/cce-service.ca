from sys import exit
import docx2txt
import docx

def next_line (txt_file,i):
    b =txt_file.find('\n',i+1)
    txt = txt_file[i:b]
    out = [txt, b]
    return out

txt = docx2txt.process("Service_Request_Sasha Radiology.docx")
index = 1
while index >= 1:
    strprint = next_line(txt,index)
    strprint[0] = strprint[0].strip()

    index = strprint[1]
    if strprint[0]:
        print(strprint[0])
        #input(index)

"""txt = txt.strip()
doc = open("testfile.txt","w")
doc.write(txt)

doc.close()"""
