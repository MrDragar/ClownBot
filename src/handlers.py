import asyncio
import logging

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.emoji import CLOWN_FACE
from pyrogram.filters import dice, create

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


async def delete_won_dice(message: Message) -> bool:
    """True, если нельзя ставить клоуна"""
    if not message.dice or message.dice.emoji != '🎰':
        return False
    if message.dice.value in [1, 22, 43, 64]:
        try:
            await message.delete()
            return False
        finally:
            return True
    return False


async def resend_until_win(bot: Client, message: Message) -> None:
    logging.info("Is my dice")
    if message.dice.emoji != "🎰":
        return
    count = 0
    while message.dice.value not in [1, 22, 43, 64] and count < 100:
        await message.delete()
        message = await bot.send_dice(
            chat_id=message.chat.id, emoji=message.dice.emoji,
            disable_notification=True
        )
        logging.info(f"New dice value: {message.dice.value}")


async def post_clown(bot: Client, message: Message) -> None:
    logging.info(f"got message from {message.from_user.id}")

    if message.from_user.id != int(CLOWN_ID):
        return
    if is_censored_text(message.text):
        return
    if await delete_won_dice(message):
        return

    logging.info(f"{message.from_user.id} is a clown")
    await message.react(emoji=CLOWN_FACE)


async def me_filter(_, bot: Client, message: Message):
    if bot.me.id == message.from_user.id:
        logging.info("Is me")
        return True
    return False


def register_handlers(bot: Client) -> None:
    bot.add_handler(MessageHandler(resend_until_win, create(me_filter) & dice))
    bot.add_handler(MessageHandler(post_clown))
