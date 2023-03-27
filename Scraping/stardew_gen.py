
## Return a string of column headers
def getAllCols(cols):
    txt = ""
    for col in cols:
        if cols.index(col) == 0:
            txt = txt + col
        else:
            txt = txt + ","+ col
    return txt
   


def getTheFirst(rows):
    txt = ""
    for row in rows:
        if rows.index(row) == 0 and type(row[0]) == str:
            txt =  txt + "'" + str(row[0]) 
        elif rows.index(row) == 0 and type(row[0]) != str:
            txt =  txt + str(row[0]) 
        elif rows.index(row)!= 0 and type(row[0]) != str:
            txt = txt + "," + str(row[0])
        else:
            txt = txt + "," + str(row[0]) 
    return txt



def getALLData(rows):
    txt = ""
    for x in range(0,len(rows[0])):
        if x == 0:
            txt =  txt + "(" + getTheFirst(rows) + ")\n"
        else:
            txt =  txt + ",(" + getTheFirst(rows) + ")\n"
        for row in rows:
            row.pop(0)
            rows = rows
    return txt




## Complete Function
def makeSQL(database, columns, rows):
    column = getAllCols(columns)
    row = getALLData(rows)
    return("INSERT INTO {} ({}) VALUES {};".format(database, column,row))


# LISTS
li1 = ['BlueJazz', 'Cauliflower','Coffee Bean']
li2 = [7,12,10]
li3 = [1,1,1]


# VARIABLES
database = 'Season'
columns = ['name', 'season','duration']
rows = [li1, li2, li3]

## FINAL FUNCTION: sample
#makeSQL(database, columns, rows)




###############
## to split columns 

test = ['a', 'b', 'c', 'd', 'e', 'f']

def splitList(lst, number):
    for i in range(0, len(lst), number):
        yield lst[i:i + number]


def SplitIntoCol(lst, chunks):
    for chunk in splitList(lst, chunks):
        print(chunk)


# SplitIntoCol(test,4)

