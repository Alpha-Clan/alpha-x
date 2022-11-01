import os 
import webbrowser
import time

def mainmenu():
	print("")
	print("<== = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ==>")
	print("")
	print("Choose the below given action you want to execute...")

	print("""
	1. Update Your Linux System
	2. Search for the available software
	3. Install Software or tool
	4. Remove Software or tool
	5. Scanning For ports - NMAP
	6. Important Apps
	7. Information Gathering - INFO-X
	8. View your Network Informations
	9. Quit Alpha - X
	""")
	tools()

def tools():
	u_inp="0"
	u_inp=input("[+]Enter The Tool Number to be executed:")
	if u_inp=="1":
	    os.system("sudo apt update")
	    os.system("apt list --upgradable")
	    upgrade()
	elif u_inp=="2":
	    pkgs = input("[+]Enter the Software or Tool Name to Search: ")
	    A = "sudo apt-cache search " + pkgs
	    os.system(A)
	elif u_inp=="3":
	    pkgi = input("[+]Enter the package to Install (ex: vlc) : ")
	    B = "sudo apt-get install " + pkgi
	    os.system(B)  
	elif u_inp=="4":
	    pkgr = input("[+]Enter the package to Remove (ex: vlc) : ")
	    C = "sudo apt-get remove " + pkgr
	    os.system(C)
	elif u_inp=="5":
	    IP = input("[+]Enter the target IP: ")
	    M="nmap "+ IP
	    os.system(M)
	elif u_inp=="6":
	    apps()
	elif u_inp=="7":
	    info_x()
	elif u_inp=="8":
	    os.system("ifconfig")
	elif u_inp=="9":
	    print("***********************************************")
	    print("")
	    print("Quiting... ThankYou for Using our ALPHA - X...!")
	    print("")
	    print("***********************************************")
	    quit()
	else:
	    print("")
	    print("Please enter valid Tool Number!")
	    tools()
	    
#######app Installation #######
###############################

def apps():
	print("""
	1. Google Chrome
	2. Telegram
	3. Libre Office
	4. Brave Browser
	5. Wikit
	6. VLC
	7. Stream
	8. Quit App Installation
	""")
	appinstall()
	aconf()
	
	
def appinstall():
	a_inp="0"
	a_inp=input("[+]Enter The Tool Number to be executed:")
	
	if a_inp == "1":
		os.system("sudo apt update")
		os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
		os.system("sudo apt install ./google-chrome-stable_current_amd64.deb")
		print("*************************************************")
		print("")
		print("   Google Chrome is Successfully Installed....")
		print("")
		print("*************************************************")
	elif a_inp == "2":
		os.system("sudo apt-get install telegram-desktop")
		print("*************************************************")
		print("")
		print("    Telegram is Successfully Installed....")
		print("")
		print("*************************************************")
	elif a_inp == "3":
		os.system("sudo apt-get install libreoffice")
		print("*************************************************")
		print("")
		print("   Libre-Office is Successfully Installed....")
		print("")
		print("*************************************************")
	elif a_inp == "4":
		os.system("""
		
		sudo apt install apt-transport-https curl

		sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg

		echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list

		sudo apt update
		
		""")
		os.system("sudo apt install brave-browser")
		print("*************************************************")
		print("")
		print("   Brave Browser is Successfully Installed....")
		print("")
		print("*************************************************")
		
	elif a_inp == "5":
		os.system("sudo apt install nodejs npm && sudo npm install wikit -g ")
		
		print("*************************************************")
		print("")
		print("   Wikit is Successfully Installed....")
		print("")
		print("*************************************************")
	elif a_inp == "6":
		os.system("sudo apt-get install vlc")
		print("*************************************************")
		print("")
		print(" VLC Media Player is Successfully Installed....")
		print("")
		print("*************************************************")
	elif a_inp == "7":
		os.system("sudo apt install steam")
		print("*************************************************")
		print("")
		print("   Steam is Successfully Installed....")
		print("")
		print("*************************************************")
	elif a_inp == "8":
		print("***********************************************")
		print("")
		print("Quiting... ThankYou for Using our App Installation...!")
		print("")
		print("***********************************************")
		mainmenu()
		conformation()
	else:
	    print("")
	    print("Please enter valid Tool Number!")
	    appinstall()


def aconf():
	print("")
	print("")
	loop = input("[+]Do you want to continue with App Installation? (Y/N) ")
	
	if loop=="Y" or loop == "y":
	    #os.system('clear')
	    apps()
	elif loop=="N" or loop == "n":
	    print("****************************************")
	    print("")
	    print("           Entering ALPHA - X....!")
	    print("")
	    print("****************************************")
	    mainmenu()
	    conformation()
	else:
	    print("Enter the Valid Input")
	    aconf()	    
	    
#######app Installation END #######
###################################	
	    
def upgrade():
	print("")
	print("")
	a=input("Do you want to upgrade the above mentioned Packages?(Y/N):")  
	if a=="Y" or a == "y":
	    #os.system('clear')
	    os.system("sudo apt autoremove")
	    os.system("sudo apt full-upgrade -y")
	    print("****************************************")
	    print("")
	    print("Your System is Succussfully UPDATED....")
	    print("")
	    print("****************************************")
	elif a=="N" or a=="n":
	    mainmenu()
	else:
	    print("Enter the Valid Input")
	    upgrade() 
	    
def alpha_x():
	os.system('clear')
	print("********************************************************************************")
	print("")
	print("""
	 $$$$$$\  $$\       $$$$$$$\  $$\   $$\  $$$$$$\                      $$\   $$\ 
	$$  __$$\ $$ |      $$  __$$\ $$ |  $$ |$$  __$$\                     $$ |  $$ |
	$$ /  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ /  $$ |                    \$$\ $$  |
	$$$$$$$$ |$$ |      $$$$$$$  |$$$$$$$$ |$$$$$$$$ |      $$$$$$\        \$$$$  / 
	$$  __$$ |$$ |      $$  ____/ $$  __$$ |$$  __$$ |      \______|       $$  $$<  
	$$ |  $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |                    $$  /\$$\ 
	$$ |  $$ |$$$$$$$$\ $$ |      $$ |  $$ |$$ |  $$ |                    $$ /  $$ |
	\__|  \__|\________|\__|      \__|  \__|\__|  \__|                    \__|  \__|
	""")
	print("") 
	print("********************************************************************************")
	print("")
	print("Hi! Welcome to Our ALPHA - X....")
	print("")
	print("********************************************************************************")
	print("")
	mainmenu()
	    
def conformation():
	print("")
	print("")
	loop = input("[+]Do you want to continue with ALPHA - X? (Y/N) ")
	
	
	if loop=="Y" or loop == "y":
	    #os.system('clear')
	    mainmenu()
	    conformation()
	elif loop=="N" or loop == "n":
	    print("****************************************")
	    print("")
	    print("ThankYou for Using our ALPHA - X....!")
	    print("")
	    print("****************************************")
	    quit()
	else:
	    print("Enter the Valid Input")
	    conformation()
		

###INFO-X starts###
###################

def info_x():
	print("")
	print("********************************************************************************")
	print("")
	print("""
	$$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\         $$\   $$\ 
	\_$$  _|$$$\  $$ |$$  _____|$$  __$$\        $$ |  $$ |
	  $$ |  $$$$\ $$ |$$ |      $$ /  $$ |       \$$\ $$  |
	  $$ |  $$ $$\$$ |$$$$$\    $$ |  $$ |$$$$$$\ \$$$$  / 
	  $$ |  $$ \$$$$ |$$  __|   $$ |  $$ |\______|$$  $$<  
	  $$ |  $$ |\$$$ |$$ |      $$ |  $$ |       $$  /\$$\ 
	$$$$$$\ $$ | \$$ |$$ |       $$$$$$  |       $$ /  $$ |
	\______|\__|  \__|\__|       \______/        \__|  \__|
	""")
	print("") 
	print("********************************************************************************")
	print("")
	print("Hi! Welcome to Our INFO-X....")
	print("")
	print("********************************************************************************")
	print("")
	infomenu()
	infoconf()


	
def infoconf():
	print("")
	print("")
	time.sleep(6)
	loop = input("[+]Do you want to continue with INFO - X? (Y/N) ")
	if loop=="Y" or loop == "y":
	    #os.system('clear')
	    infomenu()
	    infoconf()
	elif loop=="N" or loop == "n":
	    print("****************************************")
	    print("")
	    print("ThankYou for Using our INFO - X....!")
	    print("")
	    print("****************************************")
	else:
	    print("")
	    print("Enter the Valid Input")
	    infoconf()
	
def domain():
	A= input("[+]Enter the website (Example: google.com):")
	print("Wait! You will be redirecting to your browser...!")
	domain1 = "https://whois.domaintools.com/"+ A # DOMAIN
	subdomain2 = "https://securitytrails.com/list/apex_domain/" + A # subdomains
	googlesearch4 = "https://www.google.ca/search?q=site:*." + A # subdomain in google search

	webbrowser.open(domain1)
	webbrowser.open(subdomain2)
	webbrowser.open(googlesearch4)

def hosting():
	A= input("[+]Enter the website (Example: google.com):")
	print("Wait! You will be redirecting to your browser...!")
	hosting1 = "https://digital.com/best-web-hosting/who-is/#search=www."+ A # hosting
	hosting2 = "https://www.codeinwp.com/who-is-hosting-this/#s=" + A

	webbrowser.open(hosting1)
	webbrowser.open(hosting2)
	
def viewdns():
	A= input("[+]Enter the website (Example: google.com):")
	print("Wait! You will be redirecting to your browser...!")
	viewdns1 = "https://viewdns.info/reversewhois/?q=" + A # whois lookup(domain names)
	viewdns2 = "https://viewdns.info/whois/?domain=" + A # domain/IP whois
	viewdns3 = "https://viewdns.info/portscan/?host=" + A # open port scanner
	viewdns4 = "https://viewdns.info/dnsreport/?domain=" + A # DNS report

	webbrowser.open(viewdns1)
	webbrowser.open(viewdns2)
	webbrowser.open(viewdns3)
	webbrowser.open(viewdns4)
	
def virusscan():
	A = input("[+]Enter the website (Example: google.com):")
	print("Wait! You will be redirecting to your browser...!")
	virustotal = "https://www.virustotal.com/gui/domain/"+A
	sitecheck = "https://sitecheck.sucuri.net/results/"+A

	webbrowser.open(virustotal)
	webbrowser.open(sitecheck)
	
def otherinfo():
	A= input("[+]Enter the website (Example: google.com):")
	print("Wait! You will be redirecting to your browser...!")
	robo = "https://www." + A + "/robots.txt" # textfiles
	cert = "https://crt.sh/?q=%25." + A # certificates
	rank = "https://dnslytics.com/domain/" + A # domain and ranking information
	geoinfo = "https://www.accessify.com/"+ A[0]+ "/" + A

	webbrowser.open(robo)
	webbrowser.open(cert)
	webbrowser.open(rank)
	webbrowser.open(geoinfo)
	
	
def infomenu():
	print("")
	print("<== = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ==>")
	print("")
	print("Choose the below given action you want to execute...")
	print("")
	print(""""
	1. SUBDOMAIN/DOMAIN
	2. HOSTING
	3. PORTS/DNS/WHOIS
	4. VIRUS SCANNER
	5. OTHER INFORMATIONS
	6. QUIT INFO-X
	""")
	infoxoptions()

def infoxoptions():
	i_inp=input("Enter number in the above given options of information you want: ")
	if i_inp=="1":
		domain()
	elif i_inp=="2":
		hosting()
	elif i_inp=="3":
		viewdns()
	elif i_inp=="4":
		virusscan()
	elif i_inp=="5":
		otherinfo()
	elif i_inp=="6":
		print("***********************************************")
		print("")
		print("Quiting... ThankYou for Using our INFO - X...!")
		print("")
		print("***********************************************")
		conformation()
	else:
	    	print("")
	    	print("Please enter valid Option!")
	    	infoxoptions()
	    
###INFO-X ends###
#################


### Main Starts ###
###################


alpha_x()
conformation()



### Main Ends ###
#################

