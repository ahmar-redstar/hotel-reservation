# bed and breakfast program Stage 1


# read the program and process commands
# commands can be upper or lower case


import datetime
from collections import namedtuple
#STAGE 1
rooms_list = []
resList = []
CONFORMATION = 0

def create_date_obj(string:str) -> "date":
    temp = string.strip().split('/')
    return datetime.date(int(temp[2]), int(temp[0]), int(temp[1]))


def handle_commands( dataline: str ) -> None:
    '''Handle the specified command'''
     

    # we strip the command when we put it in
    # since we want upper or lower, we have to put it in a specific case--> let's use lower case
    newline = dataline.strip(' ')
   # print(dataline)
    command = newline[0:2]
    command_lower = command.lower()
    Reserve = namedtuple('Reserve', 'room arv dep name conformation')

    
    if command_lower == 'ab':
        # actual room number data is after the command, starting from the 3rd character
        ab_data = newline[2:]
        
        # take whitespace off the data
        ab_data.strip()

        # add the room number to the bedrooms list
        if int(ab_data) in rooms_list:
            print("Room {} already exists".format(int(ab_data)))
        else:
            rooms_list.append( int(ab_data) )
    
    elif command_lower == 'bl':
        print('Number of bedrooms in service:', len(rooms_list))
        print('------------------------------------')
        for room in rooms_list:
            print(room)
                
    elif command_lower == 'pl':
        print(dataline[2:].strip())
        
    elif command_lower == '**':
        return
    
    elif command_lower == 'bd':
        room_value = dataline.strip()[2:]
        list_size = len(rooms_list)
        
        
        
        if(int(room_value) in rooms_list):
            rooms_list.pop(rooms_list.index(int(room_value)))
            print("Room {} was removed".format(int(room_value)))       
        else:
            print("Room {} does not exist".format(int(room_value)))

    elif command_lower == 'nr':
        storeList = []

        

        storeList = dataline.strip().split()

         
        
        if int(storeList[1]) in rooms_list:

            arvial = create_date_obj(storeList[2])
            depart = create_date_obj(storeList[3])

            isConflict = False
            



            for i in resList:

                if i.room == int(storeList[1]):
                    if create_date_obj(i.arv)< arvial < create_date_obj(i.dep):
                        print("Sorry, can't reserve room {} ({} to {});".format(i.room, storeList[2], storeList[3]))
                        print("    it's already booked (Conf. #{})".format(i.conformation))
                        isConflict = True
                              
                    
                    
                
            if arvial < depart and not isConflict:
            
                global CONFORMATION
                CONFORMATION += 1
                tempReserve = Reserve(int(storeList[1]), storeList[2],storeList[3].strip(),storeList[4].strip() + ' ' + storeList[5].strip(),  CONFORMATION)
                resList.append(tempReserve)
                print('Reserving room {} for {}  -- conformation {}'.format(tempReserve.room, tempReserve.name,tempReserve.conformation))
                print('    (arrving {} , departing {}'.format(tempReserve.arv, tempReserve.dep))

            else:
                print("Sorry, can't reserve room {}".format(storeList[1]))
                print("can't leave before you arive")

        else:
            print("Sorry; can't reserve room {}; room not in service".format(storeList[1]))

            
                

    elif command_lower == 'rl':

        print('No. Rm. Arrive      Depart     Guest')

        print('------------------------------------------------')

        
        
        for i in resList:

            print('{:3} {:3} {:10} {:10} {}'.format(i.conformation, i.room, i.arv, i.dep, i.name))

    elif command_lower == 'rd':

        tempData = int(dataline.strip()[2:])

        
        isFound = False
        
        for i in resList:

            if i.conformation == tempData:

                resList.remove(i)

                isFound = True

        if not isFound:
            print("Sorry, can't cancel reservation; no confirmation number", tempData)
        

        
        
                

            
            
                  
                

        

    else:
        handle_invalid_command(command)
        
    return
        
def handle_invalid_command( command: str ) -> None:
    print("Sorry,", command, "isn't a valid command")
    return


#STAGE2


infile = open('bandbTest.txt', 'r')

file_lines = infile.readlines()

for line in file_lines:
    handle_commands(line)

infile.close()
    

