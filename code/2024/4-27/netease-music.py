import requests
from bs4 import BeautifulSoup 


print('注:如果您的网址格式为:https://music.163.com/#/discover/toplist\n那么删去其中的"/#"部分,使其变为:https://music.163.com/discover/toplist')
print('请合理使用本程序,作者不对任何使用者负责\n下载的音乐无法打开则表示目前没有办法直接下载该音乐!')
print('-----------------------------')
url = input('请输入网址:')
eval("url")
print('-----------------------------')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
res = requests.get(url=url,headers=headers)
#获取网页源代码
soup = BeautifulSoup(res.text,'html.parser')
#匹配对应的数据,音乐名称
result = soup.find('ul',class_='f-hide')
infor = result.find_all('a')

idlist = []  #存放ID
namelist = [] #存放名字
number = 0 #歌曲的序号

for i in infor:
    number = number+1
    name = i.text #音乐名字
    result = i.get('href')
    id = result[9:]
    idlist.append(id)
    Newurl = 'https://music.163.com/'+result
    namelist.append(name)
    print(str(number)+' '+name+' '+Newurl)



#保存数据
def download():
    while True:
        a = input("请输入你要下载的歌曲的序号:")
        b = int(a)-1
        aa = idlist[b]
        musicName = namelist[b]

        url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(aa)
        music = requests.get(url=url,headers=headers).content

        with open('{}.mp3'.format(musicName),'wb')as f:
            f.write(music)
            print(musicName+'下载完毕!')

download()
