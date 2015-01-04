    BeagleBone Black 默认是Angstrom系统，专门为嵌入式搞的linux系统，BBB官方支持这个系统。虽然官方不支持Ubuntu，但是还是有部分人在用，比如小弟我··\(^o^)/~简单讲下如何烧Ubuntu系统

# 1.硬件准备

microSD卡一个（最好大点，4G+，但是我手里只有一个破手机上退下来的2G的将就用吧），

microSD读卡器，

可选：键盘，鼠标，显示器

# 2.软件准备

我笔记本是win7，虽然虚拟机有Ubuntu系统，但是怕虚拟机读写USB口烧录的时候有问题还是用的win7来烧的。需要准备的有

ubuntu-14.04 eMMC Flasher,我这里下载的目前最新的

（http://elinux.org/BeagleBoardUbuntu#eMMC:_BeagleBone_Black），

Win32 Disk Imager,

7zip,

# 3.主要步骤

            There is an image for flashing to the eMMC by Robert C Nelson found on this page (look for the .img.xz file not .tar.xz)
        Alternatively, the direct download link for this image is here: 
    
    `wget https://rcn-ee.net/deb/flasher/trusty/BBB-eMMC-flasher-ubuntu-14.04.1-console-armhf-2014-10-29-2gb.img.xz` 
    
        After you have downloaded the .img.xz file you want, use a program such as 7zip to extract the image file
            Once 7zip is installed, right click on .img.xz file you just downloaded and click 7zip > Extract Here, to extract the .img file
        Insert the micro SD card into your computer
            Using a microSD-to-SD or microSD-to-USB adapter is fine 
        Use Win32 Disk Imager to write the image onto your micro SD
            Instructions on how to use Win32 Disk Imager can be found here 
        After Win32 Disk Imager has finished remove the micro SD card from your computer

# 4.Flashing Ubuntu to the eMMC

        After you have put the BeageBone Black Ubuntu Flasher image on a micro SD card, insert it into the powered-off BBB.
            Also make sure you have a keyboard, mouse, display, and Ethernet connected
        While holding down the 'boot' button, apply power to the board. Continue to hold the 'boot' button until the USER LEDs begin to flash
            You should use a 5V external power source, USB power may not work
        After about a minute your screen should show the login prompt.
        Leave the board be for about 10 minutes; the image is being flashed to the eMMC
        After about 10 minutes have passed the 4 LEDs should be solid and not flickering. Remove the power, remove the mirco SD, and then re-apply power to the board
        It will take a minute or two for the board to boot to the log-in screenUser is: ubuntu
        Password is: temppwd
            Note: echo is turned off for typing in password 
        You should now be in the command terminal for Ubuntu and your BeagleBone Black will boot here from now on.

# 5.Ubuntu 网络配置
## 5.1 显示器登录

如果有显示器跟键盘应该能看到命令行进行操作，但是像我这样没有多余的显示器，并且BBB的的HDMI一般还需要转接下，只好远程操控了。

## 5.2 USB-TTL 串口登录

BBB可以用串口线来连接，搞个USB-TTL的的串口线来连接，记得波特率是115200。GND接BBB J1 的6个pin的第一个pin,网口方向侧的第一个，同时标有一个白圆点，另4 pin接TXD，5 pin接RXD。这个顺序我找了好几个文档都发现有表述。

## 5.3 USB-OTG SSH登录

最方便的还是用SSH来登陆。可以选择用SSH指令来登陆，我是用的Putty来登陆的，刚烧完的系统，用自带的USB线插上供电后应该会有提示发现U盘，打开把里面的驱动装好，这样USB就算扩展为网线来用了。

可以把宿机的网络连接设置共享来让这个BBB共享上网，比如我笔记本用wifi上网，右键无线网络连接-熟悉-共享，选择一个网络连接，一般虚拟出来的应该是本地连接2吧，根据自己实际选择。这样宿机共享的本地连接作为网关应该是192.168.7.1，然后给BBB分配了个静态ip：192.168.7.2，ping下看能不能通。

若要用共享网卡上外网，需要设置默认网关
use root:

再配置BB-Black的路由和DNS等，可以在PuTTY中，登陆ssh终端，输入指令：

    route add default gw 192.168.7.1

然后查看路由设置

    root@beaglebone:~# route  
    Kernel IP routing table  
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface  
    default         192.168.7.1     0.0.0.0         UG    0      0        0 usb0  
    192.168.7.0     *               255.255.255.252 U     0      0        0 usb0  

还需要配置域名解析，编辑文件  /etc/resolv.conf

    root@beaglebone:~# nano /etc/resolv.conf  

增加几条nameserver的记录，并保存修改。比如 

    domain localdomain
    search localdomain
    nameserver 192.168.1.1
    nameserver 216.146.1.66
    nameserver 216.147.1.66

测试一下，结果如下：

## 5.4 默认账号密码

网络通了后，尝试登录BBB，用putty登录192.168.7.2，端口默认22，新烧的Ubuntu默认账号ubuntu,密码temppwd,登录进去后，先passwd ubuntu修改下密码。
如果要开通root用户，sudo passwd root 

## 5.5 wifi连接

用USB连接是可以，但是总不能每天抱着笔记本给BBB共享联网，很不方便有木有？所以我们继续努力，我从网上买了个wifi adapter。BBB一般的image都是3.8。13内核的，买的时候参考看支持的wifi控制芯片http://eewiki.net/display/linuxonarm/BeagleBone+Black。需要提的是大家常用的USB无线网卡中，TPLink，水星、能达等，水星的芯片比较特殊，3.8的内核不能够原生支持，若想使用，请自行编译其驱动，并加入内核。从初学者来说，不建议使用。

我的wifi adapter，

    sudo lsusb

查询下返回如下：

    Bus 001 Device 002: ID 0bda:8176 Realtek Semiconductor Corp. RTL8188CUS 802.11n WLAN Adapter

说明网卡支持，并已经挂载

安装无线上网工具：

    sudo aptitude install wireless-tools

查询无线网卡是否正常：

    sudo ifconfig -a

启用wlan0节点：

    sudo ifconfig wlan0 up

扫描无线网络：

    sudo iwlist wlan0 scan

修改interfaces

    sudo vim /etc/network/interfaces
    
    auto wlan0
    iface wlan0 inet static
        wpa-ssid "your ssid"
        wpa-psk  "your passwd"
    address 192.168.1.103
    netmask  255.255.255.0
    gateway  192.168.1.1

然后reboot了下，一切正常连接，终于摆脱长长的线了，现在只要有了电源，就完全可以自由操控了，为实现智能小车或者机器人奠定了通信基础。

## 5.6 更新源列表

    sudo nano /etc/apt/sources.list
    
    deb http://ports.ubuntu.com/ubuntu-ports/  trusty main restricted universe multiverse
    deb http://ports.ubuntu.com/ubuntu-ports/  trusty-security main restricted universe multiverse
    deb http://ports.ubuntu.com/ubuntu-ports/  trusty-updates main restricted universe multiverse
    deb http://ports.ubuntu.com/ubuntu-ports/  trusty-proposed main restricted universe multiverse
    deb http://ports.ubuntu.com/ubuntu-ports/  trusty-backports main restricted universe multiverse
    deb-src http://ports.ubuntu.com/ubuntu-ports/  trusty main restricted universe multiverse
    deb-src http://ports.ubuntu.com/ubuntu-ports/  trusty-security main restricted universe multiverse
    deb-src http://ports.ubuntu.com/ubuntu-ports/  trusty-updates main restricted universe multiverse
    deb-src http://ports.ubuntu.com/ubuntu-ports/  trusty-proposed main restricted universe multiverse
    deb-src http://ports.ubuntu.com/ubuntu-ports/  trusty-backports main restricted universe multiverse
    
    
    #Kernel source: https://github.com/RobertCNelson
    deb [arch=armhf] http://repos.rcn-ee.net/ubuntu/ trusty main

修改下本地语言环境，之前没更改，更新源的时候老报404错误

    sudo nano /etc/default/locale
    
    LANG="en_US.UTF-8"
    LANGUAGE="en_US:en"
    LANG="en_US.UTF-8"
    LANGUAGE="en_US:en"
    
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install vim

还是习惯使用vim装个vim先。

    df -hl 查看磁盘剩余空间
    df -h 查看每个根路径的分区大小
    du -sh [目录名] 返回该目录的大小
    du -sm [文件夹] 返回该文件夹总M数
    更多功能可以输入一下命令查看：
    df --help
    du --help

查看当前文件夹下所有文件大小（包括子文件夹）
    du -sh

    ubuntu@arm:/etc/apt$ du -h
    4.0K    ./preferences.d
    24K     ./apt.conf.d
    4.0K    ./sources.list.d
    4.0K    ./trusted.gpg.d
    92K     .

 
查看指定文件夹下所有文件大小（包括子文件夹）

    ubuntu@arm:/etc$ du -h apt
    4.0K    apt/preferences.d
    24K     apt/apt.conf.d
    4.0K    apt/sources.list.d
    4.0K    apt/trusted.gpg.d
    92K     apt

 
查看指定文件大小

    ubuntu@arm:/etc$ du -h ./apt/sources.list.d
    4.0K    ./apt/sources.list.d

查看指定文件夹大小
    
    ubuntu@arm:/etc$ du -hs apt
    92K     apt


用法：du [选项]... [文件]...
 或：du [选项]... --files0-from=F
计算每个文件的磁盘用量，目录则取总用量。
长选项必须使用的参数对于短选项时也是必需使用的。

## 5.7 python开发环境

set date and time:

    sudo ntpdate pool.ntp.org

Next install the dependencies:

    sudo apt-get update
    sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y

install BBIO:

    sudo pip install Adafruit_BBIO

# 6.VNC SERVER

##6.1 proxy

众所周知的原因，在国内查找或者下载国外内容非常吃力，只好加个proxy，

编辑.bashrc

    export http_proxy='http://proxy_ip:port'

另外附几个free proxy list：

    http://www.proxy.com.ru/
    
    http://www.ultraproxies.com/
    
    http://free-proxy-list.net/
    
    http://www.ippredator.com/

后经测试发现免费的变更太快，还是花钱买了个付费的，1年100块钱，每月30G也差不多够用了，然后在win7上新建了VPN，然后共享给本地连接，BBB用网线连接来用。实测BBB也可以用，能够正常更新源，及下载，终于解决这个恼人的事情。

然后重新

    sudo apt-get update
    
    sudo apt-get upgrade下，可以连上了

## 6.2 配置lxde和vnc server

### 6.2.1

安装x window:

    apt-get install xorg

安装lxde:

    apt-get install lxde-core

安装vnc server:

    apt-get install tightvncserver

第一次运行vnc server生成配置文件，需要输入密码:

tightvncserver :1

tightvncserver -kill :1

编辑~/.vnc/xstartup文件，在尾部添加:

lxterminal &

/usr/bin/lxsession -s LXDE &

启用vnc server:

    vncserver -geometry 800x600

开机自启动tightvncserver

首先把以下内容写入 /etc/init.d/tightvncserver

    #!/bin/sh
    ### BEGIN INIT INFO
    # Provides: tightvncserver
    # Required-Start: $syslog $remote_fs $network
    # Required-Stop: $syslog $remote_fs $network
    # Default-Start: 2 3 4 5
    # Default-Stop: 0 1 6
    # Short-Description: Starts VNC Server on system start.
    # Description: Starts tight VNC Server. Script written by James Swineson.
    ### END INIT INFO
    # /etc/init.d/tightvncserver
    VNCUSER='ubuntu'
    case "$1" in
            start)
                    su $VNCUSER -c '/usr/bin/tightvncserver :1'
                    echo "Starting TightVNC Server for $VNCUSER"
            ;;
            stop)
                    pkill Xtightvnc
                    echo "TightVNC Server stopped"
            ;;
            *)
                    echo "Usage: /etc/init.d/tightvncserver {start|stop}"
                    exit 1
            ;;
    esac
    exit 0

然后运行：

    sudo chmod 755 /etc/init.d/tightvncserver
    sudo update-rc.d tightvncserver defaults

重启看效果吧。

取消开机启动也很简单，就一行代码：

    sudo update-rc.d -f tightvncserver remove

### 6.2.2 下载vnc viewer

在这里下载: http://www.realvnc.com/download/viewer/

打开客户端，输入IP:590x，这里x是x桌面的编号:

连接后输入密码，就可以进入桌面了。

### 6.2.3  解决中文乱码

BBB默认locale是en，不习惯可以改中文。但是建议还是保留en

    cd /usr/share/locales
    ./install-language-pack zh_CN
    apt-get install language-pack-zh-hans
    apt-get install ttf-wqy-zenhei
	
vi /etc/default/locale     
    #修改为
    #LANG="zh_CN.UTF-8"
    #LANGUAGE="zh_CN:zh"

关闭putty，重新打开shell，执行locale，就可以看到语言设置是中文了

### 6.2.4 firefox

    sudo apt-get install firefox



