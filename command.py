import subprocess

class Command(object):
    def __init__(self):
        self.commands = { 
            "test" : self.test,
            "tempdc"  : self.tempdc,
            "upsdc"  : self.upsdc,
            "dns"  : self.dns,
            "help" : self.help
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: " 

        if command in self.commands:
            response += self.commands[command]()
        else:
           response += "Sorry ambo xpehe the command: " + command + ". " + self.help()

        return response

    def test(self):
        return "testing command" 

    def dns(self):
            tarikh = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
            (output_tarikh, err) = tarikh.communicate()
            probe1 = subprocess.Popen("/usr/local/nagios/libexec/check_dns -H x1.com.my -s 1.1.1.1 | awk '{print $2,$3,$4,$5,$6,$7,$8,$9}' ", stdout=subprocess.PIPE, shell=True)
            (output_probe1, err) = probe1.communicate()
            probe2 = subprocess.Popen("/usr/local/nagios/libexec/check_dns -H x2.com.my -s 1.1.1.1 | awk '{print $2,$3,$4,$5,$6,$7,$8,$9}' ", stdout=subprocess.PIPE, shell=True)
            (output_probe2, err) = probe2.communicate()
            probe3 = subprocess.Popen("/usr/local/nagios/libexec/check_dns -H x3.com.my -s 1.1.1.1 | awk '{print $2,$3,$4,$5,$6,$7,$8,$9}' ", stdout=subprocess.PIPE, shell=True)
            (output_probe3, err) = probe3.communicate()
            msg = ('This is pusatdatakk_bot info dns status\n'
            "Date: "+output_tarikh+
            "1. DNS server 1.1.1.1 lookup: "+output_probe1+
            "2. DNS server 1.1.1.2 lookup :"+output_probe2+
            "3. DNS server 1.1.1.3 lookup domain xxx.yy :"+output_probe3)
            return msg

    def upsdc(self):
            tarikh = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
            (output_tarikh, err) = tarikh.communicate()
            probe1 = subprocess.Popen("/usr/local/nagios/libexec/check_apc.pl -H xx.xx.xx.xx -C yourpass -l out_status ", stdout=subprocess.PIPE, shell=True)
            (output_probe1, err) = probe1.communicate()
            probe2 = subprocess.Popen("/usr/local/nagios/libexec/check_apc.pl -H xx.xx.xx.xx -C yourpass -l bat_run_remaining | awk '{print $2,$3,$4,$5,$6,$7}' ", stdout=subprocess.PIPE, shell=$
            (output_probe2, err) = probe2.communicate()
            probe3 = subprocess.Popen("/usr/local/nagios/libexec/check_apc.pl -H xx.xx.xxx -C yourpass -l bat_temp | awk '{print $2,$3,$4,$5,$6,$7}' ", stdout=subprocess.PIPE, shell=True)
            (output_probe3, err) = probe3.communicate()
            msg = ('This is pusatdatakk_bot ups60kva bilik ups telefonis \n'
            "Date: "+output_tarikh+
            "Batery OUTPUT status: "+output_probe1+
            "Time Remaining :"+output_probe2+
            "Battery Temp :"+output_probe3)
            return msg

    
    def tempdc(self):
            tarikh = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
            (output_tarikh, err) = tarikh.communicate()
            probe1 = subprocess.Popen("/usr/local/nagios/libexec/check_snmp -H xx.xx.xx.xx -o enterprises.17095.3.2.0 -w 20 -c 30 | awk '{print $4}' ", stdout=subprocess.PIPE, shell=True)
            (output_probe1, err) = probe1.communicate()
            probe2 = subprocess.Popen("/usr/local/nagios/libexec/check_snmp -H xx.xx.xx.xx -o enterprises.17095.3.10.0 -w 20 -c 30 | awk '{print $4}' ", stdout=subprocess.PIPE, shell=True)
            (output_probe2, err) = probe2.communicate()
            msg = ('This is pusatdatakk_bot temp datacenter ppkt \n'
            "Date: "+output_tarikh+
            "Temp probe1: "+output_probe1+
            "Temp probe2 :"+output_probe2)
            return msg


    def help(self):
        response = "Currently ambo support the following commands:\r\n" 

        for command in self.commands:
            response += command + "\r\n" 

        return response
