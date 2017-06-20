import pymydb

myconnection = pymydb.MySQL()

print(myconnection)

myconnection.drop_db()