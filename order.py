from os import listdir
import os.path 
import time
mypath = "C:/Users/IBM/Downloads/"
stuff = listdir(mypath)
data = {}


for element in stuff:
	path = mypath+element
	if (os.path.isfile(path)):
		ti_c = os.path.getctime(path)
		ti_m = os.path.getmtime(path)
		
		# Converting the time in seconds to a timestamp
		c_ti = time.ctime(ti_c)
		m_ti = time.ctime(ti_m)
		data[element] = [mypath,path,ti_c,ti_m]
	else:
		#is dir
		a = 1

#core funct
def createDir(temppath,nameDir):
	globals()[exception] = False
	newpath = temppath+nameDir
	if not os.path.exists(newpath):
		os.makedirs(newpath)

def moveFile(path):
	os.replace(data[file][1],path)
#create folder
#get extensions
exception = True

for file in data:
	if(file == "desktop.ini" or file.endswith(".ini") or file.lower().endswith(".DAT")): continue
	if file.endswith(".exe") or file.endswith(".msi"):
		exeDir = "executables/"
		createDir(mypath,exeDir)
		moveFile(mypath+exeDir+file)

	if file.endswith(".png") or file.endswith(".img") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".HEIC") or file.endswith(".gif") or file.endswith(".svg") or file.endswith(".webp"):
		imgDir = "images/"
		createDir(mypath,imgDir)
		moveFile(mypath+imgDir+file)
		
	if file.endswith(".mp4") or file.endswith(".mov"):
		videoDir = "videos/"
		createDir(mypath,videoDir)
		moveFile(mypath+videoDir+file)

	if file.endswith(".wav") or file.endswith(".mp3") or file.endswith(".ogg") or file.endswith(".aac") or file.endswith(".m4a"):
		audioDir = "audios/"
		createDir(mypath,audioDir)
		moveFile(mypath+audioDir+file)

	if file.endswith(".stl") or file.endswith(".obj"):
		threedDir = "3dFiles/"
		createDir(mypath,threedDir)
		moveFile(mypath+threedDir+file)

	if file.endswith(".rar") or file.endswith(".zip") or file.endswith(".7z") or file.endswith(".tar") or file.endswith(".rar5"):
		zipDir = "compressed/"
		createDir(mypath,zipDir)
		moveFile(mypath+zipDir+file)

	if file.endswith(".txt") or file.endswith(".md"):
		txtDir = "notepad/"
		createDir(mypath,txtDir)
		moveFile(mypath+txtDir+file)

	if file.endswith(".jar") or file.endswith(".schematic") or file.endswith(".schem"):
		mcDir = "minecraft/"
		createDir(mypath,mcDir)
		moveFile(mypath+mcDir+file)

	if file.endswith(".pdf") or file.endswith(".doc") or file.endswith(".docx") or file.endswith(".ppt") or file.endswith(".pptx") or file.endswith(".xls") or file.endswith(".csv"):
		docDir = "documents/"
		createDir(mypath,docDir)
		moveFile(mypath+docDir+file)

	if file.endswith(".skp"):
		sketchup = "sketchup/"
		createDir(mypath,sketchup)
		moveFile(mypath+sketchup+file)

	if file.endswith(".html"):
		htmlDir = "htmls/"
		createDir(mypath,htmlDir)
		moveFile(mypath+htmlDir+file)

	if file.endswith(".psd"):
		psdDir = "psd/"
		createDir(mypath,psdDir)
		moveFile(mypath+psdDir+file)

	if file.endswith(".torrent"):
		torrentDir = "torrents/"
		createDir(mypath,torrentDir)
		moveFile(mypath+torrentDir+file)

	if file.endswith(".bsdesign"):
		bs4design = "bs4design/"
		createDir(mypath,bs4design)
		moveFile(mypath+bs4design+file)

	if file.endswith(".log"):
		logDir = "logs/"
		createDir(mypath,logDir)
		moveFile(mypath+logDir+file)

	if file.endswith(".log"):
		logDir = "logs/"
		createDir(mypath,logDir)
		moveFile(mypath+logDir+file)

	if file.endswith(".ovpn"):
		ovpnDir = "ovpn/"
		createDir(mypath,ovpnDir)
		moveFile(mypath+ovpnDir+file)

	if (exception):
		valuePoint = file.find(".")
		if(valuePoint):
			print("Extension not ordered:",file[valuePoint+1:])