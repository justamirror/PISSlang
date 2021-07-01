from pisslang import PISSinterpreter
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(PISSinterpreter().console())