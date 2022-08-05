#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main(void){
    // 安装依赖库
    system("pip install PyQt5 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("pip install QtWidgets -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("pip install QtGui -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("pip install QtWebEngineWidgets -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com");
    system("python3 -m pip install QtWebEngineWidgets");
    system("pip --trusted-host pypi.python.org install QtWebEngineWidgets");
    // 提示用户
    cout << "安装应该完成了";
    return 0;
}