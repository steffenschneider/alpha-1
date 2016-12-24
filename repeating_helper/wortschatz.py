def delete_duplicates():
    import re
    import os
    # read file into 2D-list
    if os.name == 'posix':
        path = "/home/kame/Dropbox/data/"
    elif os.name == 'nt':
        path = "C:/Users/steffen.schneider/Dropbox/data/"
    filename = "wortschatz.txt"
    file_ = path + filename
    file_input = open(file_, "r")  # todo unicodeDecodeError
    text = file_input.readlines()  # .read() reads only one line
    list_original = list(text)
    # print("len list_original: " + str(len(list_original)))
    # print(list_original)

    list_separated = []
    for i in range(len(list_original)):
        list_original[i] = re.sub("\n", "", list_original[i])
        list_original[i] += "\t"
        # print("list_original i: " + str(i))
        # print("size_list_separated: " + str(len(list_separated)))
        list_separated.append([])
        list_separated[i].append(list_original[i].split("\t")[0])
        try:
            list_separated[i].append(list_original[i].split("\t")[1])
        except ValueError:
            list_separated[i].append("")
    # print("len list_separated: " + str(len(list_separated)))
    # print("list_separated")
    # for i in list_separated:
    #   print(i)

    # for all element in first column
    list_first_column = []
    for i in list_separated:
        list_first_column.append(i[0])
    list_first_column = sorted(list(set(list_first_column)))
    list_first_column.sort(key=lambda x: x.lower())
    # print("len list_first_column: " + str(len(list_first_column)))

    # take the element first_element
    list_output = []
    for j in range(len(list_first_column)):
        # print("j: " + str(j))
        list_output.append([[], [], [], []])
        # print(list_first_column[j])
        list_output[j][0] = list_first_column[j]
        # put all element of the second column with the same first_element together
        column_counter = 1
        for k in range(len(list_original)):
            # print("k: " + str(k))
            # print(list_separated[k][0])
            if list_separated[k][0] == list_first_column[j]:
                try:
                    list_output[j][column_counter] = list_separated[k][1].split("\n")[0]
                except ValueError:
                    pass
                column_counter += 1
        list_output[j][3] = "\n"
    # print("len list_output: " + str(len(list_output)))
    # print("list_output")
    # for i in list_output:
    #    print(i)

    # list to string
    for i in range(len(list_output)):
        if not list_output[i][2]:
            list_output[i][2] = ""
        input_ = (24 - len(list_output[i][0])) * " " + "\t"
        list_output[i] = list_output[i][0] + input_ + list_output[i][1].strip() + "  " + list_output[i][2] + \
                         list_output[i][3]

    with open(r"/home/kame/Dropbox/data/wortschatz.txt", "w") as myfile:
        for d in range(len(list_output)):
            # print("d: " + str(d))
            # ignore empty lines
            # print(list_output[d])
            if len(list_output[d][0]) == " ":
                pass
            else:
                myfile.write(list_output[d])

    n_deleted = len(list_original) - len(list_output)
    if n_deleted > 0:
        print("deleted --> " + str(n_deleted) + " duplicate words in word list")


if __name__ == '__main__':
    delete_duplicates()
