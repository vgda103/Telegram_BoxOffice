import telegram

token = open( 'token.txt', 'r' ).read()

# 메시지 '핸들러'
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

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

async def craw( update : Update, context ) -> None:
    print( update.message.chat_id ) # 채팅방 ID
    await update.message.reply_text( '' )
    pass

print( '--------------텔레그램 봇 실행-----------------' )
app = ApplicationBuilder().token( token ).build()

# 핸들러 등록
app.add_handler( CommandHandler( "hello", hello ) ) # /hello
app.add_handler( CommandHandler( "bye", bye ) ) # /bye
app.add_handler( CommandHandler( "craw", craw ) )
app.add_handler( CommandHandler( "rabbit", rabbit ) )

app.run_polling()
