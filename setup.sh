#!/bin/bash
# Version 0.1
#===============================================================================
# 本脚本用于自动安装 FourEye（重明）依赖程序，包括Linux系统依赖和Python依赖
# 使用方式(建议使用root用户运行)：
# +------------------------------+
# |  chmod 755 setup.sh          |
# |  ./setup.sh                  |
# +------------------------------+
# 若有使用问题联系: https://github.com/lengjibo/FourEye/issues
# 最后祝好运

echo "
  ______                   ___
(_) |                    / (_)
   _|_  __          ,_   \__         _
  / | |/  \_|   |  /  |  /    |   | |/
 (_/   \__/  \_/|_/   |_/\___/ \_/|/|__/
                                 /|
                                 \|  "



if ping -c 1 -w 2 mirrors.ustc.edu.cn &>/dev/null; then
	echo "[+] 测试网络可用"
else
	echo "[-] 测试网络不可用，请检查网络设置"
	exit
fi

# 判断Python依赖
python_requirements=`pip3 freeze`
str="termcolor"
if [[ $python_requirements =~ $str ]];then
    echo "[+] Python依赖存在"
    echo "[*] 开始检查Linux系统依赖程序"
else
    echo "[-] 未找到Python依赖"
    echo "[*] 开始安装Python依赖"
    which "pip3" &>/dev/null
    if [ $? -eq 0 ]
    then
    pip3 install -r requirements.txt
    else
    echo "[-] 未找到可用的pip3, 请使用一下命令手动安装: "
    echo "--> apt-get install python3-termcolor"
    echo "or"
    echo "--> pip3 install termcolor"
    fi
fi


# 判断mingw-w64依赖
m="mingw-w64"
SYSTEM=`cat /etc/issue.net | awk '{print $1}'`

case $SYSTEM in
    Debian) echo "[+] 检测系统是$SYSTEM, 使用apt-get安装"
        min=`dpkg --list | grep mingw-w64`
        if [[ $min =~ $m ]];then
            echo "[+] 检测到已经安装了mingw-w64"
            python3 BypassFramework.py
            exit
        else
            sudo apt-get install mingw-w64
            echo "[+] 系统依赖安装完成"
            python3 BypassFramework.py
            exit
        fi
        ;;
    Kali) echo "[+] 检测系统是$SYSTEM, 使用apt-get安装"
        min=`dpkg --list | grep mingw-w64`
        if [[ $min =~ $m ]];then
            echo "[+] 检测到已经安装了mingw-w64"
            python3 BypassFramework.py
            exit
        else
            sudo apt-get install mingw-w64
            echo "[+] 系统依赖安装完成"
            python3 BypassFramework.py
            exit
        fi
        ;;
    *)
        ;;
esac 

SYS=`cat /etc/redhat-release | awk '{print $1}'`
    
case $SYS in
    CentOS) echo "[+] 检测系统是$SYS, 使用yum安装"
        if [[ $min =~ $m ]];then
            echo "[+] 检测到已经安装了mingw-w64"
            python3 BypassFramework.py
        else
            sudo yum install mingw64-gcc
            python3 BypassFramework.py
            exit
        fi
        ;;
    *) echo "[-] 脚本不适用于该系统"
        exit
        ;;
esac
