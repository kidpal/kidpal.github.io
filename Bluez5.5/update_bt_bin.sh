#!/bin/sh
rm -rf /customer/bluetooth/bin/bluetoothd
sync
if [ "`ls /customer/bluetooth/bin/bluetoothd`" == "" ]; then
	echo "/customer/bluetooth/bin/bluetoothd is deleted"
fi

echo " "
rm -rf /customer/bluetooth/bin/bluetoothctl
sync
if [ "`ls /customer/bluetooth/bin/bluetoothctl`" == "" ]; then
	echo "/customer/bluetooth/bin/bluetoothctl is deleted"
fi

echo " "
rm -rf /customer/bluetooth/bin/btgatt-server
sync
if [ "`ls /customer/bluetooth/bin/btgatt-server`" == "" ]; then
	echo "/customer/bluetooth/bin/btgatt-server is deleted"
fi

echo " "
if [ -e "/mnt/mmc/bluetoothctl" ]; then
	cp /mnt/mmc/bluetoothctl /customer/bluetooth/bin/
	sync
	chmod a+rx /customer/bluetooth/bin/bluetoothctl
	sync
	ls -al /customer/bluetooth/bin/bluetoothctl
	echo "bluetoothctl is copied to /customer/bluetooth/bin/"
fi

echo " "
if [ -e "/mnt/mmc/bluetoothd" ]; then
	cp /mnt/mmc/bluetoothd /customer/bluetooth/bin/
	sync
	chmod a+rx /customer/bluetooth/bin/bluetoothd
	sync
	ls -al /customer/bluetooth/bin/bluetoothd
	echo "bluetoothd is copied to /customer/bluetooth/bin/"
	
fi

echo " "
if [ -e "/mnt/mmc/btgatt-server" ]; then
	cp /mnt/mmc/btgatt-server /customer/bluetooth/bin/
	sync
	chmod a+rx /customer/bluetooth/bin/btgatt-server
	sync
	ls -al /customer/bluetooth/bin/btgatt-server
	echo "btgatt-server is copied to /customer/bluetooth/bin/"
fi

echo " "
