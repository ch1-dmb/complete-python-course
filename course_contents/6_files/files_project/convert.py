# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json
csv_read = open('csv_file.txt', 'r')
csv_list = csv_read.readlines()
csv_read.close()

csv_list = [line.strip() for line in csv_list]
print(csv_list)

csv_collection=[]
for i in csv_list:
    new_list = i.split(",")
    csv_dic = {
        'club': new_list[0],
        'country': new_list[1],
        'city': new_list[2]
    }
    csv_collection.append(csv_dic)


convert_file = open("csv_file.txt", 'w')
json.dump(csv_collection, convert_file)



# json_data =  json.dumps(csv_collection, indent=4)

# with open("csv_file.json", 'w') as convert_file:
    # json.dump(csv_collection, convert_file, indent=4)

# convert_file.write(json_data)
# convert_file.close()


# [{"club": "Manchester United", "country": "UK", "city": "Manchester"}, {"club": "Real Madrid", "country": "Spain", "city": "Madrid"}, {"club": "Juventus", "country": "Italy", "city": "Turin"}]