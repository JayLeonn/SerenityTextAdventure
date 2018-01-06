import mysql.connector
import time
import sys
db = mysql.connector.connect(host="localhost",
                             user="dbuser09",
                             passwd="dbpass",
                             db="serenity",
                             buffered=True)
cur = db.cursor()
oxygen = 1
def kirjoita(lause):
   for l in lause:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.00)


def kirjoita1(lause):
   for l in lause:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
    

def kirjoita2(lause):
   for l in lause:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)


def use(target):

    cur = db.cursor()
    sql = "SELECT room_id FROM PLAYER"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        roomid=str(row[0])

    items = []
    sql = "SELECT name FROM ITEM WHERE player_id = 1"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        items.append(row[0])

    objects = []
    sql = "SELECT name FROM OBJECT WHERE room_id = (SELECT room_id FROM PLAYER)"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        objects.append(row[0])

    sanalista=target.split(" ")
    if "on" in sanalista:
        sanalista=target.split(" on ")
        if sanalista[0] == "tool" and "Hyper-X 1872" in items:
            sanalista[0] = "Hyper-X 1872"
        if sanalista[1] =="pod" and "escape pod" in objects:
            sanalista[1] = "escape pod"
        if sanalista[0] == "mask" and "breathing mask" in items:
            sanalista[0] = "breathing mask"
        if sanalista[0] == "mask" and "breathing mask with oxygen tank" in items or target == "breathing mask" and "breathing mask with oxygen tank" in items:
            sanalista[0] = "breathing mask with oxygen tank"
        if sanalista[0] == "tank" and "oxygen tank" in items:
            sanalista[0] = "oxygen tank"
        if sanalista[1] == "mask" and "breathing mask" in items:
            sanalista[1] = "breathing mask"
        if sanalista[1] == "mask" and "breathing mask with oxygen tank" in items or target == "breathing mask" and "breathing mask with oxygen tank" in items:
            sanalista[1] = "breathing mask with oxygen tank"
        if sanalista[1] == "tank" and "oxygen tank" in items:
            sanalista[1] = "oxygen tank"
        if sanalista[1] == "part" and roomid == "4" and sanalista[0] == "Hyper-X 1872":
            sanalista[1] = "escape pod"
        if sanalista[1] == "engine" and "hyperdrive engine" in objects:
            sanalista[1] = "hyperdrive engine"
        if sanalista[0] == "part" and "engine part" in items:
            sanalista[0] = "engine part"

    #aliakset
    if target == "password terminal" and roomid == "2":
        target = "Flight Deck password terminal"
    if target == "terminal" and roomid == "2":
        target = "Flight Deck password terminal"
    if target == "flight deck password terminal":
        target = "Flight Deck password terminal"
    if target == "switch" and roomid == "3":
        target = "light switch"
    if target == "switch" and roomid == "5":
        target = "oxygen switch"
    if target == "pc" and roomid == "1":
        target = "computer"
    if target == "control panel" and roomid == "3":
        target = "Spaceship control panel"
    if target == "hatch" and roomid == "7":
        target = "escape hatch"
    if target == "lever" and roomid == "7":
        target = "escape hatch"
    if target == "mask" and "breathing mask" in items:
        target = "breathing mask"
    if target == "mask" and "breathing mask with oxygen tank" in items:
        target = "breathing mask with oxygen tank"
    if target == "breathing mask" and "breathing mask with oxygen tank" in items:
        target = "breathing mask with oxygen tank"
    if target == "part" and "engine part" in items:
        target = "engine part"

    #computer
    if target=="computer" and target in objects:
        computer=1
        kirjoita("Starting compute"),kirjoita2("r......"),print("")
        while computer==1:
            kirjoita1("1. Show crew member information"), print("")
            kirjoita1("2. Exit computer"), print("")
            inputti=input("")
            if inputti=="1":
                kirjoita1("Please_insert_a_pod_number:")
                inputti=input("")
                if inputti == "1" or inputti == "2" or inputti == "4" or inputti == "5":
                    print("")
                    print(">>1>k>!>x?>>%>>>@>>d>3!!>#>7>}]>>w{>>[>>e>$$>0>>")
                    kirjoita1("Ser011100110e locat#sdf 0101010class KttC? sh!t"), print("")
                    kirjoita1("!(!/=)(/0H9),"), print("")
                    kirjoita1("Or1gi551230 142186f"), print("")
                    kirjoita1("D!!o)/!)(/ing: sd.01:19"), print("")
                    print("<0<s<<<d<<s<?<<xD<<1<f<<?<s<3¤<<L0L9<!43<<f<A?!<")
                    kirjoita2("File corrupted"), print("")
                    print("")
                elif inputti == "3":
                    print("")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    kirjoita1("Crew member #3"), print("")
                    kirjoita1("Service location: USS Serenity, a middle class attack ship"), print("")
                    kirjoita1("Rank: SpacePrivate"), print("")
                    kirjoita1("Origin: Kepler-186f"), print("")
                    kirjoita1("Date of cryo freezing: 01.01.2615"), print("")
                    kirjoita1("Current star date: 21.05.2620"), print("")
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    print("")
                else:
                    kirjoita2("incorrect input"), print("")
            elif inputti=="2" or inputti=="exit":
                computer=0
                kirjoita1("Shutting down..."),print("")
                return
            else:
                kirjoita2("incorrect input"), print("")
                

    #light switch        
    elif target == "light switch" and target in objects:
        sql = "SELECT dark FROM ROOM WHERE room_id = 6"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            dark = str(row[0])

        if dark == "1":
            sql = "UPDATE ROOM SET dark = 0 WHERE room_id = 4 OR room_id = 6"
            cur.execute(sql)
            sql = "UPDATE ROOM SET description_id = 34, visited = 0 WHERE room_id = 2"
            cur.execute(sql)
            print("You toggled lights on")
        else:
            sql = "UPDATE ROOM SET dark = 1 WHERE room_id = 4 OR room_id = 6"
            cur.execute(sql)
            sql = "UPDATE ROOM SET description_id = 2 WHERE room_id = 2"
            cur.execute(sql)
            print("You toggled lights off")

    #password terminal
    elif target == "Flight Deck password terminal" and target in objects:
        kirjoita2("Enter 8 number password:")
        password=input("")
        if password == "01012615":
            sql = "UPDATE ROOM SET locked = 0 WHERE room_id = 3"
            cur.execute(sql)
            kirjoita2("Door unlocked"), print("")
        else:
            kirjoita2("Incorrect password"), print("")

    #oxygen switch
    elif target =="oxygen switch" and target in objects:
        print("Would you like to turn off the oxygen?") ,print("")
        inputti=input("[WARNING]: All oxygen will be sucked out! Y/N: ").upper()
        loop = 1
        while loop == 1:
            if inputti=="Y":
                sql= "UPDATE ROOM SET fire=0"
                cur.execute(sql)
                sql= "SELECT mask FROM player WHERE mask=1"
                cur.execute(sql)
                loop=0
                if cur.rowcount!=1:
                    print("You have turned off the oxygen without any breathing equipment. You have suffocated.")
                    print(" ")
                    print("-----------------------------------------")
                    db.rollback()
                    loop = 1
                    while loop == 1:
                        inputti=input("Do you want to restart the game? Y/N: ").upper()
                        if inputti=="Y":
                            print("-----------------------------------------")
                            print(" ")
                            loop=0
                            alku()
                        elif inputti == "N":
                            kirjoita2("Closing game...")
                            loop=0
                            sys.exit(0)
                        else:
                            print("Please insert proper answer")
                            inputti=input("Do you want to restart the game? Y/N: ").upper()
                else:
                    print("You have turned off the oxygen.")
                    return

            elif inputti=="N":
                print("You step away from the switch.")
                loop=0
                return
            else:
                print("Please insert proper answer")
                inputti=input("[WARNING]: All oxygen will be sucked out! Y/N: ").upper()
        
    #use item on object
    elif sanalista[0] in items and sanalista[1] in objects:
        #use tool on escape pod
        if sanalista[0]=="Hyper-X 1872" and sanalista[1]=="escape pod":
            sql = "SELECT object_id, player_id FROM ITEM WHERE item_id = 5"
            cur.execute(sql)
            res = cur.fetchall()
            for row in res :
                sijainti2 = str(row[0])
                sijainti1 = str(row[1])
            if sijainti1=="1" or sijainti2=="16": 
                print("You have already taken the engine part.")
            else: 
                print("You removed and took the engine part from the escape pod with Hyper-X 1872 tool.")
                sql = "UPDATE ITEM SET player_id = 1, object_id = NULL WHERE item_id = 5"
                cur.execute(sql)
                sql = "UPDATE ROOM SET description_id = 35 WHERE room_id = 4"
                cur.execute(sql)
        
        #use engine part on engine       
        elif sanalista[0]=="engine part" and sanalista[1]=="hyperdrive engine":
            print("You put the engine part in the engine and fixed the engine system.")
            sql = "UPDATE ITEM SET player_id = NULL, object_id = 16 WHERE item_id = 5"
            cur.execute(sql)
            sql = "UPDATE ROOM SET description_id = 40, visited = 0 WHERE room_id = 3"
            cur.execute(sql)
            
        else:
            print("You cannot use", target)

    #use item on item
    elif sanalista[0] in items and sanalista[1] in items:            
        #use breathing mask on oxygen tank
        if sanalista[0]=="breathing mask" and sanalista[1]=="oxygen tank" or sanalista[0]=="oxygen tank" and sanalista[1]=="breathing mask":
            combine("breathing mask with oxygen tank")
        else:
            print("can't use", target)
            
    #control panel
    elif target == "Spaceship control panel" and target in objects:
        sql = "SELECT object_id FROM ITEM WHERE item_id = 5"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            sijainti = str(row[0])

        if sijainti == "16":
            loppu()
        else:
            print("The engine is broken. Perhaps it could be fixed.")

    #Escape hatch
    elif target =="escape hatch" and target in objects:
        inputti=input("WARNING: do you really want to open the hatch? Y/N: ").upper()
        loop = 1
        while loop == 1:
            if inputti =="Y":
                print("You have been sucked into space, sweet dreams")
                print(" ")
                print("-----------------------------------------")
                db.rollback()
                while loop == 1:
                    inputti=input("Do you want to restart the game? Y/N: ").upper()
                    if inputti=="Y":
                        print("-----------------------------------------")
                        print(" ")
                        loop=0
                        alku()
                    elif inputti=="N":
                        kirjoita2("Closing game..."),print("")
                        loop=0
                        sys.exit(0)
                    else:
                        print("Please insert a proper asnwer")
                        inputti=input("Do you want to restart the game? Y/N: ").upper()
            elif inputti =="N":
                print("You step away from the Hatch")
                loop=0
                return
            else:
                print("Please insert a proper asnwer")
                inputti=input("WARNING: do you really want to open the hatch? Y/N: ").upper()

    #use breathing mask            
    elif target == "breathing mask" and target in items:
        equip(target)

    #use breathing mask with oxygen tank
    elif target == "breathing mask with oxygen tank" and target in items:
        equip(target)
        
    else:
        print("can't use", target)
    
    
def equip(target):
    items = []
    sql = "SELECT name FROM ITEM WHERE player_id = 1"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        items.append(row[0])
        
    if target == "mask" and "breathing mask with oxygen tank"in items:
        target = "breathing mask with oxygen tank"
    if target =="breathing mask" and "breathing mask with oxygen tank" in items:
        target = "breathing mask with oxygen tank"
    if target == "mask" and "breathing mask" in items:
        target = "breathing mask"

    sql = "SELECT player_id FROM ITEM WHERE name = '" + target + "'"
    cur.execute(sql)
    
    if cur.rowcount==1:
        if target == "breathing mask with oxygen tank":
            print("You equip breathing mask")
            sql = "UPDATE PLAYER SET mask = 1"
            cur.execute(sql)
        elif target == "breathing mask":
            print("It seems to be missing an oxygen source.")
        else:
            print("You can't equip " +target)
    else:
        print("You can't equip that.") 
    return cur.rowcount

def read(target):
    cur = db.cursor()
    items=[]   
    sql = "SELECT name FROM ITEM WHERE room_id = (SELECT room_id FROM PLAYER) OR player_id = 1"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        items.append(row[0])

    #aliakset
    if target == "manual" and "Hyper-X manual" in items:
        target = "Hyper-X manual"

    if target == "Hyper-X manual" and target in items:
        sql = "SELECT descript FROM DESCRIPTION WHERE description_id = 32"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            print (row[0])
    else:
        print("You can't read", target)
        
   
def examine(target):


    cur = db.cursor()
    sql = "SELECT room_id FROM PLAYER"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        roomid=str(row[0])
    
    objects = []
    cur = db.cursor() 
    sql = "SELECT name FROM OBJECT WHERE room_id = (SELECT room_id FROM PLAYER)"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        objects.append(row[0])

    items = []
    sql = "SELECT name FROM ITEM WHERE room_id = (SELECT room_id FROM PLAYER) OR player_id = 1"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        items.append(row[0])

    #aliakset
    if target == "password terminal" and roomid == "2":
        target = "Flight Deck password terminal"
    if target == "terminal" and roomid == "2":
        target = "Flight Deck password terminal"
    if target == "flight deck password terminal":
        target = "Flight Deck password terminal"
    if target == "switch" and roomid == "3":
        target = "light switch"
    if target == "switch" and roomid == "5":
        target = "oxygen switch"
    if target == "pc" and roomid == "1":
        target = "computer"
    if target == "mask" and "breathing mask" in items:
        target = "breathing mask"
    if target == "mask" and "breathing mask with oxygen tank" in items or target == "breathing mask" and "breathing mask with oxygen tank" in items:
        target = "breathing mask with oxygen tank"
    if target == "tank" and "oxygen tank" in items:
        target = "oxygen tank"
    if target == "pod 1" and roomid == "1":
        target = "sleeping pod 1"
    if target == "pod 2" and roomid == "1":
        target = "sleeping pod 2"
    if target == "pod 3" and roomid == "1":
        target = "sleeping pod 3"
    if target == "pod 4" and roomid == "1":
        target = "sleeping pod 4"
    if target == "pod 5" and roomid == "1":
        target = "sleeping pod 5"
    if target == "manual" and "Hyper-X manual" in items:
        target = "Hyper-X manual"
    if target == "control panel" and roomid == "3":
        target = "Spaceship control panel"
    if target == "tool" and "Hyper-X 1872" in items:
        target = "Hyper-X 1872"
    if target == "pod" and roomid == "4":
        target = "escape pod"
    if target == "cabinet" and roomid == "5":
        target = "oxygen cabinet"
    if target == "cabinet" and roomid == "8":
        target = "steel reinforced cabinet"
    if target == "engine" and roomid == "10":
        target = "hyperdrive engine"
    
    if target in objects:
        sql = "SELECT descript FROM DESCRIPTION WHERE description_id = (SELECT description_id FROM OBJECT WHERE name = '" + target + "')"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            print (row[0])

    elif target in items:
        sql = "SELECT descript FROM DESCRIPTION WHERE description_id = (SELECT description_id FROM ITEM WHERE name = '" + target + "')"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            print (row[0])

    elif target == "room" or target == "around":
        sql = "SELECT descript FROM DESCRIPTION WHERE description_id = (SELECT description_id FROM ROOM WHERE room_id = (SELECT room_id FROM PLAYER))"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            print (row[0])
            
    elif target == "pod" and roomid == "1" or target == "sleeping pod" and roomid == "1" or target == "pods" and roomid == "1" or target == "sleeping pods" and roomid == "1":
        inputti = input("There are five pods in this room. Which pod did you mean?(insert a number): ")
        inputti = str(inputti)
        examine("sleeping pod " +inputti)   

    elif target == "part" and roomid == "4":
        print("This is a functioning engine part of the escape pod engine.")

    elif target == "lever" and roomid == "7":
        print("This lever can be used to open the escape hatch.")
        
    else:
        print("Can't find", target, "nearby.")
    return

def take(target):
    cur=db.cursor()
    cur = db.cursor()
    sql = "SELECT room_id FROM PLAYER"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        roomid=str(row[0])
    
    items=[]   
    sql = "SELECT name FROM ITEM WHERE room_id = (SELECT room_id FROM PLAYER)"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        items.append(row[0])

    #aliakset 
    if target == "tool" and "Hyper-X 1872" in items or target == "hyper-x 1872" and "Hyper-X 1872" in items or target == "hyper-x" and "Hyper-X 1872" in items:
        target = "Hyper-X 1872"
    if target == "mask" and "breathing mask" in items:
        target = "breathing mask"
    if target == "tank" and "oxygen tank" in items:
        target = "oxygen tank"
    if target == "manual" and "Hyper-X manual" in items:
        target = "Hyper-X manual"
        
    sql= "UPDATE ITEM SET player_id=1, room_id=NULL\
    WHERE name='" +target+ "' AND room_id=(SELECT room_id FROM player)"
    cur.execute(sql)
    if cur.rowcount==1:
        print("You take " +target)
        if target=="breathing mask":
            sql= "UPDATE ROOM SET description_id = 37 WHERE room_id = 3"
            cur.execute(sql)
        if target=="Hyper-X manual":
            sql= "UPDATE ROOM SET description_id = 38 WHERE room_id = 9"
            cur.execute(sql)
        if target=="Hyper-X 1872":
            sql= "UPDATE ROOM SET description_id = 39 WHERE room_id = 11"
            cur.execute(sql)
    else:
        if target == "part" and roomid == "4" or target == "engine part" and roomid == "4":
            print("This engine part cannot be detached without a tool.")
        else:
            print("You can't take that.")
    
    return cur.rowcount
    
def open(target):
    cur = db.cursor()
    sql = "SELECT room_id FROM PLAYER"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        roomid=str(row[0])
    #aliakset
    if target == "cabinet" and roomid == "5":
        target = "oxygen cabinet"
    if target == "cabinet" and roomid == "8":
        target = "steel reinforced cabinet"

    objects = []
    sql = "SELECT name FROM OBJECT WHERE room_id = (SELECT room_id FROM PLAYER)"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        objects.append(row[0])

    if target == "pod 1" and roomid == "1":
        target = "sleeping pod 1"
    if target == "pod 2" and roomid == "1":
        target = "sleeping pod 2"
    if target == "pod 3" and roomid == "1":
        target = "sleeping pod 3"
    if target == "pod 4" and roomid == "1":
        target = "sleeping pod 4"
    if target == "pod 5" and roomid == "1":
        target = "sleeping pod 5"
        
    #open oxygen cabinet
    if target == "oxygen cabinet" and target in objects:
        print("You have opened the cabinet. There is an oxygen switch inside.")
        sql = "UPDATE OBJECT SET room_id = 5 WHERE object_id = 12"
        cur.execute(sql)
        
    #open steel reinforced cabinet
    elif target == "steel reinforced cabinet" and target in objects:
        sql = "SELECT player_id FROM ITEM WHERE item_id = 3"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            sijainti1 = str(row[0])
        if sijainti1=="1":
            print("You have opened the cabinet. It's empty.")
        else: 
            print("You have opened the cabinet. There is an oxygen tank inside.")
            sql = "UPDATE ITEM SET room_id = 8 WHERE item_id = 3"
            cur.execute(sql)

        
    else:
        if target in objects:
            print("You can't open", target,".")
        else:
            print("Can't find", target,".")

def close(target):
    cur = db.cursor()
    sql = "SELECT room_id FROM PLAYER"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        roomid=str(row[0])

    objects = []
    sql = "SELECT name FROM OBJECT WHERE room_id = (SELECT room_id FROM PLAYER)"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        objects.append(row[0])

    #aliakset
    if target == "cabinet" and roomid == "5":
        target = "oxygen cabinet"
    if target == "cabinet" and roomid == "8":
        target = "steel reinforced cabinet"

    #close oxygen cabinet
    if target == "oxygen cabinet" and target in objects:
        print("You have closed the cabinet.")
        sql = "UPDATE OBJECT SET room_id = NULL WHERE object_id = 12"
        cur.execute(sql)

    #close steel reinforced cabinet
    elif target == "steel reinforced cabinet" and target in objects:
        print("You have closed the cabinet.")
        sql = "UPDATE ITEM SET room_id = NULL WHERE item_id = 3"
        cur.execute(sql)
        
    else:
        if target in objects:
            print("You can't close", target,".")
        else:
            print("Can't find", target,".")
    
def pos():
    cur = db.cursor()
    sql = "SELECT shortdescription FROM ROOM WHERE room_id = (SELECT room_id FROM PLAYER)"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        print (row[0])
    return

def go(direction):
    cur = db.cursor()
    #aliakset
    if direction == "e":
        direction = "east"
    if direction == "n":
        direction = "north"
    if direction == "s":
        direction = "south"
    if direction == "w":
        direction = "west"
    if direction == "u":
        direction = "up"
    if direction == "d":
        direction = "down"
        
    sql = "SELECT room_id FROM PLAYER"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        mista=str(row[0])
        
    sql = "SELECT minne FROM MOVEMENT WHERE direction = '" + direction + "'AND mista = '" + mista + "'"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        roomid = str(row[0])
        
    if cur.rowcount==1:
        #fire
        sql = "SELECT fire FROM ROOM WHERE room_id = '" + roomid + "'"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            fire = str(row[0])
        #dark
        sql = "SELECT dark FROM ROOM WHERE room_id = '" + roomid + "'"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            dark = str(row[0])
        #locked
        sql = "SELECT locked FROM ROOM WHERE room_id = '" + roomid + "'"
        cur.execute(sql)
        res = cur.fetchall()
        for row in res :
            locked = str(row[0])
        
        if fire == "1":
            print("As you open the door to the engine room you see an engulfing fire raging in the room. You step back to the southern corridor.")
        elif dark == "1":
            print("It's too dark to move there.")
        elif locked == "1":
            print("The door is locked.")
        else:
            sql = "UPDATE PLAYER SET room_id = '" + roomid + "'"
            cur.execute(sql)
            pos()
            sql = "SELECT visited FROM ROOM WHERE room_id = (SELECT room_id FROM PLAYER)"
            cur.execute(sql)
            res = cur.fetchall()
            for row in res :
                visited = str(row[0])
            if visited == "0": 
                sql = "SELECT descript FROM DESCRIPTION WHERE description_id = (SELECT description_id FROM ROOM WHERE room_id = (SELECT room_id FROM PLAYER))"
                cur.execute(sql)
                res = cur.fetchall()
                for row in res :
                    print (row[0])
                sql = "UPDATE ROOM SET visited = 1 WHERE room_id = (SELECT room_id FROM PLAYER)"
                cur.execute(sql)
            
    else:
        print("You can't go that way")
    return

def combine(target):
    cur = db.cursor()
    sanalista=target.split(" with ")
    #print(sanalista)

    items = []
    sql = "SELECT name FROM ITEM WHERE player_id = 1"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        items.append(row[0])

    #aliakset
    if target == "tool" and "Hyper-X 1872" in items or target == "hyper-x 1872" and "Hyper-X 1872" in items or target == "hyper-x" and "Hyper-X 1872" in items:
        target = "Hyper-X 1872"
    if target == "mask" and "breathing mask" in items:
        target = "breathing mask"
    if target == "mask" and "breathing mask with oxygen tank" in items or target == "breathing mask" and "breathing mask with oxygen tank" in items:
        target = "breathing mask with oxygen tank"
    if target == "tank" and "oxygen tank" in items:
        target = "oxygen tank"
    if target == "manual" and "Hyper-X manual" in items:
        target = "Hyper-X manual"

    if sanalista[0] in items and sanalista [1] in items:
        if sanalista[0] == "breathing mask" and sanalista[1] == "oxygen tank" or sanalista[0] == "oxygen tank" and sanalista[1] == "breathing mask":
            sql = "UPDATE ITEM SET player_id = 1, object_id = NULL, room_id = NULL WHERE name = 'breathing mask with oxygen tank'"
            cur.execute(sql)
            sql = "UPDATE ITEM SET player_id = NULL, object_id = NULL, room_id = NULL WHERE name = 'breathing mask'"
            cur.execute(sql)
            sql = "UPDATE ITEM SET player_id = NULL, object_id = NULL, room_id = NULL WHERE name = 'oxygen tank'"
            cur.execute(sql)
            print("You have succesfully attached the oxygen tank into your breathing mask. The mask is now useable.")
        else:
            print("Cant combine", sanalista[0], "with", sanalista[1])
    else:
        if sanalista[0] in items:
            print("You don't have", sanalista[1])
        elif sanalista[1] in items:
            print("You don't have", sanalista[0])
        else:
            print("You don't have", sanalista[0], "and", sanalista[1])

def inventory():
    cur=db.cursor()
    sql= "SELECT name FROM ITEM WHERE player_id=1"
    cur.execute(sql)
    res=cur.fetchall()
    if cur.rowcount>=1:
        print("INVENTORY:")
        for row in res:
            print(" - " + row[0])
    else:
        print("Your inventory is empty")
    return

def alku():
    print("              _____ ___________ _____ _   _ _____ _______   __")
    print("             /  ___|  ___| ___ \  ___| \ | |_   _|_   _\ \ / /")
    print("             \ `--.| |__ | |_/ / |__ |  \| | | |   | |  \ V / ")
    print("              `--. \  __||    /|  __|| . ` | | |   | |   \ /  ")
    print("             /\__/ / |___| |\ \| |___| |\  |_| |_  | |   | |  ")
    print("             \____/\____/\_| \_\____/\_| \_/\___/  \_/   \_/  ")
    print("")
    x=input("                       PRESS ENTER TO START GAME")
    print("")
    print("To see list of commands type 'help'")
    print("")
    sql = "SELECT descript FROM DESCRIPTION WHERE description_id = (SELECT description_id FROM ROOM WHERE room_id = (SELECT room_id FROM PLAYER))"
    cur.execute(sql)
    res = cur.fetchall()
    for row in res :
        print (row[0])
    sql = "UPDATE ROOM SET visited = 1 WHERE room_id = (SELECT room_id FROM PLAYER)"
    cur.execute(sql)

def loppu():
    print("")
    print("You are now successfully operating the spaceship's controls. You type in the coordinates for the closest space-station and start making your way back to safety. Congratulations!")

    print("                  _____ _   _  _____   _____ _   _______  ")
    print("                 |_   _| | | ||  ___| |  ___| \ | |  _  \ ")
    print("                   | | | |_| || |__   | |__ |  \| | | | | ")
    print("                   | | |  _  ||  __|  |  __|| . ` | | | | ")
    print("                   | | | | | || |___  | |___| |\  | |/ /  ")
    print("                   \_/ \_| |_/\____/  \____/\_| \_/___/   ")
    print(" ")
    print("     We thank you for playing our game and sincerely hope that you enjoyed it. ")
    print(" ")
    print("It took you" ,steps, "steps to complete the game")
    x=input("Press ENTER to exit.")
    sys.exit(0)
    
def help():
    print("commands:")
    print("examine (something),")
    print("look around,")
    print("go (direction),")
    print("take (something),")
    print("combine (something) with (something),")
    print("equip,")
    print("use (something),")
    print("use (something) on (something),")
    print("open (something),")
    print("inventory")

def map():
    print(" _______________________________________ ")
    print("|                   _______             |")
    print("| __  __   _   ___ |       |       N    |") 
    print("||  \/  | /_\ | _ \|Flight |     W-|-E  |")
    print("|| |\/| |/ _ \|  _/|deck   |       S    |")
    print("||_|  |_/_/ \_\_|  |_______|            |")
    print("|        _______    ___|___     _______ |")
    print("|       |       |  |North  |   |       ||") 
    print("|       | Cryo  |__|corrido|___|Escape ||")
    print("|       | room  |  |r      |   |pods   ||")
    print("|       |_______|  |_______|   |_______||")
    print("|                   ___|___     ___|___ |")
    print("|                  |Middle |   |pressur||") 
    print("|                  |corrido|___|e      ||")
    print("|                  |r      |   |room   ||")
    print("|                  |_______|   |_______||")
    print("|        _______    ___|___     _______ |")
    print("|       |Upper  |  |South  |   |Crew   ||")  
    print("|       |engine |__|corrido|___|quarter||")
    print("|  _____|room   |  |r      |   |s      ||")
    print("| |Lower|_______|  |_______|   |_______||")
    print("| |engine |                     ___|___ |")
    print("| |room   |                    |Captain||")  
    print("| |_______|                    |'s  qua||")
    print("|                              |rters  ||")
    print("|USS Serenity                  |_______||")
    print("|_______________________________________|")
    
alku()
steps = 0
x=1
while x == 1:
    print("")
    komento= input(">")
    sanalista=komento.split(" ")
    #pituus = len(sanalista)-1
    if sanalista[0]=="examine" or sanalista[0]=="inspect" or sanalista[0]=="look":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        examine(target)
    elif sanalista[0]=="go" or sanalista[0]=="move":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        steps = steps + 1
        go(target)
    elif sanalista[0]=="use":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        use(target)
    elif sanalista[0]=="combine":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        combine(target)
    elif sanalista[0]=="open":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        open(target)
    elif sanalista[0]=="close":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        close(target)
    elif sanalista[0]=="take":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        take(target)
    elif sanalista[0]=="pick" and sanalista[1]=="up":
        sanalista.remove(sanalista[0])
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        take(target)
    elif sanalista[0]=="equip":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        equip(target)
    elif sanalista[0]=="inventory" or sanalista[0]=="inv" or sanalista[0]=="i":
        inventory()
    elif sanalista[0]=="read":
        sanalista.remove(sanalista[0])
        target = " ".join(str(i) for i in sanalista)
        read(target)
    elif sanalista[0]=="why" or sanalista[0]=="why?":
        print("I don't know.")
    elif sanalista[0]=="help" or sanalista[0]=="h":
        help()
    elif sanalista[0]=="map":
        map()
    else:
        print("unknown command")
