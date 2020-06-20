import re
with open('401k-symbols.txt') as f:
    lines = f.readlines() # list containing lines of file
    # columns = [] # To store column names
    #
    i = 1
    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        print('\n\n')
        print(line)
        if line:
            if i % 3 == 1:
                columns = [item.strip() for item in line.split('(')]
                print(columns[0])
                print(columns[1][0:-1])
            elif i % 3 == 0:
                columns = [item.strip() for item in line.split('Investments')]
                print(columns[0])
                print(dir(re.search('\d+', columns[1])))

            #                 d = {} # dictionary to store file data (each line)
            #                 data = [item.strip() for item in line.split(',')]
            #                 for index, elem in enumerate(data):
            #                     d[columns[index]] = data[index]
            #
            #                 my_list.append(d) # append dictionary to list
            #
            i = i + 1
# # pretty printing list of dictionaries
# print(json.dumps(my_list, indent=4))