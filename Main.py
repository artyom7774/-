from DATA.Modules.root import *
from tkinter import *
import asyncio


async def update():
    while True:
        await asyncio.sleep(1)
        print('Hello from coroutine')


async def main():
    root = Root()

    root.config(menu=root.main_menu)

    await update()

    root.mainloop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
