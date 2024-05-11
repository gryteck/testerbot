import asyncio
import logging

from handlers import dp
from config import bot


async def main() -> None:
    pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING,
                        # filename='main.log', filemode='w',
                        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s', force=True)
    asyncio.run(dp.start_polling(bot))
