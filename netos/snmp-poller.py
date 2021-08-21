import csv
import schedule
import time
from easysnmp import *


def poll(host, com, ver, mib):
    session = Session(hostname=host, community=com, version=ver)
    output = session.get(mib)
    print(output.value)

with open('snmp-poller-inventory.csv') as inventory:
    invcsv = csv.reader(inventory)
    for row in invcsv:
        host = row[0]
        com = row[1]
        ver = int(row[2])
        freq = int(row[3])
        for mib in row[4:]:
            schedule.every(freq).seconds.do(poll, host, com, ver, mib)

while True:
    schedule.run_pending()
    time.sleep(1)
