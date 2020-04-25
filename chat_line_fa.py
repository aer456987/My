# 讀取檔案(刪除\n空白)
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines


# 篩選欄位
def field(lines):
    fields = []
    for fie in lines:
        if not fie:                # 如果是空行就忽略
            continue
        elif '2019/' in fie[0]:    # 如果裡面含有'2019/'就忽略
            continue
        elif fie[2] == ':':        # 如果第三個字串是':'就從第六個字串開始加入清單
            fields.append(fie[6:])
        else:
            fields.append(fie)
    return fields


# 格式轉換
def convert(lines):
    news = []
    for new in lines:
        if new[:8] == 'Yuzzzzzz':
            news.append(new[:3] + ': ' + new[9:])
        elif new[:4] in '羽鳥吟仁':
            news.append(new[:4] + ': ' + new[5:])
        else:
            news.append(new)
    return news


def save(file_name, lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    filename = '原始檔yuzzzz.txt'
    lines = read_file(filename)
    lines = field(lines)
    lines = convert(lines)
    save('轉換後與yuz.txt', lines)
    # save('轉換後與yuz.csv',lines)

main():