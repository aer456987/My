import urllib.request as req

# 抓取檔案
def getdata(url):
    request = req.Request(url, headers = {
        'cookie':'over18=1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    })

    # 抓取資料
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')
        # print(data)
    return data


# 資料解析,取得標題和上一頁的網頁連結
def analyzedata(data):
    import bs4
    root = bs4.BeautifulSoup(data, 'html.parser')    # 用BeautifulSoup4開啟上面抓到的html網頁

    # 變數.find_all('標籤', 篩選條件)  → (全部)從網頁中尋找標籤
    titles = root.find_all('div', class_='title')    # 搜尋'div'標籤中含有class_='title'的資料
    for title in titles:
        if title.a != None:          # 如果title中有a標籤就印出(排除已被刪除的文章)
            print(title.a.string)

    # 搜尋'a'標籤中string內文是'‹ 上頁'的資料
    nextLink = root.find('a', string='‹ 上頁')
    return nextLink['href']          # 回傳nextLink(a標籤)標籤中的'href'屬性，產生的網址會被存入


# 執行
def main():
    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
    count = 0
    while count < 3:
        count += 1
        print('=================================\n' +
            '【第', count, '頁】\n' +
            '================================='
        )
        data = getdata(url)
        data = 'https://www.ptt.cc' + analyzedata(data)

main()