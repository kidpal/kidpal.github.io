#!/bin/sh

case "$1" in
  start)
  	echo "Init BT module ..."

	if [ "`lsmod|grep hci_uart`" == "" ]; then
		echo "wifip 1" > /tmp/cardv_fifo
		insmod /customer/modules/4.9.227/hci_uart.ko
	fi

	sleep 1

	if [ $? -eq 1 ]; then
		exit 1
	fi

	./customer/bluetooth/rtk_hciattach -n -s 115200 /dev/ttyS2 rtk_h5 &
	sleep 1
	rm /customer/bluetooth/bluez_build/dbus/var/run/dbus/pid
	sleep 1
	./customer/bluetooth/bin/dbus-daemon --system &
	sleep 1
	./customer/bluetooth/bin/bluetoothd -n -d -C &
	sleep 1
	./customer/bluetooth/bin/hciconfig hci0 up
	sleep 1
	
	SSID=`nvconf get 1 wireless.ap.ssid`
	./customer/bluetooth/bin/hciconfig hci0 name $SSID
	
	sleep 1
	./customer/bluetooth/bin/hciconfig hci0 reset
	
	#sleep 1
	#./customer/bluetooth/bin/hciconfig hci0 leadv
	#sleep 1
	#./customer/bluetooth/bin/hcitool -i hci0 cmd 0x08 0x0006 20 00 20 00 00 00 00 00 00 00 00 00 00 07 00
	#sleep 1
	#./customer/bluetooth/bin/hcitool -i hci0 cmd 0x08 0x0008 0D FF 4D 69 56 75 65 5F 62 30 30 35 35 30 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	#sleep 1
	#./customer/bluetooth/bin/hcitool -i hci0 cmd 0x08 0x000A 01
	
	#sleep 1
	#./customer/bluetooth/bin/bluetoothctl advertise on &
	#echo "BT running ......"
;;
  stop)
    ./customer/bluetooth/bin/hciconfig hci0 down
	echo " Kill all process of BT"
	busybox killall bluetoothd
	busybox killall dbus-daemon
	#rm /customer/bluetooth/bluez_build/dbus/var/run/dbus/pid
	busybox killall rtk_hciattach
	#Power off RTL8821
	echo "wifip 0" > /tmp/cardv_fifo
;;
  rf)
    echo "Init BT module ..."

	if [ "`lsmod|grep hci_uart`" == "" ]; then
		echo "wifip 1" > /tmp/cardv_fifo
		insmod /customer/modules/4.9.227/hci_uart.ko
	fi

	sleep 1

	if [ $? -eq 1 ]; then
		exit 1
	fi

	./customer/bluetooth/rtk_hciattach -n -s 115200 /dev/ttyS2 rtk_h5 &
	sleep 1
	rm /customer/bluetooth/bluez_build/dbus/var/run/dbus/pid
	sleep 1
	./customer/bluetooth/bin/dbus-daemon --system &
	sleep 1
	./customer/bluetooth/bin/bluetoothd -n -d -C &
	sleep 1
	./customer/bluetooth/bin/hciconfig hci0 up
	sleep 1
	./customer/bluetooth/bin/hciconfig hci0 name 'MiVue_'
	sleep 1
	./customer/bluetooth/bin/hciconfig hci0 reset
	sleep 1
	cp mnt/mmc/bluetooth/GSD_Bluetooth_tool/mp_rtl8821c_fw lib/firmware/.
	sleep 1
	cp mnt/mmc/bluetooth/GSD_Bluetooth_tool/mp_rtl8821cs_config lib/firmware/.
	sleep 1
	cp mnt/mmc/bluetooth/GSD_Bluetooth_tool/rtlbtmp lib/firmware/.
	sleep 1
	chmod 644 lib/firmware/mp_rtl8821c_fw
	sleep 1
	chmod 644 lib/firmware/mp_rtl8821cs_config
	sleep 1
	chmod 777 lib/firmware/rtlbtmp
	sleep 1
	ps -ef|grep blue
;;
  *)
	echo "Usage: $0 {start|stop|rf}"
	exit 1
esac

exit $?

