# proxy is used !
import urllib.request

proxy = {"http": "http://124.88.67.20:843"}  # choose from http://proxylist.hidemyass.com/2
opener = urllib.request.FancyURLopener(proxy)
with opener.open("http://httpbin.org/ip") as f:
    print(f.read().decode('utf-8'))
