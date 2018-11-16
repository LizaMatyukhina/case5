import urllib.request

i = 0
with open('input.txt') as f_in:
    with open('output.txt', 'w') as f_out:
        html_code = f_in.readlines()
        for i in range(0, len(html_code)):
            url = html_code[i]
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)
            part_name = text.find("player-name")
            name = text[text.find('>', part_name) + 1:text.find('&', part_name)]
            print(name, file = f_out)
            part_values = text.find("player-totals")
            values = text[text.find('>', part_values) + 1: text.find('/tr', part_values)]
            values = values.replace('TOTAL', '')
            values = values.replace('t', '')
            values = values.replace('n', '')
            values = values.replace('\\', '')
            values = values.replace('</d>', '')
            values = values.replace('<d>', ' ')
            values = values.replace('<', '')
            values = values.replace(',', '')
            a = values.split(' ')
            COMP = a[1]
            ATT = a[2]
            YDS = a[4]
            TD = a[6]
            print(COMP, file = f_out)
            print(ATT, file = f_out)
            print(YDS, file = f_out)
            print(TD, file = f_out)