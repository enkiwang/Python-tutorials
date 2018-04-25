"""
Created on Wed Apr 25 09:02:00 2018
*****parser + open a file (to write) *****
1：import argparse

2：parser = argparse.ArgumentParser() # create a parser object

3：parser.add_argument()

4：parser.parse_args()  # anlyze the parser
------------------------------------------------------------------------------------
python this_file_name.py -u http://www.sohu.com -d 'a=1,b=2,c=3' -o /tmp/index.html
url: http://www.sohu.com
query: ?a=1&b=2&c=3
saving_dir: /tmp/index.html
------------------------------------------------------------------------------------
@author: @https://www.cnblogs.com/linxiyue/p/3908623.html

"""

import argparse
from pyquery import PyQuery as pq


def getArgs():
    parse=argparse.ArgumentParser()
    parse.add_argument('-u',type=str)
    parse.add_argument('-d',type=str)
    parse.add_argument('-o',type=str)
    args=parse.parse_args()
    return vars(args)


def urlAddQuery(url,query):
    query=query.replace(',','&')  # a=1,b=2,c=3 --> a=1&b=2&c=3
    if '?' in url:
        return url.replace('?','?'+query+'&')
    else:
        return url+'?'+query
    
    
def getHref():
    args=getArgs()  # {'u': 'http://www.sohu.com', 'd': 'a=1,b=2,c=3', 'o': '/tmp/index.html'}
    url=args['u']  # http://www.sohu.com
    query=args['d'].strip("\'")  # a=1,b=2,c=3
    fileName=args['o']  # /tmp/index.html
    doc=pq(url=url)
    count=0
    
    with open(fileName,'w') as f:
        for a in doc('a'):
            a=pq(a)
            print(a)
            href=a.attr('href')
            if href:
                newurl=urlAddQuery(href,query)
                count = count+1
                if count < 5:   #print first 4 (queried) urls
                    print(newurl)
                    print("")
                if count == 4:
                    return 
                f.write(newurl+'\n')


if __name__=='__main__':
    getHref()
    
    
"""
<a href="http://news.sohu.com/s2018/lianghui/index.shtml" target="_blank"/>
http://news.sohu.com/s2018/lianghui/index.shtml?a=1&b=2&c=3

<a href="javascript:void(0)"/>
javascript:void(0)?a=1&b=2&c=3

<a href="/" target="_blank">&#25628;&#29392;&#39318;&#39029;</a>
/?a=1&b=2&c=3

<a href="http://mp.sohu.com/" target="_blank"/>
http://mp.sohu.com/?a=1&b=2&c=3

"""
