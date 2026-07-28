########################################################
#
# File Name : DuplicateCodeLogic.py
# Description : Find and Delete Duplicate Files
# Author : Sachin Nemaram Patel
#
########################################################

import os
import hashlib

def CalculateCheckSum(FileName):

    try:

        if(os.path.exists(FileName) == False):
            return None

        if(os.path.isfile(FileName) == False):
            return None

        if(os.access(FileName, os.R_OK) == False):
            return None

        fobj = open(FileName, "rb")

        hobj = hashlib.md5()

        Buffer = fobj.read(1024)

        while(len(Buffer) > 0):

            hobj.update(Buffer)

            Buffer = fobj.read(1024)

        fobj.close()

        return hobj.hexdigest()

    except Exception:

        return None


def FindDuplicate(DirectoryName):

    Duplicate = {}

    try:

        if(os.path.exists(DirectoryName) == False):
            print("It does not exists this type of directory with the name of : ",DirectoryName)
            return None

        if(os.path.isdir(DirectoryName) == False):
            print("Invali Directory or Invalid Path of Directory")
            return None

        for FolderName, SubFolder, FileName in os.walk(DirectoryName):

            for fname in FileName:

                FilePath = os.path.join(FolderName, fname)

                CheckSum = CalculateCheckSum(FilePath)

                if(CheckSum == None):
                    continue

                if(CheckSum in Duplicate):
                    Duplicate[CheckSum].append(FilePath)
                else:
                    Duplicate[CheckSum] = [FilePath]

        return Duplicate

    except Exception:

        return None

def DeleteDuplicate(DirectoryName, fobj):

    MyDict = FindDuplicate(DirectoryName)

    if(MyDict == None):
        return 0, 0

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    DuplicateFound = 0
    DuplicateDeleted = 0

    fobj.write("Duplicate File Details\n")
    fobj.write("-" * 60 + "\n\n")

    for value in Result:

        CheckSum = CalculateCheckSum(value[0])

        fobj.write("Checksum : " + str(CheckSum) + "\n")

        Count = 0

        for FileName in value:

            DuplicateFound = DuplicateFound + 1

            if(Count == 0):

                fobj.write("Original File : " + FileName + "\n")

            else:

                try:

                    if(os.path.exists(FileName) == False):

                        fobj.write("File Not Found : " + FileName + "\n")
                        continue

                    if(os.path.isfile(FileName) == False):

                        fobj.write("Not a Regular File : " + FileName + "\n")
                        continue

                    if(os.access(FileName, os.W_OK) == False):

                        fobj.write("Permission Denied : " + FileName + "\n")
                        continue

                    os.remove(FileName)

                    DuplicateDeleted = DuplicateDeleted + 1

                    fobj.write("Deleted File : " + FileName + "\n")

                except PermissionError as e:

                    fobj.write("Permission Error : " + str(e) + "\n")

                except Exception as e:

                    fobj.write("Error : " + str(e) + "\n")

            Count = Count + 1

        fobj.write("-" * 60 + "\n")

    return DuplicateFound, DuplicateDeleted
