<h1 align="center"> FourEye（重明） - AV Evasion Tool For Red Team Ops</h1>

用于快速生成免杀的 EXE 可执行文件，目前拥有三种免杀方法。

```
 ______                   ___           
(_) |                    / (_)          
   _|_  __          ,_   \__         _  
  / | |/  \_|   |  /  |  /    |   | |/  
 (_/   \__/  \_/|_/   |_/\___/ \_/|/|__/
                                 /|     
                                 \|   


                    v1.6 stable !
                    author lengyi@HongHuSec Lab !

 FourEye BypassFrameWork | BypassAV your shellcode && exe 
```

## 声明
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) 仅限用于技术研究和获得正式授权的测试活动。

## 安装方法

推荐使用kali linux系统安装,后期会考虑增加docker部署，或增加setup脚本。

> git clone https://github.com/lengjibo/FourEye.git

> cd FourEye

> pip install -r requirements.txt

> python3 BypassFramework.py

**因为是linux下编译，所以编译文件会有体积大的问题，该工具为三天内的产物，可能有不少bug，欢迎在issus处与我反馈**


## 使用方法

### shellcode

> python3 BypassFramework.py

![image](https://raw.githubusercontent.com/lengjibo/FourEye/main/image/1.png)

> 选择shellcode

![image](https://raw.githubusercontent.com/lengjibo/FourEye/main/image/2.png)

> 选择免杀方式，1：Fiber、2：APC、3：图片分离，选择加密方式，xor或者rot13，然后输入shellcode，选择位数，x64或者x86

![image](https://raw.githubusercontent.com/lengjibo/FourEye/main/image/3.png)

> 执行execute

![image](https://raw.githubusercontent.com/lengjibo/FourEye/main/image/4.png)


### exe

> 选择exe，然后输入exe即可


![image](https://raw.githubusercontent.com/lengjibo/FourEye/main/image/5.png)


### demo。已上传至B站。

https://www.bilibili.com/video/BV1zy4y1S7ZM/

https://www.bilibili.com/video/BV1Sh411Z7qc

https://www.bilibili.com/video/BV1b54y1x7RT

## 引用

大多数方法均为网上已经公开的方法，本人只是对其整合、优化，多来自于ired，感谢其分享精神。

## update

2020.12.14：增加其对exe的免杀，方法参考@bats3c，若使用报错请安装x86_64-w64-mingw32-gcc
2021.01.03: 增加x86、x64的支持


## TODO

- 增加更多的免杀、shellcode加密方法


