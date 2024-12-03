import asyncio
from bleak import BleakClient, BleakScanner


async def connect_and_interact(address: str):
    # Connect to the BLE device
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        # Discover GATT services
        services = await client.get_services()
        print("Discovered GATT services:")
        for service in services:
            print(f"- Service UUID: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"  - Characteristic UUID: {characteristic.uuid}")
                print(f"    Properties: {characteristic.properties}")

                # If readable, read the value of the characteristic
                if "read" in characteristic.properties:
                    try:
                        value = await client.read_gatt_char(characteristic.uuid)
                        print(f"    Value: {value}")
                    except Exception as e:
                        print(f"    Failed to read characteristic: {e}")

                # Optionally subscribe to notifications for characteristics
                if "notify" in characteristic.properties:
                    def notification_handler(sender, data):
                        print(f"Notification from {sender}: {data}")

                    await client.start_notify(characteristic.uuid, notification_handler)
                    await asyncio.sleep(5)  # Receive notifications for 5 seconds
                    await client.stop_notify(characteristic.uuid)


async def main():
    # # Discover BLE devices
    # print("Scanning for devices...")
    # devices = await BleakScanner.discover()

    # if not devices:
    #     print("No devices found. Ensure your BLE peripheral is advertising.")
    #     return

    # # List discovered devices
    # for i, device in enumerate(devices):
    #     print(f"[{i}] {device.name} ({device.address})")

    # # Choose a device to connect to
    # index = int(input("Enter the index of the device to connect: "))
    # selected_device = devices[index]

    # print(f"Connecting to {selected_device.name} ({selected_device.address})...")
    # await connect_and_interact(selected_device.address)

    print(f"Connecting to D0:76:02:B0:05:51 ...")
    await connect_and_interact('D0:76:02:B0:05:51')


if __name__ == "__main__":
    asyncio.run(main())
