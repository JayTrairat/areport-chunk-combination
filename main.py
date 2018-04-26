import re
def main():
    word_list = {}
    for index in range(1, 28):
        with open('assets/naming_elements/pos_' + str(index) + '.txt', 'r', encoding='utf8') as source:
            contents = [content.strip().split('|')[0] for content in source.readlines()]
            contents = [content for content in contents if not content.isdigit() and not re.match("-", content)]
            contents = [content for content in contents]
            word_list[index] = contents
        with open('assets/naming_elements/important_word_pos_' + str(index) + '.txt', 'w', encoding='utf8') as outp:
            outp.write('|'.join(word_list[index]))

    # naming_list = [
    #     pos_1 + pos_2 + pos_3 + pos_4 + pos_5 + pos_6 + pos_7 + pos_8 + pos_9 + pos_10
    #     for pos_1 in word_list[1]
    #     for pos_2 in word_list[2]
    #     for pos_3 in word_list[3]
    #     for pos_4 in word_list[4]
    #     for pos_5 in word_list[5]
    #     for pos_6 in word_list[6]
    #     for pos_7 in word_list[7]
    #     for pos_8 in word_list[8]
    #     for pos_9 in word_list[9]
    #     for pos_10 in word_list[10]
    # ]
    # print(naming_list)
    # print(word_list)

    #     with open('assets/google_sheet_export_position_' + str(index) + '.csv', 'r', encoding='utf8') as source:
    #         contents = [content.strip().split('|')[0] for content in source.readlines()]
    #     with open('assets/naming_elements/pos_' + str(index) + '.txt', 'w', encoding='utf8') as outp:
    #         outp.write('\n'.join(contents))

if __name__ == '__main__':
    main()
