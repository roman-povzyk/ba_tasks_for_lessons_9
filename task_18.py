with open("file_for_words_10.txt", "r") as file:
    data_with_commas = file.read()
    data_without_commas = data_with_commas.replace(",", " ")
    string_list = data_without_commas.split(" ")
    print(f"Кількість слів — {len(string_list)}")

file.close()