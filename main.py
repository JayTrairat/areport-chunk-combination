def main():
    for index in range(1, 28):
        with open('assets/google_sheet_export_position_' + str(index) + '.csv', 'r', encoding='utf8') as source:
            contents = [content.strip().split('|')[0] for content in source.readlines()]
        with open('assets/naming_elements/pos_' + str(index) + '.txt', 'w', encoding='utf8') as outp:
            outp.write('\n'.join(contents))

if __name__ == '__main__':
    main()
