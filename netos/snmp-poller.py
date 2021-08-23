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
            hrStorageUsed = str(session.get("hrStorageUsed.{}".format(hrStorageIndex)).value)

            memory_base = "snmp-memoryUsage-"
            memory_ip = str(host.replace(".", "_"))
            memory_extension = ".csv"
            memory_file_name = memory_base + memory_ip + memory_extension

            memory_get_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            result_memory = [memory_get_time, hrStorageUsed]

            with open(memory_file_name, 'a+') as file_dsk:
                writer = csv.writer(file_dsk, delimiter=',')
                writer.writerow(result_memory)

            result_memory_total = str(session.get("hrStorageSize.{}".format(hrStorageIndex)).value)
            memory_file_name_total = memory_base + memory_ip + "-totalMemory" + memory_extension
            file_mem_total = open(memory_file_name_total, 'w')
            file_mem_total.write(result_memory_total + "\n")
            file_mem_total.close()

            print(CGREEN + "File " + memory_file_name + " has been updated." + CEND)
            print(CGREEN + "File " + memory_file_name_total + " has been updated." + CEND)

    except EasySNMPTimeoutError:
        print(CRED + "Timeout on getting memory usage from " + host + ". File is not created!" + CEND)

    except Exception as e:
        print(CRED + "Something went wrong on " + host + "! Unknown error!\n\n" + CEND)
        print(e)


def getCpuLoad(host, com, ver):
    session = Session(hostname=host, community=com, version=ver)
    CRED = '\033[41m'
    CGREEN = '\033[32m'
    CEND = '\033[0m'

    try:
        cpu_cores = 2
        cpu_load_time = 1       # 1 = 1min load ; 2 = 5min load ; 3 = 15min load
        cpu_load_raw = str(session.get("laLoad.{}".format(cpu_load_time)).value)
        cpu_load_raw2 = float(cpu_load_raw) / cpu_cores
        cpu_load = str("{:.2f}".format(cpu_load_raw2))

        cpu_base = "snmp-cpuLoad-"
        cpu_ip = str(host.replace(".", "_"))
        cpu_extension = ".csv"
        cpu_file_name = cpu_base + cpu_ip + cpu_extension

        cpu_get_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
        result_cpuload = [cpu_get_time, cpu_load]

        with open(cpu_file_name, 'a+') as file_cpu:
            writer = csv.writer(file_cpu, delimiter=',')
            writer.writerow(result_cpuload)

        print(CGREEN + "File " + cpu_file_name + " has been updated." + CEND)

    except EasySNMPTimeoutError:
        print(CRED + "Timeout on getting CPU load from " + host + ". File is not updated!" + CEND)

    except Exception as e:
        print(CRED + "Something went wrong on " + host + "! Unknown error!\n\n" + CEND)
        print(e)


def getDiskUsage(host, com, ver):
    session = Session(hostname=host, community=com, version=ver)
    CRED = '\033[41m'
    CGREEN = '\033[32m'
    CEND = '\033[0m'

    try:
        dskIndex = 1

        check_disk = "/dev/sda" in session.get("dskDevice.{}".format(dskIndex)).value.lower()

        if check_disk:
            dskTotal = str(session.get("dskTotal.{}".format(dskIndex)).value)
            dskAvailable = str(session.get("dskAvail.{}".format(dskIndex)).value)
            dskUsed = str(session.get("dskUsed.{}".format(dskIndex)).value)

            disk_base = "snmp-diskUsage-"
            disk_ip = str(host.replace(".", "_"))
            disk_extension = ".csv"
            disk_file_name = disk_base + disk_ip + disk_extension

            disk_get_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            result_disk = [disk_get_time, dskTotal, dskAvailable, dskUsed]

            with open(disk_file_name, 'a+') as file_dsk:
                writer = csv.writer(file_dsk, delimiter=',')
                writer.writerow(result_disk)

            print(CGREEN + "File " + disk_file_name + " has been updated." + CEND)

    except EasySNMPTimeoutError:
        print(CRED + "Timeout on getting memory usage from " + host + ". File is not updated!" + CEND)

    except Exception as e:
        print(CRED + "Something went wrong on " + host + "! Unknown error!\n\n" + CEND)
        print(e)


with open('snmp-poller-schedule.csv') as inventory:
    invcsv = csv.reader(inventory)
    for row in invcsv:
        host = row[0]
        com = row[1]
        ver = int(row[2])
        freq = int(row[3])

        schedule.every(freq).seconds.do(getMemoryUsage, host, com, ver)
        schedule.every(freq).seconds.do(getDiskUsage, host, com, ver)
        schedule.every(freq).seconds.do(getCpuLoad, host, com, ver)

while True:
    schedule.run_pending()
    time.sleep(1)
