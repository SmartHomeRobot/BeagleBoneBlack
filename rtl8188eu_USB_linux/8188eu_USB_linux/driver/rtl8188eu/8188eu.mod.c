#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0xa60b9ee, "module_layout" },
	{ 0xfb1d585d, "register_netdevice" },
	{ 0x12da5bb2, "__kmalloc" },
	{ 0xf9a482f9, "msleep" },
	{ 0xc411a2ab, "complete_and_exit" },
	{ 0xfbc74f64, "__copy_from_user" },
	{ 0xb2f0a763, "_raw_spin_unlock" },
	{ 0xd6ee688f, "vmalloc" },
	{ 0xfc64f7da, "mutex_destroy" },
	{ 0x15692c87, "param_ops_int" },
	{ 0x67c2fa54, "__copy_to_user" },
	{ 0x2e5810c6, "__aeabi_unwind_cpp_pr1" },
	{ 0x97255bdf, "strlen" },
	{ 0x5692a8d0, "dev_set_drvdata" },
	{ 0x2d9e1451, "find_vpid" },
	{ 0x47939e0d, "__tasklet_hi_schedule" },
	{ 0xeb555322, "netif_carrier_on" },
	{ 0xb08ba1ba, "_raw_spin_lock_bh" },
	{ 0xf7cecaec, "skb_clone" },
	{ 0xf5bdc596, "dev_get_by_name" },
	{ 0x20000329, "simple_strtoul" },
	{ 0xf7802486, "__aeabi_uidivmod" },
	{ 0x58762bf3, "skb_copy" },
	{ 0xe300bf7, "schedule_work" },
	{ 0x695b2cfd, "down_interruptible" },
	{ 0x2a3aa678, "_test_and_clear_bit" },
	{ 0x36fd3576, "netif_carrier_off" },
	{ 0x62aa1015, "usb_kill_urb" },
	{ 0x98d2e4e1, "remove_proc_entry" },
	{ 0x7b029cbc, "filp_close" },
	{ 0x4e830a3e, "strnicmp" },
	{ 0x593a99b, "init_timer_key" },
	{ 0x2dfe6e76, "mutex_unlock" },
	{ 0x16f49395, "usb_autopm_get_interface" },
	{ 0x85df9b6c, "strsep" },
	{ 0x89a524b2, "usb_enable_autosuspend" },
	{ 0x999e8297, "vfree" },
	{ 0xc8fd8a4a, "usb_disable_autosuspend" },
	{ 0x91715312, "sprintf" },
	{ 0x7d11c268, "jiffies" },
	{ 0x28d4da70, "skb_trim" },
	{ 0xe2d5255a, "strcmp" },
	{ 0xcd88c59d, "__netdev_alloc_skb" },
	{ 0x7e38d039, "netif_rx" },
	{ 0xf8e01445, "__pskb_pull_tail" },
	{ 0x536ff674, "__init_waitqueue_head" },
	{ 0xe707d823, "__aeabi_uidiv" },
	{ 0x35b6b772, "param_ops_charp" },
	{ 0xfa2a45e, "__memzero" },
	{ 0xd5f2172f, "del_timer_sync" },
	{ 0x48b0f5c0, "skb_queue_purge" },
	{ 0x5f754e5a, "memset" },
	{ 0xc22e75d2, "_raw_spin_unlock_irqrestore" },
	{ 0x37befc70, "jiffies_to_msecs" },
	{ 0xe9aded55, "usb_deregister" },
	{ 0x78dc0a06, "__mutex_init" },
	{ 0x27e1a049, "printk" },
	{ 0x20c55ae0, "sscanf" },
	{ 0x71c90087, "memcmp" },
	{ 0x2344b0b9, "free_netdev" },
	{ 0xfaef0ed, "__tasklet_schedule" },
	{ 0x328a05f1, "strncpy" },
	{ 0x983d1be0, "register_netdev" },
	{ 0xbbb1fc64, "wireless_send_event" },
	{ 0x2db4a89f, "usb_control_msg" },
	{ 0x16305289, "warn_slowpath_null" },
	{ 0xf3d82ad6, "skb_push" },
	{ 0x2ebe8186, "mutex_lock" },
	{ 0x9545af6d, "tasklet_init" },
	{ 0x8834396c, "mod_timer" },
	{ 0xf95fa6f9, "kill_pid" },
	{ 0xf53d8915, "arm_delay_ops" },
	{ 0x3d790046, "skb_pull" },
	{ 0x55f2296f, "device_init_wakeup" },
	{ 0x8df707e8, "init_net" },
	{ 0xc9481534, "dev_kfree_skb_any" },
	{ 0xd79b5a02, "allow_signal" },
	{ 0x59e5070d, "__do_div64" },
	{ 0x9d5617e5, "flush_signals" },
	{ 0x4d746532, "skb_queue_tail" },
	{ 0x5a65b3a5, "netif_device_attach" },
	{ 0xce7a2ada, "usb_submit_urb" },
	{ 0xf9257b7a, "usb_get_dev" },
	{ 0x15c30e6, "_raw_spin_unlock_bh" },
	{ 0x7cbb50c0, "usb_reset_device" },
	{ 0x3bd1b1f6, "msecs_to_jiffies" },
	{ 0xf99c21a8, "usb_put_dev" },
	{ 0xd62c833f, "schedule_timeout" },
	{ 0x5952a882, "__raw_spin_lock_init" },
	{ 0x5d83e84e, "eth_type_trans" },
	{ 0x143cc31b, "create_proc_entry" },
	{ 0x166ec38b, "_raw_spin_lock" },
	{ 0xafa620b7, "_raw_spin_lock_irqsave" },
	{ 0xc479a064, "unregister_netdevice_queue" },
	{ 0x44da5d0f, "__csum_ipv6_magic" },
	{ 0x37a0cba, "kfree" },
	{ 0x9d669763, "memcpy" },
	{ 0x8f341d3a, "dev_alloc_name" },
	{ 0xc9f5df35, "up" },
	{ 0x6d7207ed, "usb_register_driver" },
	{ 0x13d63e3b, "skb_dequeue" },
	{ 0x550ed0fa, "unregister_netdev" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0x676bbc0f, "_set_bit" },
	{ 0xd2b2afe, "complete" },
	{ 0xb81960ca, "snprintf" },
	{ 0xc7044edd, "__netif_schedule" },
	{ 0xca54fee, "_test_and_set_bit" },
	{ 0x99bb8806, "memmove" },
	{ 0xe113bbbc, "csum_partial" },
	{ 0x85670f1d, "rtnl_is_locked" },
	{ 0x49ebacbd, "_clear_bit" },
	{ 0x3df79ab, "skb_put" },
	{ 0xd1b1e58, "wait_for_completion_timeout" },
	{ 0x6d044c26, "param_ops_uint" },
	{ 0x11083ea6, "skb_copy_bits" },
	{ 0x1c87b97f, "dev_get_drvdata" },
	{ 0x6bbb5373, "usb_free_urb" },
	{ 0xac5ddfc3, "usb_autopm_put_interface" },
	{ 0x760a0f4f, "yield" },
	{ 0xe1a4c246, "usb_alloc_urb" },
	{ 0x19d1bfb2, "filp_open" },
	{ 0x9ce9e70f, "alloc_etherdev_mqs" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";

MODULE_ALIAS("usb:v0BDAp8179d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "E54AFC4145D0A7E7121B00D");
