import subprocess
import optparse
# do the command on shell
# shut down the interface
def mac_changer(interface, mac_addr):
    # disable the interface
    subprocess.call(["sudo","ifconfig",interface,"down"])
    # change its mac address
    subprocess.call(["sudo","ifconfig",interface,"hw","ether",mac_addr])
    # enable the interface
    subprocess.call(["sudo","ifconfig",interface,"up"])

if __name__=="__main__" :

    mac_addr = '11:f2:33:44:e5:26'
    # parser = optparse.OptionParser()
    # parser.parse_args()
    # # user can add -i or --interface and then store the value to variable called interface
    # parse.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")

    interface = input("interface: ")
    print("original MAC address: ")
    subprocess.call(["ifconfig", interface, "|","grep", "ether"])
    print("[+] change the mac address of interface: "+interface+" to "+mac_addr)
    mac_changer(interface, mac_addr)
