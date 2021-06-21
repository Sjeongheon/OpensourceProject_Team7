import os
import sys
import urllib.request

def translate(text) :
        client_id = "ZyBOdiaTYq0bA6XwoNEI"
        client_secret = "2u08u52QQq"
        encText = urllib.parse.quote(text)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
                response_body = response.read()
                return response_body.decode('utf-8')
        else:
                return "Error Code:" + rescode
