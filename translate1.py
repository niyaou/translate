import importlib, sys, urllib

importlib.reload(sys)
import urllib.request
import json
import hashlib
import urllib
import random


def translate(inputFile, outputFile):
    fin = open(inputFile, 'r', encoding='utf-8')
    fout = open(outputFile, 'w', encoding='utf-8')
    appid = '20170307000041649'
    secretKey = 'JcXq9a9QwvxN2l6AhIqH'

    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = 'apple'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    for eachLine in fin:
        line = eachLine.strip()
        if line:
            if line[0].isdigit():
                fout.write(line + "\n")
            else:

                sign = appid + line + str(salt) + secretKey
                sign = hashlib.md5(sign.encode()).hexdigest()

                myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
                    line) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
                resultPage = urllib.request.urlopen(myurl)

                print (myurl)

                resultJason = resultPage.read().decode('utf-8')
                resultJasons = resultPage.read()
                print (resultJason)

                try:
                    js = json.loads(resultJason)

                    print ('dst')
                    dst = str(js["trans_result"][0]["dst"])
                    outStr = dst
                    print (dst)
                    if dst[0]:
                        outDst = dst.strip() + "\n"
                    fout.write(outDst)
                except Exception as e:
                    fout.write("\n")
                    continue
        else:

            fout.write("\n")



            # fout.write(dst.strip().encode('utf-8'))              #将结果输出

    fin.close()
    fout.close()


if __name__ == '__main__':
    translate(sys.argv[1], sys.argv[2])  # 通过获得命令行参数获得输入输出文件名来执行，方便
