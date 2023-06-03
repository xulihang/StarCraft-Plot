#coding=utf-8
f=open("plot.txt","r",encoding="utf-8")
en_content=""
cn_content=""
content=""
for line in f.readlines():
    if line.find("->")!=-1:
        #en_content=en_content+(line.split("->")[0].strip().replace("||","")+"\n")
        #cn_content=cn_content+(line.split("->")[1].strip().replace("||","")+"\n")
        content=content+line.split("->")[0].strip().replace("||","")+"->"+line.split("->")[1].strip().replace("||","")+"\n"
f.close()
'''
fw=open("cn.txt","w")
fw.write(cn_content)
fw.close()
fw=open("en.txt","w")
fw.write(en_content)
fw.close()
'''
fw=open("out.txt","w")
fw.write(content)
fw.close()
