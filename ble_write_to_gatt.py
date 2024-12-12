import asyncio
from bleak import BleakClient

# Function to write data to a GATT characteristic
async def write_to_gatt_characteristic(device_address, characteristic_uuid, data):
    try:
        # Connect to the BLE peripheral
        async with BleakClient(device_address) as client:
            print(f"Connected to {device_address}")
            
            # Write data to the specified characteristic
            await client.write_gatt_char(characteristic_uuid, data)
            print(f"Data {data} successfully written to characteristic {characteristic_uuid}")
    except Exception as e:
        print(f"Failed to write to GATT characteristic: {e}")

# Main function
if __name__ == "__main__":
    # Replace with the BLE device address (Windows format: XX:XX:XX:XX:XX:XX)
    device_address = "D0:76:02:B0:05:51"

    # Replace with the UUID of the GATT characteristic to write to
    characteristic_uuid = "00002a05-0000-1000-8000-00805f9b34fb"

    # Replace with the data to write (in bytes)
    data = bytearray([0x88, 0x88, 0x88, 0x88])

    # Run the asyncio event loop
    asyncio.run(write_to_gatt_characteristic(device_address, characteristic_uuid, data))
