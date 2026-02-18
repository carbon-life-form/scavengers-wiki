f = open('input.txt', 'r')
header = True
for line in f:
    s=''
    data = line.strip().split('\t')
    print('<tr>')

    for d in data:
        if header:
            print(f'<th>{d}</th>')
        else:
            print(f'<td>{d}</td>')
    header = False
    print('</tr>')
f.close()