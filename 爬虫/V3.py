import urllib

if __name__ == '__main__':
    url = "https://app.peopleapp.com/Api/600/DetailApi/shareArticle?type=0&article_id=2554003"
    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

    html = rsp.read()

    html = html.decode()
    #print(html)
