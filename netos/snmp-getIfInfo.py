import csv
import schedule
import time

from easysnmp import *


def getIfInfo(host, com, ver):

    session = Session(hostname=host, community=com, version=ver)

    CRED = '\033[41m'
    CGREEN = '\033[32m'
    CEND = '\033[0m'

    try:
        if_num = int(session.get('ifNumber.0').value)
        if_numbers = if_num + 1

        result_all = []

        for index in range(if_numbers):
            check_instance = session.get("ifIndex.{}".format(index)).value != "NOSUCHINSTANCE"
            check_nulls = "null" not in session.get("ifDescr.{}".format(index)).value.lower()

            if index != 0 and check_instance and check_nulls:
                result = [session.get("ifIndex.{}".format(index)).value, session.get("ifDescr.{}".format(index)).value]

                if_admin_status_number = int(session.get("ifAdminStatus.{}".format(index)).value)
                if if_admin_status_number == 1:
                    result.append("up")
                elif if_admin_status_number == 2:
                    result.append("down")
                elif if_admin_status_number == 3:
                    result.append("testing")

                if_oper_status_number = int(session.get("ifOperStatus.{}".format(index)).value)
                if if_oper_status_number == 1:
                    result.append("up")
                elif if_oper_status_number == 2:
                    result.append("down")
                elif if_oper_status_number == 3:
                    result.append("testing")
                elif if_oper_status_number == 4:
                    result.append("unknown")
                elif if_oper_status_number == 5:
                    result.append("dormant")
                elif if_oper_status_number == 6:
                    result.append("notPresent")
                elif if_oper_status_number == 7:
                    result.append("lowerLayerDown")

                result_all.append(result)

        inventory_ip = str(host.replace(".", "_"))
        inventory_base = "snmp-ifInfo-"
        inventory_extension = ".csv"
        inventory_file_name = inventory_base + inventory_ip + inventory_extension

        with open(inventory_file_name, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(result_all)

        print(CGREEN + inventory_file_name + " has been created." + CEND)

    except EasySNMPTimeoutError:
        print(CRED + "Timeout on getting interfaces info from " + host + ". File is not updated!" + CEND)

    except Exception as e:
        print(CRED + "Something went wrong on " + host + "! Unknown error!" + CEND + "\n")
        print(e)


with open('snmp-getIfInfo-schedule.csv') as getIfSchedule:
    reader = csv.reader(getIfSchedule)
    for row in reader:
        host = row[0]
        com = row[1]
        ver = int(row[2])
        freq = int(row[3])

        schedule.every(freq).seconds.do(getIfInfo, host, com, ver)

while True:
    schedule.run_pending()
    time.sleep(1)
