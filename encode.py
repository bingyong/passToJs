#coding:utf-8
import  execjs
import click

def info():
    print("\033[1;33;40m [+]============================================================")
    print("\033[1;33;40m [+] Python调用JS加密password文件内容                          =")
    print("\033[1;33;40m [+] Explain: YaunSky                                          =")
    print("\033[1;33;40m [+] https://github.com/yaunsky                                =")
    print("\033[1;33;40m [+]============================================================")
    print("                                                                             ")

#对密码文件进行加密  密文在当前目录下的pass_encode.txt中

def Encode(jsfile, username, passfile):
    print("[+] 正在进行加密，请稍后......")
    with open (jsfile,'r') as strjs:
        src = strjs.read()
        phantom = execjs.get('PhantomJS')	#调用JS依赖环境
        getpass = phantom.compile(src)	#编译执行js脚本
        with open(passfile, 'r') as strpass:
            for passwd in strpass.readlines():
                passwd = passwd.strip()
                mypass = getpass.call('encrypt', username, passwd)	#传递参数
                with open("pass_encode.txt", 'a+') as p:
                    p.write(mypass+"\n")
            print("\033[1;33;40m [+] 加密完成")

#对单一密码进行加密
def passstring(jsfile, username, password):
    print("[+] 正在进行加密，请稍后......")
    with open (jsfile,'r') as strjs:
        src = strjs.read()
        phantom = execjs.get('PhantomJS')	#调用JS依赖环境
        getpass = phantom.compile(src)	#编译执行js脚本
        mypass = getpass.call('encrypt', username, password)	#传递参数
        print("\033[1;33;40m[+] 加密完成:{}".format(mypass))

@click.command()
@click.option("-J", "--jsfile", help='JS 加密文件')
@click.option("-u", "--username", help="登陆用户名")
@click.option("-P", "--passfile", help="明文密码文件")
@click.option("-p", "--password", help="明文密码字符串")
def main(jsfile, username, passfile, password):
    info()
    if jsfile != None and passfile != None and username != None:
        Encode(jsfile, username, passfile)
    elif jsfile != None and password != None and username != None:
        passstring(jsfile, username, password)
    else:
        print("python3 encode.py --help")

if __name__ == "__main__":
    main()
