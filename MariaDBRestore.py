import os
import fileinput
import sys

import bz2
from bz2 import decompress




#THis function will decompress files for respecitive app server
def DecompressBZ2files(userInDir,userOpDir):

    Decomdirpath = userOpDir+"/"+gsrvname
    bz2filepath = userInDir+"/"+gsrvname
    if os.path.exists(Decomdirpath) is False:
        os.makedirs(Decomdirpath)
        print "created dir decom"

    for file in os.listdir(bz2filepath):
        archive_path = os.path.join(userInDir+"/"+gsrvname, file)
        outfile_path = os.path.join(userOpDir+"/"+gsrvname, file[:-4])
        with open(archive_path, 'rb') as source, open(outfile_path, 'wb') as dest:
            dest.write(bz2.decompress(source.read()))
    print "Decmpression has been done for " +gsrvname


def MariaDBRestore():
    print "scp %s nirav.joshi@108.168.207.6:/home/nirav.joshi" % srcpath
    oscmd = "scp %s nirav.joshi@108.168.207.6:/home/nirav.joshi" % srcpath
    os.system(oscmd)




if __name__ == '__main__':

    DecompressBZ2files()
    MariaDBRestore()
