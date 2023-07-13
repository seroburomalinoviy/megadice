import asyncio
from conf import Token

from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import random

# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/d4", description="Кинуть кубик Д4"),
        BotCommand(command="/d6", description="Кинуть кубик Д6"),
        BotCommand(command="/d8", description="Кинуть кубик Д8"),
        BotCommand(command="/d10", description="Кинуть кубик Д10"),
        BotCommand(command="/d12", description="Кинуть кубик Д12"),
        BotCommand(command="/d20", description="Кинуть кубик Д20"),
    ]
    await bot.set_my_commands(commands)


async def main():

    stikerIds = {
        "d41": "CAACAgIAAxkBAAEJLc1keMzNq8z8oiaA4-35iMMYCEgt1wAC9i4AAkxCyUv5PBj0AycAARovBA",
        "d42": "CAACAgIAAxkBAAEJLdtkeM7X9mQ6q9LUFj5YLg5xSW0OpwACrywAAmOdwUvIHTWBSd-dRS8E",
        "d43": "CAACAgIAAxkBAAEJLd1keM7lUw9Fum3SQp9e2y3hnKjRPAAC5DIAAvc8wUtVbJ0jk39EBy8E",
        "d44": "CAACAgIAAxkBAAEJLd9keM7zS8ZeN5Slead8Go875CTUJQACVS0AAmUiwEt03wUmBSl_ZS8E",
        
        "d61": "CAACAgIAAxkBAAEJLeFkeNAQoq3Go2hu0yXAGhV_sV-dsgACwCwAAgVbwUtOjwQ9VqYHHi8E",
        "d62": "CAACAgIAAxkBAAEJLeNkeNAeDc-E86H9N4z9WFbNv1CGYAAC-isAAlNAyEvSywatbYYIqi8E",
        "d63": "CAACAgIAAxkBAAEJLeVkeNAy56qSUyRpqVpz5r96OH21JQACyS4AAoy4yEvqtOIbZcPCEy8E",
        "d64": "CAACAgIAAxkBAAJSSmR40LBPhcFVWNwy8ZQV_pahO1w7AAIHNgACVoDAS-aGV1VuL-vCLwQ",
        "d65": "CAACAgIAAxkBAAJSTGR40Lym0R3ffZY_vm9hMGQE7vrnAAL8KQACOs_JS115talXdkLPLwQ",
        "d66": "CAACAgIAAxkBAAJSTmR40MNnSDZxNRGDEpsDGqHotyA2AALgLwACQaPBS8GaS9VgxSqLLwQ",

        "d81": "CAACAgIAAxkBAAJSUGR40MxHN2qDquGWV_7aofDFe7P8AAInMQAChNzAS-crPl5YPZsJLwQ",
        "d82": "CAACAgIAAxkBAAJSUmR40NIToV5P7iLS61WnEVgO71CoAALAKgACUjLISy0CXkEBt4RaLwQ",
        "d83": "CAACAgIAAxkBAAJSVGR40Ni0cC69xYRET9eHaj5tpqsEAALCLwACMqXISyVjRdHc8KnHLwQ",
        "d84": "CAACAgIAAxkBAAJSVmR40N-f0dtfecsy6CBmdCKpfEYbAAKxKQACT8DJS9mJFmw31lmJLwQ",
        "d85": "CAACAgIAAxkBAAJSWGR40OVjl2F8H8_KrWPXF-c7TDaLAALPJQACQofJSyz3ZElka4b0LwQ",
        "d86": "CAACAgIAAxkBAAJSWmR40OxyObeJja8LL0y-PmSInRcsAALTLAACbefJS2jwuVLWOPo2LwQ",
        "d87": "CAACAgIAAxkBAAJSXGR40PNX7GPkYzXXXGlkIhCUHF_3AAKlLAACQU7JS4TSEkvZ3bxSLwQ",
        "d88": "CAACAgIAAxkBAAJSXmR40PwlUt3FkyOTnlTX1CvBiJpgAAItMAACmjzJS82k4MpxIDQ3LwQ",

        "d101": "CAACAgIAAxkBAAJSYGR40QYWqw6uB19tq-p6plkEp-wmAAICLwACd3fISz383veLiHMSLwQ",
        "d102": "CAACAgIAAxkBAAJSYmR40Q2oxX4FkKP_ekVfq3lwfY-UAALpKwAC7qjJS9WiLAK2wsVBLwQ",
        "d103": "CAACAgIAAxkBAAJSZGR40RXhOkYmbpNhR_gypHCnGg61AAJ_MgAC4A3ISzktHMzbG0ocLwQ",
        "d104": "CAACAgIAAxkBAAJSZmR40Rv0JXKlVOn3yayOJFgTCDZJAALnMAACJUHJS52F2IQ40qrCLwQ",
        "d105": "CAACAgIAAxkBAAJSaGR40SIYuQwEDlXrsiqqxJkCCL0_AALpNgACz_zJSxbvyD_Z5zIxLwQ",
        "d106": "CAACAgIAAxkBAAJSamR40ShcnLplXiNVqkGJ3A3ITKhAAAKBLAACwifIS4C9MfdmjMgpLwQ",
        "d107": "CAACAgIAAxkBAAJSbGR40S_qrVinrAH4Ki8jY8WOAmpQAAJNLQADkshL3GhX3ykEBJAvBA",
        "d108": "CAACAgIAAxkBAAJSbmR40TVRAvQlO4_xpuCg6ur-HbncAAI5MAAC1yXIS8-zofo9AUSyLwQ",
        "d109": "CAACAgIAAxkBAAJScmR40UCUKV9zTpH1xtPJYzRGf8dMAAL7NAAC0iXISxBnrhv__JC8LwQ",
        "d1010": "CAACAgIAAxkBAAJSdGR40UbnmnSJaHxOp0WalurpcTPNAALLLQACl1fJSwun74In2RLZLwQ",

        "d121": "CAACAgIAAxkBAAJSdmR40Vcbm6N0--b5uZVmEeDky7dOAAJVMQACCt7JS96Ax3cvoG81LwQ",
        "d122": "CAACAgIAAxkBAAJSeGR40WSP_bdjrKr-3GECbxZXlMchAAJMMAACRUjJS2Qc7q3vCnTyLwQ",
        "d123": "CAACAgIAAxkBAAJSemR40Wxe0vmif2o6ueBQFc1S7Df7AAIyMwACh-jJS0A71X5I8OG-LwQ",
        "d124": "CAACAgIAAxkBAAJSfGR40XKrHp3SIZusTEsUisd0wIdYAALHKQAC7E7JS7LSXSPD96mWLwQ",
        "d125": "CAACAgIAAxkBAAJSfmR40XdRpMCE62ZmRhOxV_zCs6CHAAJxLAACG4rIS1Y2iRNqIlxBLwQ",
        "d126": "CAACAgIAAxkBAAJSgGR40X2b0cqj4wr59OJPOEiJWqxSAAI_LAACA4vJSzPI07s8ZDcaLwQ",
        "d127": "CAACAgIAAxkBAAJSgmR40YN-pMQSVo6TiTJ9Nl__Ab6JAAKwPwACs8rJS8GyZdKqZAVdLwQ",
        "d128": "CAACAgIAAxkBAAJShGR40YlxBuMDHbg3B7nDQhsSfNQKAAL5MAACFqTIS4JnrmUEI-liLwQ",
        "d129": "CAACAgIAAxkBAAJShmR40Y6VdEgbXYf7kym5676pZSbRAAKgLAAC57zAS6shbvqIJe3fLwQ",
        "d1210": "CAACAgIAAxkBAAJSiGR40ZVXabRlZJpxRwd-zms51o0iAAJILgACl-vJS1IY6dtqc_ppLwQ",
        "d1211": "CAACAgIAAxkBAAJSimR40ZtMQjkwus4yWkLbOXR-JSAVAALYJwACG-7ISxQa74eJD-1BLwQ",
        "d1212": "CAACAgIAAxkBAAJSjGR40aAT7n8yqIUSEAVGNNGINt0IAAIzMQACgknJSy6XbPNKZptFLwQ",

        "d201": "CAACAgIAAxkBAAJSjmR40asz8vnwOfIsTFBGtzzZWJ_TAAKhLAACloPBS-PaAyQotahOLwQ",
        "d202": "CAACAgIAAxkBAAJSkGR40bC3j7nJ0zuMJDhtwkBlqObuAAIXLQACxurJS7aB2rXHWgF3LwQ",
        "d203": "CAACAgIAAxkBAAJSkmR40bbfW92D7HwVoMPD1-2F0AeGAALHLQACFoXIS7u2h869RrA9LwQ",
        "d204": "CAACAgIAAxkBAAJSlGR40bzDcsEf4xffKBCNBOyXyl8lAAKZLQACMqrJS_zbpCOdWo3FLwQ",
        "d205": "CAACAgIAAxkBAAJSlmR40cE2x19-bwABuousDl9WNMvUxgACNi8AAi1QyEtsntuBuNqA-i8E",
        "d206": "CAACAgIAAxkBAAJSmGR40cgfdy_Vu05b5CF5rmd4T6UCAAJBLAAC10vIS_UoAvEHqEq3LwQ",
        "d207": "CAACAgIAAxkBAAJSmmR40c7GJY1s-QO7s5M1QydBMTu_AAKLMQAC3w3IS9bhh8te2a9BLwQ",
        "d208": "CAACAgIAAxkBAAJSnGR40dL_wuqKOBuMyVL4ibw_hpi_AAIBLwACYprJS3BJm6a_uoxzLwQ",
        "d209": "CAACAgIAAxkBAAJSnmR40dndNh4VR_88zIlmVIFv2hBLAAKaMQACRfTISy94ys3fI-LOLwQ",
        "d2010": "CAACAgIAAxkBAAJSoGR40d1QrCz4KazaQ86KBJw42C24AAL9LwACsQAByEsVPzcPtQlcOS8E",
        "d2011": "CAACAgIAAxkBAAJSomR40eTUUJ6DtgeyrxnHK-QIZkGcAALhKgACTBTAS8By8r2p8bGxLwQ",
        "d2012": "CAACAgIAAxkBAAJSpGR40ekYbVlKhxlQehpgmMtDb47vAAKNLgAC__3IS8SmJvx01njHLwQ",
        "d2013": "CAACAgIAAxkBAAJSpmR40e8LtQL4bI0PG2yhrHQ2lB6QAAJqLAAC0BHJS-OhcGcbkHfwLwQ",
        "d2014": "CAACAgIAAxkBAAJSqGR40fXURfsylT7j_JyYcQPcd7L6AAI6LQACxTnAS0v_01n8SC03LwQ",
        "d2015": "CAACAgIAAxkBAAJSqmR40ftU7Qyjki8AAYgTTWy9_Sn22QACNC8AAmmbyUu1h6Oqs4NILi8E",
        "d2016": "CAACAgIAAxkBAAJSrGR40gABU4SdJnLXi0RH1ZofwoXSxQACSioAArfvwEuRcYYcmIm9gy8E",
        "d2017": "CAACAgIAAxkBAAJSrmR40gYlQP2asahJIG0xczjpXDhuAAKaJwACg_7IS9Rr9ILcJox1LwQ",
        "d2018": "CAACAgIAAxkBAAJSsGR40gzW59cHMOXQle9GfG8p5znmAAK_NAAC94PJSxZlk_yLVzjNLwQ",
        "d2019": "CAACAgIAAxkBAAJSsmR40hHodaSP3r1vQdsii5gRckvbAAJ9LAACShTJSwShJxCekUldLwQ",
        "d2020": "CAACAgIAAxkBAAJStGR40hbUxv3J1QuwG95B2iyS3q4EAAKpKAACtoTBS5sKqlwOoP-7LwQ",


    }



    # Создание бота, диспетчера и хранилища состояний
    bot = Bot(token=Token)

    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    async def d4(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 4)
        await message.answer_sticker(stikerIds[f"d4{str(result)}"])

    async def d6(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 6)
        await message.answer_sticker(stikerIds[f"d6{str(result)}"])

    async def d8(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 8)
        await message.answer_sticker(stikerIds[f"d8{str(result)}"])

    async def d10(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 10)
        await message.answer_sticker(stikerIds[f"d10{str(result)}"])

    async def d12(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 12)
        await message.answer_sticker(stikerIds[f"d12{str(result)}"])

    async def d20(message: types.Message, state: FSMContext):
        await state.finish()
        result = random.randint(1, 20)
        await message.answer_sticker(stikerIds[f"d20{str(result)}"])

    async def dgoogle(message: types.Message, state: FSMContext):
        await state.finish()
        await message.answer("Bot Made by @Sergeevid")

    async def dildo(message: types.Message, state: FSMContext):
        await state.finish()
        await message.answer("Not bad little prankster")

    dp.register_message_handler(d4, commands="d4", state='*')
    dp.register_message_handler(d6, commands="d6", state='*')
    dp.register_message_handler(d8, commands="d8", state='*')
    dp.register_message_handler(d10, commands="d10", state='*')
    dp.register_message_handler(d12, commands="d12", state='*')
    dp.register_message_handler(d20, commands="d20", state='*')
    dp.register_message_handler(dgoogle, commands="dgoogle", state='*')
    dp.register_message_handler(dildo, commands="dildo", state='*')

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    await dp.skip_updates()
    await dp.start_polling()

    # Закрытие хранилища
    await dp.storage.close()
    await dp.storage.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())