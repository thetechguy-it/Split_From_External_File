class Device:
    '''Router Class'''
    def __init__(self, ip_add, hname, os_version):
        '''initialize values'''
        self.ip_add = ip_add
        self.hname = hname
        self.os_version = os_version

    def getdesc(self):
        '''return a formatted description of the device'''
        desc = f'Device Management Address:{self.ip_add}\n'\
               f'Device Hostname          :{self.hname}\n'\
               f'Device OS Version        :{self.os_version}'
        return desc

test = open("devices.txt", "r")
test_temp = test.readlines()
print(test_temp)
switches_list = []
n = 0
for switches in test_temp:
    switches_temp_list1 = switches.split("\n")
    switches_list.append(switches_temp_list1[0])
    #print(switches_list)
    dynamic_v = switches_list
    dynamic_v = switches.split(",")
    ip = dynamic_v[0]
    hostname = dynamic_v[1]
    ios = dynamic_v[2]
    switch = Device(ip, hostname, ios)
    n = n + 1
    print("Switch #", n, "\n" + switch.getdesc() + "\n")
test.close()