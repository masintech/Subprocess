import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest ="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args() # arguments is a empty list []

    if not options.interface:
        parse.error("[-] Please specify an interface, user --help for more info")
    elif not options.new_mac:
        parse.error("[-] Please specify a new mac, use --help for more info")
    return options



def get_current_mac (interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result :
        return mac_address_search_result.group(0)
    else:
        print("[-] MAC address not found")
# do the command on shell
# shut down the interface
def mac_changer(interface, mac_addr):
    # disable the interface add sudo in the list if it's necessary in your case
    subprocess.call(["ifconfig",interface,"down"])
    # change its mac address
    subprocess.call(["ifconfig",interface,"hw","ether",mac_addr])
    # enable the interface
    subprocess.call(["ifconfig",interface,"up"])


if __name__=="__main__" :

    options= get_arguments()
    #ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
    current_mac = get_current_mac(options.interface, options.new_mac)
    print("The original MAC address is ",current_mac)
    mac_changer(interface, options.new_mac)
    print("Now the MAC address has changed to ",current_mac)






    # interface = input("interface: ")
    # print("original MAC address: ")
    # cmd = "ifconfig "+interface+" | grep ether"
    # #print(cmd)
    # ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # output = ps.communicate()[0]
    #
    # #ps = subprocess.Popen(('ifconfig',interface),stdout=subprocess.PIPE)
    # #output = subprocess.check_output(('grep',interface),stdin=ps.stdout)
    # #ps.wait()
    # print(output)
    # #subprocess.call(["ifconfig", interface, "|","grep", "ether"])
    # print("[+] change the mac address of interface: "+interface+" to "+mac_addr)
    # mac_changer(interface, mac_addr)
