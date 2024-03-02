#zadanie nr 1
import datetime
import os
import time
import shutil

#os.chdir('C:\\Users\\szymo\\Desktop')
#os.mkdir('folder testowy')
#time.sleep(5)
#os.rmdir('folder testowy')

os.chdir('C:\\Users\\szymo\\Desktop')

if os.path.exists('./foldertestowy'):
    shutil.rmtree('foldertestowy')

os.mkdir('foldertestowy')
os.chdir('C:\\Users\\szymo\\Desktop\\foldertestowy')

for i in range(10):
    time_now = datetime.datetime.now()
    time_now_f = time_now.strftime("%H%M%S")
    file = open(f'report {time_now_f}.txt', 'w')
    file.write('asdf')
    file.close()
    time.sleep(2)

