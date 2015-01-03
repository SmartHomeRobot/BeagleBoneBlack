配置BB-Black的路由和DNS等，可以在PuTTY中，登陆ssh终端，输入指令：
    
    sudo route add default gw 192.168.7.1

然后查看路由设置
        
    root@beaglebone:~# route 

Kernel IP routing table 
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface 
default         192.168.7.1     0.0.0.0         UG    0      0        0 usb0 
192.168.7.0     *               255.255.255.252 U     0      0        0 usb0

# 2.还需要配置域名解析，编辑文件  /etc/resolv.conf
root@beaglebone:~# nano /etc/resolv.conf
增加几条nameserver的记录，并保存修改。比如 

domain localdomain
search localdomain
nameserver 192.168.1.1
nameserver 216.146.1.66
nameserver 216.147.1.66
