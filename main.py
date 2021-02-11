# import asyncio
# from bleak import BleakScanner

# async def run():
#     devices = await BleakScanner.discover()
#     for d in devices:
#         print(d)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())

import asyncio
import platform

from bleak import BleakClient, BleakScanner


async def print_services(mac_addr: str):
    device = await BleakScanner.find_device_by_address(mac_addr)
    async with BleakClient(device) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_services(mac_addr))