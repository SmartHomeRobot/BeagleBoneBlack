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


# 8. Transferring the image to the BBB via TFTP

## 8.1 setenv

Use C-Kermit type the following at the u-boot prompt:

    setenv autoload no
	
    dhcp
	# Obtain IP config via DHCP

An IP address should be acquired now – assume it is 192.168.1.103 for now.

    setenv serverip 192.168.1.107
	
Replace with the IP address of your Linux server

## 8.2 transferring

    tftp 0x80200000 uImage-BBB
	
This was the file that was called uImage-dtb.am335x-boneblack. Notice that the address needs to be 0x80200000 and not the address that the mkimage –l command reported

    setenv bootargs console=ttyO0,115200n8 quiet root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait

The file system (that will be on top of the Linux kernel) is the one on the eMMC card for now

    bootm 0x80200000
	
The parameter passed here is the addresses of where the kernel image was dumped


With the final command listed above, you should see the kernel begin execution.

Here is some example output: 
    U-Boot# tftp 0x80200000 uImage-BBB
    using musb-hdrc, OUT ep1out IN ep1in STATUS ep2in
    MAC 7c:66:9d:6e:f1:ed
    HOST MAC de:ad:be:af:00:00
    RNDIS ready
    high speed config #2: 2 mA, Ethernet Gadget, using RNDIS
    USB RNDIS network up!
    Using usb_ether device
    TFTP from server 192.168.1.107; our IP address is 192.168.1.103
    Filename 'uImage-BBB'.
    Load address: 0x80200000
    Loading: T T T T T T T T T T T T T T T T T T T T 
    Retry count exceeded; starting again
    link up on port 0, speed 100, full duplex
    Using cpsw device
    TFTP from server 192.168.1.107; our IP address is 192.168.1.103
    Filename 'uImage-BBB'.
    Load address: 0x80200000
    Loading: T #################################################################
    	 #################################################################
    	 #################################################################
    	 #################################################################
    	 ########################################
    	 327.1 KiB/s
    done
    Bytes transferred = 4403742 (43321e hex)
    U-Boot# setenv bootargs console=ttyO0,115200n8 quiet root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait
    U-Boot# bootm 0x80200000
    ## Booting kernel from Legacy Image at 80200000 ...
       Image Name:   Linux-3.8.13-00770-g1b68031
       Created:      2015-01-15  17:03:20 UTC
       Image Type:   ARM Linux Kernel Image (uncompressed)
       Data Size:    4403678 Bytes = 4.2 MiB
       Load Address: 80008000
       Entry Point:  80008000
       Verifying Checksum ... OK
       Loading Kernel Image ... OK
    
    Starting kernel ...
    
    Uncompressing Linux... done, booting the kernel.
    [    0.158719] omap2_mbox_probe: platform not supported
    [    0.165282] tps65217-bl tps65217-bl: no platform data provided
    [    0.230013] bone-capemgr bone_capemgr.9: slot #0: No cape found
    [    0.267118] bone-capemgr bone_capemgr.9: slot #1: No cape found
    [    0.304226] bone-capemgr bone_capemgr.9: slot #2: No cape found
    [    0.341336] bone-capemgr bone_capemgr.9: slot #3: No cape found
    [    0.356213] bone-capemgr bone_capemgr.9: slot #6: BB-BONELT-HDMIN conflict P8.45 (#5:BB-BONELT-HDMI)
    [    0.365808] bone-capemgr bone_capemgr.9: slot #6: Failed verification
    [    0.380892] omap_hsmmc mmc.5: of_parse_phandle_with_args of 'reset' failed
    [    0.388149] bone-capemgr bone_capemgr.9: loader: failed to load slot-6 BB-BONELT-HDMIN:00A0 (prio 2)
    [    0.452932] pinctrl-single 44e10800.pinmux: pin 44e10854 already requested by 44e10800.pinmux; cannot claim for gpio-leds.8
    [    0.464628] pinctrl-single 44e10800.pinmux: pin-21 (gpio-leds.8) status -22
    [    0.471903] pinctrl-single 44e10800.pinmux: could not request pin 21 on device pinctrl-single
    Mount failed for selinuxfs on /sys/fs/selinux:  No such file or directory
     * Starting Mount filesystems on boot                                    [ OK ]
     * Starting Populate and link to /run filesystem                         [ OK ]
     * Stopping Populate and link to /run filesystem                         [ OK ]
     * Stopping Track if upstart is running in a container                   [ OK ]
     * Starting Initialize or finalize resolvconf                            [ OK ]
     * Starting set console keymap                                           [ OK ]
     * Starting Signal sysvinit that virtual filesystems are mounted         [ OK ]
     * Starting Signal sysvinit that virtual filesystems are mounted         [ OK ]
     * Starting Bridge udev events into upstart                              [ OK ]
     * Stopping set console keymap                                           [ OK ]
     * Starting Signal sysvinit that remote filesystems are mounted          [ OK ]
     * Starting device node and kernel event manager                         [ OK ]
     * Starting load modules from /etc/modules                               [ OK ]
     * Starting cold plug devices                                            [ OK ]
     * Starting log initial device creation                                  [ OK ]
     * Stopping load modules from /etc/modules                               [ OK ]
     * Starting set console font                                             [ OK ]
     * Stopping set console font                                             [ OK ]
     * Starting userspace bootsplash                                         [ OK ]
     * Stopping userspace bootsplash                                         [ OK ]
     * Starting configure network device security                            [ OK ]
     * Starting Send an event to indicate plymouth is up                     [ OK ]
     * Stopping Send an event to indicate plymouth is up                     [ OK ]
    [    5.543007] libphy: PHY 4a101000.mdio:01 not found
    [    5.548048] net eth0: phy 4a101000.mdio:01 not found on slave 1
     * Starting Signal sysvinit that the rootfs is mounted                   [ OK ]
     * Starting configure network device security                            [ OK ]
     * Starting Clean /tmp directory                                         [ OK ]
     * Stopping Clean /tmp directory                                         [ OK ]
     * Starting Mount network filesystems                                    [ OK ]
     * Starting Signal sysvinit that local filesystems are mounted           [ OK ]
     * Stopping cold plug devices                                            [ OK ]
     * Stopping Mount filesystems on boot                                    [ OK ]
    Waiting for network configuration...
    Waiting up to 60 more seconds for network configuration...
    Booting system without full network configuration...
     * Starting Failsafe Boot Delay                                          [ OK ]
     * Starting flush early job output to logs                               [ OK ]
     * Stopping log initial device creation                                  [ OK ]
     * Starting configure network device security                            [ OK ]
     * Starting D-Bus system message bus                                     [ OK ]
     * Stopping Mount network filesystems                                    [ OK ]
     * Stopping flush early job output to logs                               [ OK ]
     * Starting configure network device                                     [ OK ]
     * Starting system logging daemon                                        [ OK ]
     * Stopping Failsafe Boot Delay                                          [ OK ]
     * Starting configure virtual network devices                            [ OK ]
     * Starting System V initialisation compatibility                        [ OK ]
     * Starting mDNS/DNS-SD daemon                                           [ OK ]
     * Starting Reload cups, upon starting avahi-daemon to make sure remote queues are populated                                                             [ OK ]
     * Stopping System V initialisation compatibility                        [ OK ]
     * Starting Reload cups, upon starting avahi-daemon to make sure remote queues are populated                                                             [fail]
     * Starting System V runlevel compatibility                              [ OK ]
     * Starting save kernel messages                                         [ OK ]
     * Starting OpenSSH server                                               [ OK ]
     * Starting ACPI daemon                                                  [ OK ]
     * Starting regular background program processing daemon                 [ OK ]
     * Stopping save kernel messages                                         [ OK ]
     * Loading cpufreq kernel modules...                                     [ OK ] 
     * Starting Bridge file events into upstart                              [ OK ]
     * CPU0...                                                                       * Starting Bridge socket events into upstart                            [ OK ]
     * CPUFreq Utilities: Setting ondemand CPUFreq governor...               [ OK ] 
    Starting very small Busybox based DHCP server: Starting /usr/sbin/udhcpd...
    udhcpd.
    AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
     * 
     * Stopping System V runlevel compatibility                              [ OK ]
    
    Ubuntu 14.04.1 LTS arm ttyO0
    
    default username:password is [ubuntu:temppwd]
    
    The IP Address for eth0 is: 192.168.1.103
    arm login: 
    
# 9. Appendix: Installing and configuring the TFTP server

[TFTP server](tftp.md)

# 10. Appendix: Installing and using C-Kermit

[C-Kermit](c-kermit.md)