def main():
    important_words = {}
    for index in range(1, 11):
        with open('assets/important_words/important_words_pos_' + str(index) + '.txt', 'r', encoding='utf8') as source:
            contents = [content.strip() for content in (source.readlines())]
            important_words[index] = contents
    list_of_name = [
        pos_1 + pos_2 + pos_3 + pos_4 + pos_5 + pos_6
        for pos_1 in important_words[1]
        for pos_2 in important_words[2]
        for pos_3 in important_words[3]
        for pos_4 in important_words[4]
        for pos_5 in important_words[5]
        for pos_6 in important_words[6]
    ]

    with open('assets/naming_list_6_pos.txt', 'w', encoding='utf8') as outp:
        for item in list_of_name:
            outp.write(item)
            outp.write('\n')

if __name__ == '__main__':
    main()
