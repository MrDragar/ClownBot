import logging

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.emoji import CLOWN_FACE

from src.config import CLOWN_ID


def is_censored_text(text: str) -> bool:
    """True, если нельзя ставить клоуна"""
    if text is None:
        return False
    if all(not symbol.isalpha() for symbol in text):
        return False

    if all((symbol in "zv" or not symbol.isalpha() for symbol in text.strip().lower())):
        logging.info("Is ZV")
        return True
    if "росси" in text.strip().lower():
        logging.info("About Russian")
        return True
    if "путин" in text.strip().lower():
        logging.info("About Putin")
        return True
    return False


async def post_clown(bot: Client, message: Message) -> None:
    logging.info(f"got message from {message.from_user.id}")
    if message.from_user.id != int(CLOWN_ID):
        return
    if is_censored_text(message.text):
        return
    logging.info(f"{message.from_user.id} is a clown")
    await message.react(emoji=CLOWN_FACE)


def register_handlers(bot: Client) -> None:
    bot.add_handler(MessageHandler(post_clown))
