import re
import time
import json
import requests


class Migu:
    def __init__(self):
        self.url = "http://music.migu.cn/v3/search?keyword={}"
        self.parse_url = "http://music.migu.cn/v3/api/music/audioPlayer/getPlayInfo?copyrightId={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
        self.dumps = {'copyrightId': '64046301000'}
        self.count = 0

    def req(self, url):
        # 获取歌曲id 和 歌曲名称
        re_response = requests.get(url, headers=self.headers)
        re_html = re_response.content.decode('utf8')
        re_songid = re.compile('<a href="/v3/music/song/(\d+)" title="(.*?)" target="_blank">.*?</a>', re.S).findall(re_html)
        print('共获取以下歌曲信息:', re_songid)
        return re_songid

    def parse(self, songid):
        url = self.parse_url.format(songid)
        self.dumps['copyrightId'] = songid
        response = requests.get(url, data=json.dumps(self.dumps), headers=self.headers)
        text = json.loads(response.content.decode())
        txt1 = text['walkmanInfo']
        txt = txt1['playUrl']
        # print(txt)
        return txt

    def download(self, txt, song_name):
        self.count = self.count + 1
        with open('%s_%s.mp3' % (song_name, txt), 'wb') as f:
            # 下载mp3文件
            response = requests.get(url=txt)
            f.write(response.content)
            print("下载:%s_%s" % (song_name, txt))
            time.sleep(1)

    def run(self):
        text = input('请输入要下载的歌曲：')
        print('你输入的歌曲名是："%s"' % text)
        print('已发送请求！')
        # print(text)
        url = self.url.format(text)
        re_songid = self.req(url)
        for i in re_songid:
            print('暂停3秒~~~')
            time.sleep(3)
            txt = self.parse(i[0])
            print('已获得下载连接!')
            print('暂停3秒~~~')
            time.sleep(3)
            self.download(txt, i[1])


if __name__ == '__main__':
    t1 = Migu()
    t1.run()
