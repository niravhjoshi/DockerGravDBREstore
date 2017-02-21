import os
import fileinput
import sys
import glob
import bz2
from bz2 import decompress
import tarfile






def MariaDBRestore():
    #/Users/nirav/mariadb/conf/
    print "scp %s nirav.joshi@108.168.207.6:/home/nirav.joshi"
    oscmd1 = "docker exec -it mariadb mysql -uroot -pgravitant < DroPDB.sql "
    os.system(oscmd1)
    oscmd2 = "docker exec -it mariadb mysql -uroot -pgravitant < CreateDB.sql "
    #os.system(oscmd2)
    oscmd2 = "docker exec -it mariadb mysql -uroot -pgravitant < CreateDB.sql "
    # os.system(oscmd2)
    oscmd2 = "docker exec -it mariadb mysql -uroot -pgravitant < CreateDB.sql "
    # os.system(oscmd2)


def DecompressFiles():

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
            break
        else:
            print "Directory already there"
            decompath = str(user_DecomDir)
            newfile_name = file_name[0:-8]
            print newfile_name
            myfile_name= "db_dump"
            outfile_path = os.path.join(decompath + "/",myfile_name)
            inputfile_path = os.path.join(file_name)
            print outfile_path
            print inputfile_path
            tar = tarfile.open(inputfile_path, "r:bz2")
            tar.extractall(path=outfile_path)
            tar.close()

            print "Decmpression has been done for %s " % (decompath)
            break




if __name__ == '__main__':

    MariaDBRestore()
    DecompressFiles()

