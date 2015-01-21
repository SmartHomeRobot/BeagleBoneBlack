c-kermit是Linux下简单易用的串口工具,配置简单,现说说我的安装使用方法,我用的USB转串口+VM,环境不同可能设备名不一样

1.安装: sudo apt-get install ckermit

2.设置配置文件 c-kermit启动时会从当前用户下查找.kermrc配置文件,所以我们先写好一个配置文件,全名为 ~/.kermrc,内容为:

set line /dev/ttyUSB0  #如果使用电脑本身的串口,这里可能是ttyS0之类的
set speed 115200
set carrier-watch off
set handshake none
set flow-control none
robust
set file type bin
set file name lit
set rec pack 1000
set send pack 1000
set window 5
c

3.使用 kermit –c 来连接串口,如果出现乱码,请关闭终端多试几次,总会成功的-:)
