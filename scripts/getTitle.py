#coding=utf-8
title=""
f=open("titles.txt","r",encoding="utf-8")
for line in f.readlines():
    if line.find("->")!=-1:
        en=line.split("->")[0]
        cn=line.split("->")[1]
        print(line)
        line=en.split("||")[0]+" "+cn.split("||")[0].split(":")[1].strip()
        title=title+line.replace("\"","")+"\n"
f.close()

f=open("out.txt","w",encoding="utf-8")
f.write(title)
f.close()
    
