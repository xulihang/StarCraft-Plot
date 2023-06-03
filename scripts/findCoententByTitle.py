#coding=utf-8
f=open("plot.txt","r",encoding="utf-8")
title=""
content=""

for line in f.readlines():
    if line.find("->")!=-1:
        en=line.split("->")[0]
        cn=line.split("->")[1]
        if en.find("\"")!=-1:
            if cn.find("“")!=-1 or cn.find("”")!=-1 or cn.find("\"")!=-1:
                if en.find("||")!=-1:
                    if en.split("||")[1].replace("\"","").isupper():
                        print(line)
                        if title!="":
                            fw=open(title.replace(" ","_")+".txt","w",encoding="utf-8")
                            fw.write(content)
                            fw.close()
                        title=en.split("||")[1].replace("\"","") ####
                        content=line+"\n"
                else:
                    if en.replace("\"","").isupper():
                        print(line)
        else:
            content=content+line+"\n"
                
                    
        #content=content+line.split("->")[0].strip().replace("||","")+"->"+line.split("->")[1].strip().replace("||","")+"\n"
f.close()
