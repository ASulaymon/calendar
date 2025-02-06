from calendar import *

while True:
    y = int(input("qaysi yilning kalendari kerak?\n>> "))
    m = int(input("qaysi oyning kalendari kerak?\n>> "))

    c = month(y, m)

    
    myfile = open("calendar.txt", "w")

    myfile.write(f"{c}\n− ASulaymon")

    myfile.close()

    print("calendar.txt fayliga qarang!")