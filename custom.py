from os import listdir
import os.path 
import time

hassettings = os.path.exists('savesettings.archiversettings')
wantsToContinue=True

if (not hassettings):
	print("Looks like you have not settings saved yet.")
	answ = input("Would you like to create them? (Y/N): ")
	if (answ not in ["Y","y","N","n"]): 
		print("Didn't undestand you. Please answer with Y (yes) or N (not)")
		quit()
	
	if (answ in ["N","n"]): wantsToContinue=False

	if (wantsToContinue):
		#create file
		fh=open("savesettings.archiversettings","x+",encoding="UTF-8")
		

		tpath = input("Enter full path of folder: ")
		if (tpath == "" or tpath == None or len(tpath) <= 0):
			print("[ERROR] Can't be blank.")
			quit()
		#save value to file
		fh=open("savesettings.archiversettings","w+",encoding="UTF-8")
		fh.write("path="+tpath)
		#ask for extra files 
		efiles = input("Do you want extra files to be classified as well? (Y/N): ")
		if (efiles == "" or efiles == None or len(efiles) <= 0): 
			print("[ERROR] Can't be blank.")
			quit()
		fh.write("\nWantsExtraFiles="+efiles)

		#ask more things


if (hassettings):
	print("[OK] Settings File Found")
	#read settings
	fh=open("savesettings.archiversettings","r+",encoding="UTF-8")
	mypath = fh.readline().strip()[len("path="):]

	wantsextrafiles = fh.readline().strip()[len("WantsExtraFiles="):]

	if(wantsextrafiles in ["Y","y","YES","Yes","yes","True","true","TRUE"]):
		wantsextrafiles = True
		print("[SETTINGS] Enabled Extra Files Folder Creation")
	else: 
		wantsextrafiles = False
		print("[SETTINGS] Disabled Extra Files Folder Creation")

if(not wantsToContinue): 

	mypath = input("Enter full path of folder:")
	if (mypath == "" or mypath == None or len(mypath) <= 0): 
		print("[ERROR] Can't be blank.") 
		quit()




existsmypath = os.path.exists(mypath)

if(not existsmypath):
	print("[ERROR] Configuration File Corrupted. Or data invalid")
	answ = input("Would you like to delete it? (Y/N): ")
	if (answ not in ["Y","y","N","n"]): 
		print("Didn't undestand you. Please answer with Y (yes) or N (not)")
		quit()
	
	if (answ in ["N","n"]): quit()

	fh.close()
	os.remove("savesettings.archiversettings")
	print("Removed!")
	quit()
else: 
	print("[SETTINGS] Organizing folder:",mypath)


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
			if (wantsextrafiles):
				extrafile = file[valuePoint+1:]+"/"
				createDir(mypath,extrafile)
				moveFile(mypath+extrafile+file)
			else:
				print("[EXCEPTION] Extension not ordered:",file[valuePoint+1:])
print("[OK] Directory succesfully organized")