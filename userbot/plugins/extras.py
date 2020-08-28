import asyncio
import os
import sys


@register(events.NewMessage(pattern=r"^.yo$", outgoing=True))
async def yo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)		      


@register(events.NewMessage(pattern=r"^.noice$", outgoing=True))
async def noice(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.fwd_from:
            return
        message_id = e.message.id
        if e.reply_to_msg_id:
            message_id = e.reply_to_msg_id
        await e.client.send_message(
            e.chat_id,
            file="https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif"
        )
        await e.delete()		      


@register(events.NewMessage(pattern=r"^.lol$", outgoing=True))
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("L😂L")


@register(events.NewMessage(pattern=r"^.alol$", outgoing=True))	
async def alol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = "L😂L"
        for j in range(15):
            t = "L🤣L" if j%2==0 else "L😂L"
            await e.edit(t)
		

@register(events.NewMessage(pattern=r"^.nice$", outgoing=True))
async def nice(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Noice")
