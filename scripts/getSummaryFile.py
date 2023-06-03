#coding=utf-8
title=""
f=open("out.txt","r",encoding="utf-8")
fw=open("SUMMARY.MD","w",encoding="utf-8")
for line in f.readlines():
    
    fw.write("* ["+line.replace("\n","")+"]("+"_".join(line.split(" ")[:-1][2:])+".md)\n")
fw.close()
f.close()
