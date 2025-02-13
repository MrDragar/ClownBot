import asyncio
import logging

from pyrogram import Client

from src import config
from src.handlers import register_handlers


def main():
    logging.basicConfig(
        level=config.log_level,
        format=config.log_format,
        filename=config.log_file,
        filemode="a"
    )
    bot = Client(
        name=config.LOGIN,
        phone_number=config.PHONE,
        password=config.PASSWORD,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        workdir="."
    )
    logging.info("register handlers")
    register_handlers(bot)
    logging.info("registered handlers")
    bot.run()


if __name__ == "__main__":
    main()
