import os
import sys
import shutil

f = open('template_overlay.html','r')
overlay = f.read()
f.close()

for root, dirs, files in os.walk(".\\raw"):
    for file in files:
        fn = root + "\\" + file
        fnn = fn.replace('.\\raw','.')
        d = os.path.dirname(fnn)
        if not os.path.exists(d):
            os.mkdir(d)
        if file.endswith(".html"):
            print(fn)
            f = open(fn, "r")
            c = f.read()
            f.close()
            f = open(fnn,'w')
            f.write(overlay.replace("{CONTENT}",c))
            f.close()
        else:
            shutil.copy(fn,fnn)