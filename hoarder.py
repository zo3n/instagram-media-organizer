import os
import getpass

g_User = getpass.getuser()
g_Path = "C:\\Users\\" + g_User + "\\Downloads\\"

g_Extensions = {
    ".mp4",
    ".png",
    ".jpg",
    ".jpeg",
}

g_Files = os.listdir(g_Path)
g_MoveList = {}

def RefreshFiles():
    global g_Files
    g_Files = os.listdir(g_Path)


def IsMediaFile(filename):
    for ext in g_Extensions:
        foundExt = filename[len(filename) - len(ext):]
        if foundExt == ext:
            return True

    return False

def FindOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def FindMoveList():
    for filename in g_Files:
        if IsMediaFile(filename):

            occurences = FindOccurrences(filename, "_")

            # If its an instagram/facebook file, it must have at least four _'s and _n in name

            if (len(occurences) >= 2) and (filename.find("_n") != -1):
                folderName = filename[ : occurences[ len(occurences) - 4 ] ]
                if not g_MoveList.get(folderName):
                    g_MoveList[folderName] = [filename]
                else:
                    g_MoveList[folderName].append(filename)




def main():
    
    FindMoveList()
    
    os.system("@echo off")
    
    # Some program (visual) settings
    os.system("color a")
    os.system("title hoarder")

    # Make profiles folder in Downloads folder
    os.chdir(g_Path)
    os.system("mkdir profiles")

    # Move to profiles directory now
    os.chdir(g_Path + "\\profiles\\")
    movedNum = 0

    # Make sure all profile folders exist
    for folderName, filename in g_MoveList.items():
        os.system("mkdir " + folderName)

    # Move all media to their profile folders
    for folderName, folderList in g_MoveList.items():
        for filename in folderList:
            os.chdir(g_Path)
            os.system('move "' + filename + '" "' + (g_Path + "\\profiles\\" + folderName + "\\") + '"')
            movedNum += 1

    print("Done. Moved " + str(movedNum) + " files.")
        


main()
