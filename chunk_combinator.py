def main():
    important_words = {}
    for index in range(1, 11):
        with open('areport-chunk-combination/assets/important_words/important_words_pos_' + str(index) + '.txt', 'r', encoding='utf8') as source:
            contents = [content.strip() for content in (source.readlines())]
            important_words[index] = contents
    list_of_name = [
        pos_1 + pos_2
        for pos_1 in important_words[1]
        for pos_2 in important_words[2]
    ]

    with open('areport-chunk-combination/assets/naming_list_6_pos.txt', 'w', encoding='utf8') as outp:
        for item in list_of_name:
            outp.write(item)
            outp.write('\n')

if __name__ == '__main__':
    main()
