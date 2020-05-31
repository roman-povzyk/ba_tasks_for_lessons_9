with open("file_for_words_10.txt", "r") as file:
    read_data = file.read()

string_list = read_data.split(" ")
string_dict = {}
count = []

for i in range(len(string_list)):
    count.append(read_data.count(string_list[i]))
    string_dict[string_list[i]] = count[i]

print(string_dict)
file.close()