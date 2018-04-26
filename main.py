import re
from functools import reduce
from collections import OrderedDict


def main():
    word_list = []
    for index in range(1, 28):
        with open('assets/naming_elements/important_word_pos_' + str(index) + '.txt', 'r', encoding='utf8') as source:
            contents = [content.strip().split('|') for content in source.readlines()]
            contents = [content[:] for content in contents]
            for content in contents:
                for item in content:
                    word_list.append(item)

    word_list = (OrderedDict.fromkeys(word_list))
    word_list = (list(word_list.items()))
    word_list = [content[0] for content in word_list]

    with open('assets/naming_elements/important_words.txt', 'w', encoding='utf8') as outp:
        outp.write('\n'.join(word_list))

if __name__ == '__main__':
    main()
