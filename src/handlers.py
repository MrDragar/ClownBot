import logging

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.emoji import CLOWN_FACE

from src.config import CLOWN_ID


async def post_clown(bot: Client, message: Message) -> None:
    logging.info(f"got message from {message.from_user.id}")
    if message.from_user.id != int(CLOWN_ID):
        return
    logging.info(f"{message.from_user.id} is a clown")
    await message.react(emoji=CLOWN_FACE)


def register_handlers(bot: Client) -> None:
    bot.add_handler(MessageHandler(post_clown))
