#coding=utf-8
import os,traceback
s = os.sep //检测分隔符\或者/
root = "/mnt/hd"+s//设定起始目录
file=open('filename.txt',"a",encoding='utf-8')
for rt,dirs,files in os.walk(root):
    for f in files:
        if rt[-1] == s:
            file.write(rt+f)
        else:
            file.write(rt+s+f)        
        file.write("\n")
        fname = os.path.splitext(f)
        try:
            pass
        except:
            err_file=open("err.txt",'a',encoding='utf-8')
            traceback.print_exc(file=err_file)
            err_file.flush()
            err_file.close()
            file.close()
