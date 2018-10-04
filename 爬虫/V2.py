'''
利用request下载页面
自动检测页面编码
'''
import urllib
import chardet
if __name__ == '__main__':
    url = "https://app.peopleapp.com/Api/600/DetailApi/shareArticle?type=0&article_id=2554003"
    rsp = urllib.request.urlopen(url)
    html = rsp.read()

    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    #使用get取值保证不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)