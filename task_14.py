with open("file_for_words_14_1.txt", "r") as file_1, \
        open("file_for_words_14_2.txt", "r") as file_2:
            for line_file_1, line_file_2 in zip(file_1, file_2):
                print(f"{line_file_1} {line_file_2}")

file_1.close()
file_2.close()
