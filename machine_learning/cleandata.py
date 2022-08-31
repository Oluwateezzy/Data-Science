import pandas as pd

list_data = []

with open("./text_data.csv", 'r') as file:
        for line in file:
            list_data.append(line.split(","))
#train_data2 = pd.DataFrame(list_data)

for line in list_data:
    del line[0:1]

#for line in list_data:
#    print(line[0])
    
print(pd.DataFrame(list_data).index)