#include <stdlib.h>
#include <stdio.h>
int main(void){
    system("pip install PyQt5 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("pip install QtWidgets -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("pip install QtGui -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("pip install QtWebEngineWidgets -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("python3 -m pip install QtWebEngineWidgets");
    system("pip --trusted-host pypi.python.org install QtWebEngineWidgets");
}