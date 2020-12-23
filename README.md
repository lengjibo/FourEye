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


                    v1.5 stable !
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

时间原因，录了一个小demo。已上传至B站。

https://www.bilibili.com/video/BV1zy4y1S7ZM/

## 引用

大多数方法均为网上已经公开的方法，本人只是对其整合、优化，多来自于ired，感谢其分享精神。

## update

12.14：增加其对exe的免杀，方法参考@bats3c，若使用报错请安装x86_64-w64-mingw32-gcc


## TODO

- 增加更多的免杀、shellcode加密方法


