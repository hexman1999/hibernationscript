#!/usr/bin/python3
import os
from os.path import expanduser
homedir=expanduser('~')
import sys
if not os.geteuid() == 0:
    sys.exit("\nOnly root can run this script\n")

os.system('clear')
print("\n--------------------------------------------------\nWelcome To HibernateScript\n\nJob: Hibernate after a specific period of sleep\n\nMade by: Muhammad Ashraf\n-----------------------------------------------------\n\n")
def printdc():print(str(run1.dcval)+' '+ str(run1.dcunit) +' which is/are ' + str(run1.dctime) + ' seconds')
def printac():print(str(run2.acval)+' '+ str(run2.acunit) +' which is/are ' + str(run2.actime) + ' seconds')
def run1():
	run1.dc = input("Please Enter the Period Time You want the PC to hibernate in Battery Power(if present) (d,h,m,s) (default:m) : ")
	while run1.dc=='':
		print('\nplease input value\n')
		run1.dc = input("Please Enter the Period Time You want the PC to hibernate in Battery Power(if present) (d,h,m,s) (default:m) : ")
#dc: input
#dctime: time used finally
#dcval: first part of input
#dcunit: unit of time
	run1.dcunit=run1.dc[-1]
	try: 
		if isinstance(int(run1.dcunit),int):run1.dc = str(run1.dc) + 'm' 
		run1.dcunit=run1.dc[-1]
	except : pass


	run1.dcval=run1.dc.split(run1.dcunit)[0]
	try : run1.dcvalint=int(run1.dcval)
	except : run1.dcvalint=''
	if run1.dcunit in ['h','m','d','s']  and run1.dcval!='' and isinstance(run1.dcvalint,int):
		run1.dcval=int(run1.dcval) 
		if run1.dcunit == 'd':
			run1.dctime = run1.dcvalint*24*60*60
			run1.dcunit='day(s)'
			printdc()
			
		elif run1.dcunit == 'h':
			run1.dctime = run1.dcvalint*60*60
			run1.dcunit='hour(s)'
			printdc()
			
		elif run1.dcunit == 'm':
			run1.dctime = run1.dcvalint*60
			run1.dcunit='minute(s)'
			printdc()
			
		elif run1.dcunit == 's': 
			run1.dctime=run1.dcvalint
			run1.dcunit = 'second(s)'
			printdc()
		else:
			print("\n\ninvailed input, Please Try again\n\n")
			run1()
			
	else:
		print('\n\ninvailed input, Please Try again\n\n')
		run1()		
run1()

def run2():
	run2.ac = input("\n\nPlease Enter the Period Time You want the PC to hibernate in AC Power (d,h,m,s) (default:m) : ")
	while run2.ac=='':
		print('\nplease input value\n')
		run2.ac = input("Please Enter the Period Time You want the PC to hibernate in AC Power (d,h,m,s) (default:m) : ")

	run2.acunit=run2.ac[-1]
	try: 
		if isinstance(int(run2.acunit),int):run2.ac = str(run2.ac) + 'm' 
		run2.acunit=run2.ac[-1]
	except : pass 


	run2.acval=run2.ac.split(run2.acunit)[0]
	try : run2.acvalint=int(run2.acval)
	except : run2.acvalint=''
	if run2.acunit in ['h','m','d','s']  and run2.acval!='' and isinstance(run2.acvalint,int):
 
		if run2.acunit == 'd':
			run2.actime = run2.acvalint*24*60*60
			run2.acunit='day(s)'
			printac()
		elif run2.acunit == 'h':
			run2.actime = run2.acvalint*60*60
			run2.acunit='hour(s)'
			printac()
		elif run2.acunit == 'm':
			run2.actime = run2.acvalint*60
			run2.acunit= 'minute(s)'
			printac()
		elif run2.acunit == 's': 
			run2.actime=run2.acvalint
			run2.acunit = 'second(s)'
			printac()

	else:
		print("\n\ninvailed input, Please Try again\n\n")
		run2()
	


run2()
#def restart():
#	python = sys.executable
#	os.execl(python, python, * sys.argv)

#logfile

os.system('clear')



print('''
Summary:
 
on Battery time is %(bat)s %(run1.dcunit)s (%(dctime)s seconds)

on AC Power time is %(ac)s %(run2.acunit)s (%(actime)s seconds)

''' %{'actime':run2.actime,'dctime':run1.dctime ,'bat' : str(run1.dcval),'ac' : str(run2.acval), 'run2.acunit' : str(run2.acunit), 'run1.dcunit' : str(run1.dcunit)})



path='/lib/systemd/system-sleep/hibernationscript'


go_on=input("Is these values correct??, please checkout to continue. (y,n) (default:y)")
if go_on=='' or go_on=='y': go_on='y'
else : sys.exit('')


def check():
	if go_on == 'y': 
		hibermethod=input('\nwhich tool you want for running the hibernation command \n\n(pm-hibernate:p, systemctl hibernate:s): ')
		if hibermethod == 's': check.hibermethod = 'systemctl hibernate'
		elif hibermethod == 'p' : check.hibermethod ='pm-hibernate'
		elif hibermethod == '' : 
			print('\nplease select input method\n')
			check()
		else : 
			print('\nInvailed input!!\n')
			check()
	
check()

os.system("echo -e '''\
#!/bin/bash\n\
# Purpose: Auto hibernates after a period of sleep\n\
# Edit the \"autohibernate\" variable below to set the number of seconds to sleep.\n\
lockfile=/var/run/systemd/rtchibernate.lock\n\
curtime=$(date +%(s)s)\n\
logfile=/tmp/tmp.log\n\
hibernate=/bin/systemctl\n\
ac_adapter=$(cat /sys/class/power_supply/AC/online)\n\
if [ \"$ac_adapter\" = \"1\" ]; then\n\
    autohibernate=%(achiber)s\n\
else\n\
    autohibernate=%(dchiber)s\n\
fi\n\
case $1/$2 in\n\
  pre/suspend)\n\
    # Suspending. Record current time, and set a wake up timer.\n\
    echo \"Suspending until\" `date -d \"$autohibernate seconds\"` >> $logfile\n\
    echo \"$curtime\" > $lockfile\n\
    rtcwake -m no -s $autohibernate\n\
    ;;\n\
  post/suspend)\n\
    # Coming out of sleep\n\
    sustime=$(cat $lockfile)\n\
    echo -n \"Back from suspend... $curtime \" >> $logfile\n\
    rm $lockfile\n\
    # Did we wake up due to the rtc timer above?\n\
    if [ $(($curtime - $sustime)) -ge $autohibernate ]\n\
    then\n\
        # Then hibernate\n\
        echo \"hibernate\" >> $logfile\n\
        %(method)s\n\
    else\n\
        echo \"wake-up\" >> $logfile\n\
        # Otherwise cancel the rtc timer and wake up normally.\n\
        rtcwake -m disable\n\
    fi\n\
    ;;\n\
esac\n''' > %(path)s && chmod +x %(path)s" %{'path':path,'achiber':run2.actime,'dchiber':run1.dctime,'method':check.hibermethod,'s':'%s'})

os.system('clear')
print("!!!!!!!!!!Done!!!!!!!!!!!")
