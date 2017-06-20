import pymydb

myconnection = pymydb.MySQL()

print(myconnection.get_records('trial3',count=4))