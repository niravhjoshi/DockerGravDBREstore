import os
import fileinput
import sys
import glob
import bz2
from bz2 import decompress
import tarfile

# Mac Static Variable
githubrepo = "https://github.com/niravhjoshi/DockerGravDBREstore.git"
DropDBSQL = "/root/DockerGravDBREstore/DroPDB.sql"
CreateDBSQL="/root/DockerGravDBREstore/CreateDB.sql"
UpdateBTSSQL="/Users/nirav/mariadb/conf/DockerGravDBREstore/UpdateBTS.sql"
global filelist
'''
# Linux Docker variable
githubrepo = "https://github.com/niravhjoshi/DockerGravDBREstore.git"
DropDBSQL = "/root/mariadb/conf/DockerGravDBREstore/DroPDB.sql"
CreateDBSQL="/root/mariadb/conf/DockerGravDBREstore/CreateDB.sql"
#UpdateBTSSQL="/Users/nirav/mariadb/conf/DockerGravDBREstore/UpdateBTS.sql"
global filelist
'''


def getGitRepo():
    os.chdir("/Users/nirav/mariadb/conf")
    oscmd0 = "git clone %s" % githubrepo

    if os.system(oscmd0) != 0:
        print("git clone is failed some how")
    os.chdir("/Users/nirav/mariadb/conf/DockerGravDBREstore")
    print 'git clone failed try with Pull'
    osgitpull = "git pull"
    os.system(osgitpull)
    print "Cloning of reposiotry is done"

#Restoration of database.
def MariaDBRestore():
    #/Users/nirav/mariadb/conf/
    while True:

        rootpw= raw_input("Please enter root password for your docker instance or check in $GRAV/conf:->")
        if rootpw == '':
            rootpw='gravitant'
        break
    oscmd1 = '/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0}<{1}'.format(rootpw,DropDBSQL)
    #oscmd1 = "/usr/local/bin/docker ps"
    os.system(oscmd1)

    oscmd2 = '/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0}<{1}'.format(rootpw,CreateDBSQL)
    os.system(oscmd2)
    print iterpath

    #    if filesname.find('softlayer') != -1:

    for filesname in glob.glob(iterpath):
        if '_bts.' in filesname:
            oscmd3 = '/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} bts < {1}'.format(rootpw,filesname)
            os.system(oscmd3)
            print "restore done for bts"
            break

    for filesname in glob.glob(iterpath):
        if '_tags.' in filesname:
            oscmd4='/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} tags <{1}'.format(rootpw,filesname)
            os.system(oscmd4)
            print "restore done for tags"
            break

    for filesname in glob.glob(iterpath):
        if '_cme.' in filesname:
            oscmd5 = '/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} cme <{1}'.format(rootpw,filesname)
            os.system(oscmd5)
            print "restore done for cme"
            break

    for filesname in glob.glob(iterpath):
        if '_sds.' in filesname:
            oscmd6 = '/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} sds <{1}'.format(rootpw,filesname)
            os.system(oscmd6)
            print "restore done  for sds"
            break

    for filesname in glob.glob(iterpath):
        if '_sfb.' in filesname:
            oscmd8 = "/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} sfb <{1}".format(rootpw,filesname)
            os.system(oscmd8)
            print "restore done for sfb"
            break

    for filesname in glob.glob(iterpath):
        if '_softlayer.' in filesname:
            oscmd9 = "/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} softlayer <{1}".format(rootpw,filesname)
            os.system(oscmd9)
            print "restore done for softlayer"
            break

    for filesname in glob.glob(iterpath):
        if '_demo.' in filesname:
            oscmd10 = "/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} demo <{1}".format(rootpw,filesname)
            os.system(oscmd10)
            print "restore done for demo"
            break

    for filesname in glob.glob(iterpath):
        if '_pyscreener.' in filesname:
            oscmd11 = "/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} pyscreener <{1}".format(rootpw,filesname)
            os.system(oscmd11)
            print "restore done for pyscreener"
            break

    for filesname in glob.glob(iterpath):
        if '_comparedb.' in filesname:
            oscmd11 = "/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} comparedb <{1}".format(rootpw,filesname)
            os.system(oscmd11)
            print "restore done for comparedb"
            break

    for filesname in glob.glob(iterpath):
        if '_ods.' in filesname:
            oscmd7 = "/usr/local/bin/docker exec -i mariadb mysql -uroot -p{0} ods <{1}".format(rootpw,filesname)
            os.system(oscmd7)
            print "restore done for ods"
            break


    #oscmd12 = "/usr/local/bin/docker exec -i mariadb mysql -uroot -pgravitant < %s" % UpdateBTSSQL
    #os.system(oscmd12)
    print "DB Restore completed fine and update also ran"


def DecompressFiles():
    global iterpath
    # Add File where you have dump your bz2 database backup.
    while True:
        user_dirInput = raw_input("Please enter your bz2 database backup location(Default will be /root/DBDrop/:->")
        if user_dirInput == '':
            user_dirInput = '/Users/nirav/Desktop/MariaDBRestore/'
        if os.path.exists(user_dirInput) is False:
            print "I could not find that path in your file system please ensure it is correct!!! " +str(user_dirInput)
            continue
        else:
            pathcompressfile = str(user_dirInput)
            print "please select your file name to be extracted:"
            print glob.glob(user_dirInput+'*')
            filelist= glob.glob(user_dirInput+'*')
            j = len(filelist)
            i=0
            while True:
                print 'File Number---> %d and File Name ----> %s' %(i,filelist[i])
                i =i+1
                if i>=j:
                    break

            file_no=raw_input("Please enter your file number which you want to extract:->")
            file_no = int(file_no)
            file_name = filelist[file_no]

            print "You have selected ----->%s" %(file_name)
            print filelist
            break

    #Please enter decompress path for your bz2 file if it is not there create it.
    while True:
        user_DecomDir = raw_input("Please enter path or location where you want to decompress files:->")
        if user_DecomDir == '':
            user_DecomDir = '/Users/nirav/Desktop/MariaDBRestore/DecomFiles/'
        if os.path.exists(user_DecomDir) is False:
            os.makedirs(user_DecomDir)
            print "New Dir is created at following location" +str(user_DecomDir)
            decompath = str(user_DecomDir)
            print "Directory is Now Created there"
            decompath = str(user_DecomDir)
            newfile_name = file_name[0:-8]
            print newfile_name
            myfile_name = "db_dump"
            outfile_path = os.path.join(decompath, myfile_name)
            inputfile_path = os.path.join(file_name)
            print outfile_path
            print inputfile_path
            tar = tarfile.open(inputfile_path, "r:bz2")
            tar.extractall(path=outfile_path)
            tar.close()
            print "Decmpression has been done for %s " % (decompath)
            iterpath = (outfile_path + '/*.sql')
            break

        else:
            print "Directory already there"
            decompath = str(user_DecomDir)
            newfile_name = file_name[0:-8]
            print newfile_name
            myfile_name= "db_dump"
            outfile_path = os.path.join(decompath ,myfile_name)
            inputfile_path = os.path.join(file_name)
            print outfile_path
            print inputfile_path
            tar = tarfile.open(inputfile_path, "r:bz2")
            tar.extractall(path=outfile_path)
            tar.close()

            print "Decmpression has been done for %s " % (decompath)
            iterpath = (outfile_path+'/*.sql')


            break
    print iterpath

def MariaDBBackup():
    print "Backing up mariaDB"


if __name__ == '__main__':
    #getGitRepo()
    DecompressFiles()
    MariaDBRestore()
    #MariaDBBackup()

