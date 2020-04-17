# 讀取檔案(刪除\n空白.用\t切割)
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip().split('\t'))
        return lines


# 篩選欄位
def field(lines):
    fields = []
    for fie in lines:
        if '2019/' in fie[0]:     # 如果裡面含有'2019/'就忽略
            continue
        elif not str(fie[0]):     # 如果是空行就忽略
            continue
        elif len(fie) > 1:        # 如果是清單禮物件>1,就從第2個物件開始加入清單
            fields.append(fie[1:])
        else:                     # 除了以上條件以外就直接加入清單
            fields.append(fie)
    return fields


# 格式轉換
def convert(lines):
    news = []
    for new in lines:
        if len(new) > 1:
            if new[0] == 'Yuzzzzzz':
                new[0] = 'Yuz'
            news.append(new[0] + '： ' + new[1])
        else:
            news.append(new)
    return news


# 儲存檔案
def save(file_name, lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(str(line) + '\n')


def main():
    filename = 'yuzzzzzzzzzzz.txt'
    lines = read_file(filename)
    lines = field(lines)
    lines = convert(lines)
    # save('[LINE]fa_output.csv',lines)
    # save('[LINE]fa_output.txt',lines)
    save('[LINE]fa_output.doc',lines)
main()