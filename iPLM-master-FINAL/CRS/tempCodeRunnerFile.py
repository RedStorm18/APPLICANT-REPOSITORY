import MySQLdb
import datetime
def tf():
    x = datetime.datetime.now()
    y = x.strftime("%y")
    z = x.strftime("%d")
    v = x.strftime("%m")
    connec = MySQLdb.connect("localhost","root","","plm_trialdb")
    cursor = connec.cursor()
    a = cursor.execute("SELECT LAST_INSERT_ID() from crs_transfereeapplicant;")
    num = int(a) + 1
    num =str(num)
    test = len(num)
    if test < 2:
        num2 = y + z +v + "00" +num
    elif test <3:
        num2 = y + z +v + "0" +num
    else:
        num2 = y + z +v +num
    applicant_num = num2
    return applicant_num
mail = tf()
print (mail)



