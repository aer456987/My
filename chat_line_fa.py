# 讀取檔案(刪除\n空白.用\t切割)
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip().split('\t'))
        # print(lines)
        return lines

# 刪除不要的欄位(日期.空行)
def field(lines):
    fields = []
    for fie in lines:
        if '2019/' in fie[0]:  # 如果裡面含有'2019/'就忽略
            continue
        elif not str(fie[0]):  # 如果是空行就忽略
            continue
        fields.append(fie)
    return fields

# 篩選要加入的欄位
def del_line(lines):
    news = []
    for new in lines:
        if len(new) == 1:  # 如果是清單禮物件=1,就加入清單
            news.append(new)
        elif len(new) > 1:  # 如果是清單禮物件>1,則從第2個物件開始加入清單
            news.append(new[1:])
    return news

def main():
    filename = 'yuzzzzzzzzzzz.txt'
    lines = read_file(filename)
    lines = field(lines)
    print(del_line(lines))


main()