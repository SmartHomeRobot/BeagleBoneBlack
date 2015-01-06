# 0.Envirment
    
    $ cat /etc/lsb-release
   
    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=14.04
    DISTRIB_CODENAME=trusty
    DISTRIB_DESCRIPTION="Ubuntu 14.04.1 LTS"

    $ uname -a  
    
    Linux Ubuntu-dev 3.13.0-43-generic #72-Ubuntu SMP Mon Dec 8 19:35:06 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux

# 1.Basic Requirements:

    * ARM Cross Compiler
        * Linaro: http://www.linaro.org/downloads/
    * Bootloader
        * Das U-Boot – the Universal Boot Loader http://www.denx.de/wiki/U-Boot
        * Source – http://git.denx.de/?p=u-boot.git;a=summary
    * Linux Kernel
        * Linus's Mainline tree: https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
    * ARM based rootfs
        * Debian: https://www.debian.org/
        * Ubuntu: http://www.ubuntu.com

# 2.ARM Cross Compiler: GCC

    sudo apt-get install gcc-arm-linux-gnueabihf

or manual:

This is a pre-built (32bit) version of Linaro GCC that runs on generic linux, so 64bit users need to make sure they have installed the 32bit libraries for their distribution.
If Ubuntu 14.04 -> 14.10:

    sudo apt-get install libc6:i386 libstdc++6:i386 libncurses5:i386 zlib1g:i386 

    wget -c https://releases.linaro.org/14.09/components/toolchain/binaries/gcc-linaro-arm-linux-gnueabihf-4.9-2014.09_linux.tar.xz
    tar xf gcc-linaro-arm-linux-gnueabihf-4.9-2014.09_linux.tar.xz
    export CC=`pwd`/gcc-linaro-arm-linux-gnueabihf-4.9-2014.09_linux/bin/arm-linux-gnueabihf-

    *Test: If this test fails, verify that you have the 32bit libraries installed on your development system.*

    ${CC}gcc --version
    arm-linux-gnueabihf-gcc (crosstool-NG linaro-1.13.1-4.9-2014.09 - Linaro GCC 4.9-2014.09) 4.9.2 20140904 (prerelease)
    Copyright (C) 2014 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
