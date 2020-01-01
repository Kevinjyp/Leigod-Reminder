import os
import subprocess
import time

opened = False

while (True):
    time.sleep(1)
    output = os.popen('tasklist | findStr Leigod')
    output = output.read()

    if (len(output) == 0) & opened:
        print("Leigod is Closed")
        args=[r"powershell",r"./notification.ps1"]
        p=subprocess.Popen(args)
        break
    elif len(output) != 0:
        opened = True
        print("Leigod is been Using")
        print(output)
    else:
        print("Leigod hasn't been Using")



# print(output)
# print(len(output))
# print(opened)