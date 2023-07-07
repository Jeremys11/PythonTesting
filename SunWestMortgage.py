import pandas as pd
import sys


if __name__ == "__main__":

    "1,2,3,4,20,90:L10;1,5,3,6,20,91:L20;1,10,3,12,20,92:L30"
    bigString = ""
    for line in sys.stdin:

        #USE rstrip() to remove formatting from line
        bigString = line.rstrip()

        #Empty arrays to be used to build dataframe
        columns = []
        index = []
        data = []

        #Removing leading and trailing quotes
        splitCol = bigString.strip("\"")

        #Splitting up columns delimited by semicolon
        splitCol = splitCol.split(";")

        #Remove empty quotes from list
        while("" in splitCol):
            splitCol.remove("")

        #Separating column header from the rest of data
        for col in splitCol:
            col = col.split(":L")
            columns.append(col[1])

            col = col[0].split(',')

            #Iterate through to get row indecies and column data
            temp = []
            for val in range(len(col)):
                if val%2 == 0:
                    if col[val] not in index:
                        index.append(col[val])
                else:
                    temp.append(col[val])
            data.append(temp)

        #Get column names and column data in dictionary relationship
        columnNameData = {}
        for col in range(len(columns)):
            columnNameData[columns[col]] = data[col]

        #Use dictionary for column names and data use index as index
        myDataFrame = pd.DataFrame(data=columnNameData,index=index)

        print(myDataFrame)