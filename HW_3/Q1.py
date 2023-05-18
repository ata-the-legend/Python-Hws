
#Q1

# import this

def main():
    """
    This is the main func of Q1
    """
    replacements = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), 
                    ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'), 
                    ('ten', '10'), ('eleven', '11'), ('twelve', '12'), ('thirteen', '13'), ('fourteen', '14'), 
                    ('fifteen', '15'), ('sixteen', '16'), ('seventeen', '17'), ('eighteen', '18'), ('nineteen', '19'), 
                    ('twenty', '20')
                    ]
    replacements.reverse()

    with open('HW_3/Zen.txt', 'r+', encoding= 'utf-8') as f:
        
        # my_text = f.read()
        # for old, new in replacements:
        #     new_text = my_text.replace(old, new)
        
        lines = f.readlines()
        new_line_list = []
        new_text_list = []
        #print(lines)
        for line in lines:
            # print(line)
            for word in line.split():
                for i in range(20):
                    if word == replacements[i][0]:
                        word = replacements[i][1]
                        break
                new_line_list.append(word)
                # print(new_line_list)
            new_line = ' '.join(new_line_list)
            new_line_list = []
            # print(new_line)
            new_text_list.append(new_line)
        new_text = '\n'.join(new_text_list)


    with open('new_Zen.txt', 'w+', encoding='utf-8') as f:
        f.write(new_text)


if __name__ == '__main__':
    main()