import telegram
import os

# 커스텀 클레스 정의
# 환경변수 등록
import sys
sys.path.append( r'C:\Users\SDA12\Desktop\AiWork' )

# 커스텀 모둘 업핸드
from De_to_En.EntoDe_code import EntoDe_code


token = open( 'C:/Users/SDA12/Desktop/AiWork/De_to_En/Telegram_token.txt', 'r' ).read()


# 메시지 '핸들러'
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from BoxOffice.BoxOffice import BoxOffice

# 메시지 처리기 = 핸들러
async def hello( update : Update, context ) -> None: # /hello 사용자 입력
    await update.message.reply_text(
        f'Hello { update.effective_user.first_name }' # Hello ~~ 해서 응답 변환
    )
    pass

async def bye( update : Update, context ) -> None:
    # 크롤링코드 실행
    # 데이터를 받아서 문자열로 변환
    print( update.message.text.split() )
    await update.message.reply_text(
        f'Bye { update.effective_user.first_name }'
    )
    pass

import requests
async def rabbit( update : Update, context ) -> None:
    await update.message.reply_text( '토끼사진을 검색 합니다' )
    rabbit_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Bunny_rabbit_at_Alligator_Bay%2C_Beauvoir%2C_France.jpg/220px-Bunny_rabbit_at_Alligator_Bay%2C_Beauvoir%2C_France.jpg'
    r = requests.get( rabbit_url )
    await update.message.reply_photo( r.content )
    pass

async def top10( update : Update, context ) -> None:
    # boxoffice = BoxOffice()
    # boxoffice.kobis_connect()
    in_str = boxoffice.top10_print()
    
    # await update.message.reply_text( boxoffice.top10_print() )
    # await update.message.reply_text(
    #     f'craw { in_str }'
    # )
    await update.message.reply_text(
        f'{ in_str }'
    )
    pass

# asyncio.run(bot.send_message(chat_id = chat_id, text = "python test"))

print( '--------------텔레그램 봇 실행-----------------' )

boxoffice = BoxOffice()
boxoffice.kobis_connect()

app = ApplicationBuilder().token( token ).build()

# 핸들러 등록
app.add_handler( CommandHandler( "hello", hello ) ) # /hello
app.add_handler( CommandHandler( "bye", bye ) ) # /bye
app.add_handler( CommandHandler( "top10", top10 ) )
app.add_handler( CommandHandler( "rabbit", rabbit ) )

app.run_polling()

bot = telegram.Bot( token )
# chat_id = os.environ.get('')
chat_id = 1
# bot.sendMessage(chat_id, text='메세지 보내기 테스트', parse_mode="Markdown")
bot.send_message( chat_id=chat_id, text='메세지 보내기 테스트' )


# https://api.telegram.org/bot7057430361:AAFDR9s_hNFAj85B2XkdXhq_1dAkLwaCoeo/getUpdates
# t.me/T_tsts4506_bot

# https://api.telegram.org/bot7057430361:AAFDR9s_hNFAj85B2XkdXhq_1dAkLwaCoeo/getUpdates