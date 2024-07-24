import asyncio
import telegram

import BoxOffice

class cht_bot():
    def __init__(self) -> None:
        
        self.bot = telegram.Bot( '7057430361:AAFDR9s_hNFAj85B2XkdXhq_1dAkLwaCoeo' )
        self.id = '7117704024'
        
        self.bot.send_message( chat_id = id, text = '테스트' )
        
        # 비동기 함수 실행
        asyncio.run(send_test_message())
        pass

        
    async def send_test_message(  ):
        bot_token = '7057430361:AAFDR9s_hNFAj85B2XkdXhq_1dAkLwaCoeo'
        chat_id = '7117704024'

        boxoffice = BoxOffice().kobis_connect()
        in_str = boxoffice.top10_print()
        # print( type( in_str ) )

        bot = telegram.Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=in_str )
        pass
    pass







