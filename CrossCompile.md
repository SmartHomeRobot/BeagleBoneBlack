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

or edit ~/.zhsrc
    /home/quanpower/dev/cross_compile/toolchain/gcc-linaro-arm-linux-gnueabihf-4.9-2014.09_linux/bin/arm-linux-gnueabihf-

*Test: If this test fails, verify that you have the 32bit libraries installed on your development system.*

    ${CC}gcc --version
    arm-linux-gnueabihf-gcc (crosstool-NG linaro-1.13.1-4.9-2014.09 - Linaro GCC 4.9-2014.09) 4.9.2 20140904 (prerelease)
    Copyright (C) 2014 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# 3.GIT

The Beaglebone patches and build scripts are stored in a git repository. Install git:

    sudo apt-get install git

And configure with your identity.

    git config --global user.email "your.email@here.com"

# 4.lzop Compression

The Linux Kernel is compressed using lzo. Install the lzop parallel file compressor:

    sudo apt-get install lzop

# 5.Bootloader: U-Boot

Das U-Boot -- the Universal Boot Loader http://www.denx.de/wiki/U-Boot

## 5.1 Download:
    ~/
    git clone git://git.denx.de/u-boot.git
    cd u-boot/
    git checkout v2014.10 -b tmp

## 5.2 Patches:
    ~/u-boot
    wget -c https://raw.githubusercontent.com/eewiki/u-boot-patches/master/v2014.10/0001-am335x_evm-uEnv.txt-bootz-n-fixes.patch
 
    patch -p1 < 0001-am335x_evm-uEnv.txt-bootz-n-fixes.patch

## 5.3 Configure and Build:
    ~/u-boot
    
    make ARCH=arm CROSS_COMPILE=${CC} distclean
    make ARCH=arm CROSS_COMPILE=${CC} am335x_evm_defconfig
    make ARCH=arm CROSS_COMPILE=${CC}

# 6. Upgrade distro "device-tree-compiler" package
    ~/
    wget -c https://raw.github.com/RobertCNelson/tools/master/pkgs/dtc.sh
    chmod +x dtc.sh
    ./dtc.sh

# 7. Kernel

First, the source code was downloaded, checked-out and patched:

    git clone git://github.com/beagleboard/kernel.git

This downloads the kernel source

    cd kernel
    git checkout 3.8

The head of 3.8 release was checked out. For further study how to check out a release tag that matches pre-built published images

    ./patch.sh
    This step may take 10 minutes or longer

Some further preparations before the kernel is built:

    cp configs/beaglebone kernel/arch/arm/configs/beaglebone_defconfig

We wish to build beaglebone series kernels

    wget http://arago-project.org/git/projects/?p=am33x-cm3.git\;a=blob_plain\;f=bin/am335x-pm-firmware.bin\;hb=HEAD -O kernel/firmware/am335x-pm-firmware.bin
                        
Pre-compiled power management firmware

    cd kernel

These steps will compile the kernel and some kernel modules:

    make ARCH=arm CROSS_COMPILE=${CC} beaglebone_defconfig
   
    make ARCH=arm CROSS_COMPILE=${CC} uImage dtbs
    This step builds the kernel and may take 15-20 minutes or longer

    make ARCH=arm CROSS_COMPILE=${CC} uImage-dtb.am335x-boneblack
    This step builds the kernel for the BBB

    make ARCH=arm CROSS_COMPILE=${CC} modules
    This builds the kernel modules and may take 20 minutes or longer

This whole process took around an hour on a VM running on a i5 2.5GHz laptop. On an i7 1.6GHz, it took twice as long, so if you have a choice then it makes sense to spend some time examining which server you really wish to develop on.

In the /home/username/develop/kbuild/kernel/kernel/arch/arm/boot folder, there will be a uImage-dtb.am335x-boneblack file. 
