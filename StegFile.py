import os;
from subprocess import Popen, PIPE

root, dirs, files = next(os.walk('/home/mohammad/Documents/python/Steganalysis/steg'));
for file in files:
    if file.lower().endswith('.wav'):
        p = Popen('steghide embed -cf /home/mohammad/Documents/python/Steganalysis/steg/' + file + ' --dontcompress -ef  /home/mohammad/Documents/python/Steganalysis/steg/secret.txt -p kabinet95', shell=True,
                  stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        print(err);