import csv
from datetime import *
import schedule
import time
from easysnmp import *


def getMemoryUsage(host, com, ver):
    session = Session(hostname=host, community=com, version=ver)
    CRED = '\033[41m'
    CGREEN = '\033[32m'
    CEND = '\033[0m'

    try:
        result_memory = []
        hrStorageIndex = 1

        check_storage_ram = ".1.3.6.1.2.1.25.2.1.2" in session.get("hrStorageType.{}".format(hrStorageIndex)).value.lower()

        if check_storage_ram:
            result_memory = str(session.get("hrStorageUsed.{}".format(hrStorageIndex)).value)

            memory_base = "snmp-memoryUsage-"
            memory_ip = str(host.replace(".", "_"))
            memory_extension = ".csv"
            memory_file_name = memory_base + memory_ip + memory_extension

            memory_get_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result_memory_text = result_memory + "," + memory_get_time
            file_mem = open(memory_file_name, 'a+')
            file_mem.write(result_memory_text + "\n")
            file_mem.close()

            result_memory_total = str(session.get("hrStorageSize.{}".format(hrStorageIndex)).value)
            memory_file_name_total = memory_base + memory_ip + "-totalMemory" + memory_extension
            file_mem_total = open(memory_file_name_total, 'w')
            file_mem_total.write(result_memory_total + "\n")


            print(CGREEN + memory_file_name + " has been created." + CEND)

    except EasySNMPTimeoutError:

        print(CRED + "Timeout on getting memory usage from " + host + ". File is not created!" + CEND)


def getCpuLoad(host, com, ver):
    session = Session(hostname=host, community=com, version=ver)

    resultDevice = []

    inventory_base = "snmp-devUsage-"
    inventory_ip = str(host.replace(".", "_"))
    inventory_deviceType = ""
    inventory_extension = ".csv"
    inventory_file_name = inventory_base + inventory_ip + inventory_deviceType + inventory_extension

    with open(inventory_file_name, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(resultDevice)


def getStorageUsage(host, com, ver):
    session = Session(hostname=host, community=com, version=ver)

    resultDevice = []

    inventory_base = "snmp-devUsage-"
    inventory_ip = str(host.replace(".", "_"))
    inventory_deviceType = ""
    inventory_extension = ".csv"
    inventory_file_name = inventory_base + inventory_ip + inventory_deviceType + inventory_extension

    with open(inventory_file_name, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(resultDevice)


def getNetworkUsage(host, com, ver):
    session = Session(hostname=host, community=com, version=ver)

    resultDevice = []

    inventory_base = "snmp-devUsage-"
    inventory_ip = str(host.replace(".", "_"))
    inventory_deviceType = ""
    inventory_extension = ".csv"
    inventory_file_name = inventory_base + inventory_ip + inventory_deviceType + inventory_extension

    with open(inventory_file_name, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(resultDevice)



with open('snmp-poller-inventory.csv') as inventory:
    invcsv = csv.reader(inventory)
    for row in invcsv:
        host = row[0]
        com = row[1]
        ver = int(row[2])
        freq = int(row[3])

        schedule.every(freq).seconds.do(getMemoryUsage, host, com, ver)

while True:
    schedule.run_pending()
    time.sleep(1)
