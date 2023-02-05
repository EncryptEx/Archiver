from os import listdir
import os.path
import time

mypath = input("Enter full path of folder:")
if mypath == "" or mypath is None:
    # reminder: always add / at the end
    mypath = "C:/Users/IBM/Downloads/"

stuff = listdir(mypath)
data = {}


for element in stuff:
    path = mypath + element
    if os.path.isfile(path):
        ti_c = os.path.getctime(path)
        ti_m = os.path.getmtime(path)

        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)
        m_ti = time.ctime(ti_m)
        data[element] = [mypath, path, ti_c, ti_m]


def createDir(temppath, nameDir):
    globals()[exception] = False
    newpath = temppath + nameDir
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def moveFile(path):
    os.replace(data[file][1], path)


def checkExtensions(*extensions):
    return sum(map(lambda x: int(checked_file.endswith(x)), extensions)) > 0


exception = True

for file in data:
    checked_file = file.lower()
    if checked_file == "desktop.ini" or checkExtensions(".ini", ".dat"):
        continue
    if checkExtensions(".exe", ".msi"):
        exeDir = "executables/"
        createDir(mypath, exeDir)
        moveFile(mypath + exeDir + file)
        continue

    if checkExtensions(
        ".png", ".img", ".jpg", ".jpeg", ".HEIC", ".gif", ".svg", ".webp"
    ):
        imgDir = "images/"
        createDir(mypath, imgDir)
        moveFile(mypath + imgDir + file)
        continue

    if checkExtensions(".mp4", ".mov"):
        videoDir = "videos/"
        createDir(mypath, videoDir)
        moveFile(mypath + videoDir + file)
        continue

    if checkExtensions(".wav", ".mp3", ".ogg", ".aac", ".m4a"):
        audioDir = "audios/"
        createDir(mypath, audioDir)
        moveFile(mypath + audioDir + file)
        continue

    if checkExtensions(".stl", ".obj"):
        threedDir = "3dFiles/"
        createDir(mypath, threedDir)
        moveFile(mypath + threedDir + file)
        continue

    if checkExtensions(".rar", ".zip", ".7z", ".tar", ".rar5"):
        zipDir = "compressed/"
        createDir(mypath, zipDir)
        moveFile(mypath + zipDir + file)
        continue

    if checkExtensions(".txt", ".md"):
        txtDir = "notepad/"
        createDir(mypath, txtDir)
        moveFile(mypath + txtDir + file)
        continue

    if checkExtensions(".jar", ".schematic", ".schem"):
        mcDir = "minecraft/"
        createDir(mypath, mcDir)
        moveFile(mypath + mcDir + file)
        continue

    if checkExtensions(".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".csv"):
        docDir = "documents/"
        createDir(mypath, docDir)
        moveFile(mypath + docDir + file)
        continue

    if checkExtensions(".skp"):
        sketchup = "sketchup/"
        createDir(mypath, sketchup)
        moveFile(mypath + sketchup + file)
        continue

    if checkExtensions(".html"):
        htmlDir = "htmls/"
        createDir(mypath, htmlDir)
        moveFile(mypath + htmlDir + file)
        continue

    if checkExtensions(".psd"):
        psdDir = "psd/"
        createDir(mypath, psdDir)
        moveFile(mypath + psdDir + file)
        continue

    if checkExtensions(".torrent"):
        torrentDir = "torrents/"
        createDir(mypath, torrentDir)
        moveFile(mypath + torrentDir + file)
        continue

    if checkExtensions(".bsdesign"):
        bs4design = "bs4design/"
        createDir(mypath, bs4design)
        moveFile(mypath + bs4design + file)
        continue

    if checkExtensions(".log"):
        logDir = "logs/"
        createDir(mypath, logDir)
        moveFile(mypath + logDir + file)
        continue

    if checkExtensions(".log"):
        logDir = "logs/"
        createDir(mypath, logDir)
        moveFile(mypath + logDir + file)
        continue

    if checkExtensions(".ovpn"):
        ovpnDir = "ovpn/"
        createDir(mypath, ovpnDir)
        moveFile(mypath + ovpnDir + file)
        continue

    if exception:
        valuePoint = file.find(".")
        if valuePoint:
            print("Extension not ordered:", file[valuePoint + 1:])
