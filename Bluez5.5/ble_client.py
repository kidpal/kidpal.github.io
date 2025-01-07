import asyncio
from datetime import datetime
from bleak import BleakClient, BleakScanner

async def connect_and_interact(address: str):
    # Connect to the BLE device
    async with BleakClient(address) as client:
        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        counter = 0
        while True:
            print(f"Connected: {client.is_connected}")

            # Discover GATT services
            services = await client.get_services()
            print("Discovered GATT services:")
            for service in services:
                print(f"- Service UUID: {service.uuid}")
                for characteristic in service.characteristics:
                    print(f"  - Characteristic UUID: {characteristic.uuid}")
                    print(f"    Properties: {characteristic.properties}")

                    # If writeable, write the value to the characteristic
                    if "write" in characteristic.properties:
                        try:
                            if ( characteristic.uuid == "0a0a1011-4e41-4249-5f49-445f42415345"):
                                # data = bytearray([0x88, 0x88, 0x88, 0x88])
                                # data = bytearray([counter+1,counter+2,counter+3,counter+4,counter+5])
                                # counter += 5

                                counter += 1
                                if counter%2 == 0:
                                    data = bytearray([0x65, 0x00]) # Mio Command 0x65, item 0x00
                                else:
                                    data = bytearray([0x65, 0x01]) # Mio Command 0x65, item 0x01
                                
                                if counter >= 255: counter = 0
                                await client.write_gatt_char(characteristic.uuid, data)
                                print("    Write values: ", end=" ")
                                for d in data: print(f"{int(d)}", end=" ")
                                print(f" successfully written to characteristic {characteristic.uuid} \n")
                        except Exception as e:
                            print(f"    Failed to write characteristic: {e}")

                    # If readable, read the value of the characteristic
                    if "read" in characteristic.properties:
                        try:
                            value = await client.read_gatt_char(characteristic.uuid)
                            if ( characteristic.uuid == "0a0a1011-4e41-4249-5f49-445f42415345"):
                                print(f"   Read bytes: {value}")
                                print("    Read values: ",end=" ")
                                for v in value: print(int(v), end=" ")
                            else:
                                print(f"    Read bytes: {value}")
                        except Exception as e:
                            print(f"    Failed to read characteristic: {e}")

                    # Optionally subscribe to notifications for characteristics
                    if "notify" in characteristic.properties:
                        def notification_handler(sender, data):
                            print(f"Notification from {sender}: {data}")

                        await client.start_notify(characteristic.uuid, notification_handler)
                        await asyncio.sleep(5)  # Receive notifications for 5 seconds
                        await client.stop_notify(characteristic.uuid)
                    print("\n")
                print("\n")
                
            # try:
            #     # Replace with the UUID of the GATT characteristic to write to
            #     characteristic_uuid = "0000bbbb-0000-1000-8000-00805f9b34fb"
            #     # Replace with the data to write (in bytes)
            #     data = bytearray([0x88, 0x88, 0x88, 0x88])

            #     await client.write_gatt_char(characteristic_uuid, data)
            #     print(f"Data {data} successfully written to characteristic {characteristic_uuid}")
            # except Exception as e:
            #     print(f"Failed to write to GATT characteristic: {e}")
            
            print(f"\nTest start: {start_time} to {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            await asyncio.sleep(15)

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
