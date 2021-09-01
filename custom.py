from os import listdir
import os.path 
import time

hassettings = os.path.exists('savesettings.archiversettings')
wantsToContinue=True

def YesNoQuestion(question):
	answ = input(question)
	if(answ in ["Y","y","YES","Yes","yes","True","true","TRUE"]):
		return True
	else: 
		return False

def CheckYesNoValue(value):
	if(value in ["Y","y","YES","Yes","yes","True","true","TRUE"]):
		return True
	else: 
		return False

if (not hassettings):
	#no settings found
	print("Looks like you have not created a settings file yet.")
	wantsToContinue = YesNoQuestion("Would you like to create it? (Y/N): ")


	if (wantsToContinue):

		#create SETTINGS file
		fh=open("savesettings.archiversettings","x+",encoding="UTF-8")
		

		tpath = input("Enter full path of folder: ")
		if (tpath == "" or tpath == None or len(tpath) <= 0):
			print("[ERROR] Can't be blank.")
			quit()
		#save value to file
		fh=open("savesettings.archiversettings","w+",encoding="UTF-8")
		fh.write("path="+tpath)
		mypath = tpath
		#ask for extra files 
		wantsextrafiles = YesNoQuestion("Do you want extra files to be classified as well? (Y/N): ")

		if wantsextrafiles:
			print("[SETTINGS] Extra Files Folder Creation Enabled ")
		else: 
			print("[SETTINGS] Extra Files Folder Creation Disabled ")
		fh.write("\nWantsExtraFiles="+str(wantsextrafiles))

		#ask more things
		answlog = YesNoQuestion("Do you want to log all organized files? (Y/N): ")
		fh.write("\nLog="+str(answlog))
		wantsTolog = answlog
		if(answlog):
			print("[SETTINGS] Log Enabled")
		else:
			print("[SETTINGS] Log Disabled")

if (hassettings):
	#settings detected
	print("[OK] Settings File Found")
	#read settings
	fh=open("savesettings.archiversettings","r+",encoding="UTF-8")
	mypath = fh.readline().strip()[len("path="):]

	wantsextrafiles = CheckYesNoValue(fh.readline().strip()[len("WantsExtraFiles="):])
	
	if(wantsextrafiles):
		print("[SETTINGS] Extra Files Folder Creation Enabled ")
	else: 
		print("[SETTINGS] Extra Files Folder Creation Disabled ")

	wantsTolog = CheckYesNoValue(fh.readline().strip()[len("Log="):])
	if(wantsTolog):
		print("[SETTINGS] Log Enabled ")
	else: 
		print("[SETTINGS] Log Disabled ")

if(not wantsToContinue): 
	#don't want to save settings
	mypath = input("Enter the full path of the folder you want to organize:")
	if (mypath == "" or mypath == None or len(mypath) <= 0): 
		print("[ERROR] Can't be blank.") 
		quit()



existsmypath = os.path.exists(mypath)

if(not existsmypath):
	print("[ERROR] Configuration File Corrupted. Or data invalid")
	answ = YesNoQuestion("Would you like to delete it? (Y/N): ")
	if(not answ): quit()

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
	
	newpath = temppath+nameDir
	if not os.path.exists(newpath):
		os.makedirs(newpath)
		if(wantsTolog):
			print("[LOG] New Folder Created:",newpath)

def moveFile(path):
	os.replace(data[file][1],path)
	if(wantsTolog):
		print("[LOG] File Moved OLD PATH=",data[file][1],"\n"+17*" "+"NEW PATH=",path)
#create folder
#get extensions

for file in data:
	exception = True
	extension = os.path.splitext(file)[1]
	if(file in ["desktop.ini", "custom.py", "oneclick.py", "savesettings.archiversettings"] or file.endswith(".ini") or file.lower().endswith(".dat")): continue
	if (extension in [".exe", ".msi"]):
		exeDir = "executables/"
		createDir(mypath,exeDir)
		moveFile(mypath+exeDir+file)
		exception = False

	if (extension in [".png", ".img", ".jpg", ".jpeg", ".HEIC", ".gif", ".svg", ".webp"]):
		imgDir = "images/"
		createDir(mypath,imgDir)
		moveFile(mypath+imgDir+file)
		exception = False
		
	if (extension in [".mp4", ".mov"]):
		videoDir = "videos/"
		createDir(mypath,videoDir)
		moveFile(mypath+videoDir+file)
		exception = False

	if (extension in [".wav", ".mp3", ".ogg", ".aac", ".m4a"]):
		audioDir = "audios/"
		createDir(mypath,audioDir)
		moveFile(mypath+audioDir+file)
		exception = False

	if (extension in [".stl", ".obj"]):
		threedDir = "3dFiles/"
		createDir(mypath,threedDir)
		moveFile(mypath+threedDir+file)
		exception = False

	if (extension in [".rar", ".zip", ".7z", ".tar", ".rar5"]):
		zipDir = "compressed/"
		createDir(mypath,zipDir)
		moveFile(mypath+zipDir+file)
		exception = False

	if (extension in [".txt", ".md"]):
		txtDir = "notepad/"
		createDir(mypath,txtDir)
		moveFile(mypath+txtDir+file)
		exception = False

	if (extension in [".jar", ".schematic", ".schem"]):
		mcDir = "minecraft/"
		createDir(mypath,mcDir)
		moveFile(mypath+mcDir+file)
		exception = False

	if (extension in [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".csv"]):
		docDir = "documents/"
		createDir(mypath,docDir)
		moveFile(mypath+docDir+file)
		exception = False

	if (extension in [".skp"]):
		sketchup = "sketchup/"
		createDir(mypath,sketchup)
		moveFile(mypath+sketchup+file)
		exception = False

	if (extension in [".html"]):
		htmlDir = "htmls/"
		createDir(mypath,htmlDir)
		moveFile(mypath+htmlDir+file)
		exception = False

	if (extension in [".psd"]):
		psdDir = "psd/"
		createDir(mypath,psdDir)
		moveFile(mypath+psdDir+file)
		exception = False

	if (extension in [".torrent"]):
		torrentDir = "torrents/"
		createDir(mypath,torrentDir)
		moveFile(mypath+torrentDir+file)
		exception = False

	if (extension in [".bsdesign"]):
		bs4design = "bs4design/"
		createDir(mypath,bs4design)
		moveFile(mypath+bs4design+file)
		exception = False

	if (extension in [".log"]):
		logDir = "logs/"
		createDir(mypath,logDir)
		moveFile(mypath+logDir+file)
		exception = False

	if (extension in [".log"]):
		logDir = "logs/"
		createDir(mypath,logDir)
		moveFile(mypath+logDir+file)
		exception = False

	if (extension in [".ovpn"]):
		ovpnDir = "ovpn/"
		createDir(mypath,ovpnDir)
		moveFile(mypath+ovpnDir+file)
		exception = False

	if (exception):
		valuePoint = file.rfind(".")
		if(valuePoint):
			if (wantsextrafiles):
				extrafile = file[valuePoint+1:]+"/"
				createDir(mypath,extrafile)
				moveFile(mypath+extrafile+file)
			else:
				print("[EXCEPTION] Extension not ordered:",file[valuePoint+1:])
print("[OK] Directory succesfully organized")