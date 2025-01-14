import asyncio
from bleak import BleakScanner

async def run():
    def detection_callback(device, advertisement_data):
        #EVT Lyon board if device.address == 'D0:76:02:B0:05:51': 
        if device.address == 'D0:76:02:B0:04:C1':
            print(f"Device: {device.address}, Advertisement Data: {advertisement_data}")

    scanner = BleakScanner(detection_callback)
    # scanner.register_detection_callback(detection_callback)

    print("Starting scanner...")
    await scanner.start()
    await asyncio.sleep(600)  # Scan for seconds
    await scanner.stop()
    print("Scanner stopped.")

loop = asyncio.get_event_loop()
loop.run_until_complete(run())