import requests
import jsonpath
import re

def song_download(url, title, author):
    print("True")
    path = '{}.mp3'.format(title)
    print('歌曲:{0}-{1},正在下载...'.format(title, author))
    # 下载
    content = requests.get(url).content
    cleaned_title = clean_filename(title)
    cleaned_author = clean_filename(author)
    with open(file=cleaned_title + cleaned_author + '.mp3', mode='wb') as f:
        f.write(content)
    print('下载完毕,{0}-{1},请查看!'.format(title, author))


def clean_filename(filename):
    cleaned_filename = re.sub(r'[^\w-]', '', filename)
    return cleaned_filename


import requests

def get_music_name():
    while True:
        print('---------------------------------------------------------')
        print("请合理使用本程序,作者不对任何使用者负责\n下载的音乐无法打开则表示目前没有办法直接下载该音乐!")
        name = input("请输入歌曲名称:")
        print("1.网易云-netease\n2.QQ-qq\n3.酷狗-kugou\n4.酷我-kuwo\n5.百度-baidu\n6.喜马拉雅-ximalaya")
        print("您应当输入netease、qq、kugou、kuwo、baidu、ximalaya中的一个")
        platform = input("请输入音乐平台类型:")
        print("---------------------------------------------------------")
        url = 'https://music.liuzhijin.cn/'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        param = {
            "input": name,
            "filter": "name",
            "type": platform,
            "page": 1,
        }
        res = requests.post(url=url, data=param, headers=headers)
        json_text = res.json()


        title = jsonpath.jsonpath(json_text, '$..title')
        author = jsonpath.jsonpath(json_text, '$..author')
        url = jsonpath.jsonpath(json_text, '$..url')
        if title:
            songs = list(zip(title, author, url))
            for i, s in enumerate(songs):
                print(f"{i + 1}. {s[0]} - {s[1]}")
            print("---------------------------------------------------------")
            index = int(input("请输入您想下载的歌曲序号(输入0退出):"))
            if index == 0:
                input("输入任意键退出...")
                exit()
            song_download(url[index - 1], title[index - 1], author[index - 1])
        else:
            print("对不起,暂无搜索结果!")

if __name__ == "__main__":
    get_music_name()
