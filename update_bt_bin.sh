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
if [ -e "/mnt/mmc/bluetoothctl" ]; then
	cp /mnt/mmc/bluetoothctl /customer/bluetooth/bin/
	sync
	chmod a+rx /customer/bluetooth/bin/bluetoothctl
	sync
	echo "bluetoothctl is copied to /customer/bluetooth/bin/"
fi
echo " "
if [ -e "/mnt/mmc/bluetoothd" ]; then
	cp /mnt/mmc/bluetoothd /customer/bluetooth/bin/
	sync
	chmod a+rx /customer/bluetooth/bin/bluetoothd
	sync
	echo "bluetoothd is copied to /customer/bluetooth/bin/"
fi
echo " "
ls -al /customer/bluetooth/bin/bluetoothd
ls -al /customer/bluetooth/bin/bluetoothctl
echo " "
echo "Successfully updated bluetoothd and bluetoothctl."
