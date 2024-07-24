import os

# 현제 경로 재정의
# os.chdir( './home/ubuntu/workspace' ) # ./
print( 'hello aws' )

import pymysql
# from workspace.cht_bot import cht_bot
# import cht_bot

# 만들었던 크롤링 부분을 클레스화?
# 정의
import requests
import json
from bs4 import BeautifulSoup

# Crawling
class Crawling:

    def __init__(self) -> None:
        """
        생성자
        """
        self.respoonse = requests
        return self
        pass # 생성자 끝

    def url_connect( self, URL ) -> int:
        """
        URL : str, 접속할 사이트주소
        reutnr : int, respoonse 상태를 알려준다.
        """

        # 사이트에 요청
        self.respoonse = requests.get( URL, headers = {} )
        return self.get_states()        
        pass # 메소드 get_connect

    def get_states( self ) -> int:
        """
        respoonse 상태를 알려준다.
        """
        return self.respoonse.status_code
        pass # get_res_states 

    def get_text( self ) -> str:
        """
        respoonse의 속성의 텍스트를 넘겨준다
        """
        return self.respoonse.text
        pass # get_text 끝

    def get_to_json( self ):
        """
        load를 사용하니 사용하지 말것
        load는 파일에서 읽어올때 사용함
        loads는 문자열을 읽을때 사용함
        respoonse를 json 형태로 파싱한 데이터를 넘겨준다
        """
        # j_data = json.loads( self.respoonse.text )
        return json.load( self.respoonse.text )
        pass # get_to_json 끝
    
    def get_to_jsons( self ):
        """
        loads를 사용함
        load는 파일에서 읽어올때 사용함
        loads는 문자열을 읽을때 사용함
        respoonse를 json 형태로 파싱한 데이터를 넘겨준다
        """
        # j_data = json.loads( self.respoonse.text )
        return json.loads( self.respoonse.text )
        pass # get_to_json 끝
    
    def get_to_soup( self ):
        """
        respoonse를 BeautifulSoup 형태로 파싱한 데이터를 넘겨준다
        """
        return BeautifulSoup( self.respoonse.text, 'html.parser' )
        pass # get_to_soup 끝

    pass # class Crawling 끝

# 정의
# 부모 정의
from BoxOffice.Crawling import Crawling
from workspace.Crawling import Crawling
import Crawling

# 클레스 내 필요한거
import datetime as dt
import json
import sys

# # 커스텀 클레스 정의
# # 환경변수 등록
sys.path.append( r'C:\Users\SDA12\Desktop\AiWork' )

# # 커스텀 모둘 업핸드
from De_to_En.EntoDe_code import EntoDe_code

class BoxOffice( Crawling ):

    def __init__(self) -> None:
        # 부모 생성자 호출
        super().__init__()

        # 속성 정의
        # self.js_data
        self.daily_data = {}
        # return self
        pass # 생성자 끝

    def kobis_connect( self ):
                
        key = EntoDe_code().get_decoder( 'BoxOffice/Yek.br' )

        # 하루전 날자를 받는다
        date_str = dt.datetime.now().strftime('%Y')  + str( dt.datetime.now().month ).zfill(2) + str( dt.datetime.now().day - 1 ).zfill(2)

        # print( date_str )

        # 접속할 사이트
        URL = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={date_str}'

        # print( URL )

        self.url_connect( URL )

        # print( self.respoonse )
        # print( self.respoonse.text )

        # 사이트에서 받아온 값을 json 형식을 파일을 변환
        js_data = self.get_to_jsons()
        
        # json 형식의 파일 안에서 boxOfficeResult에 dailyBoxOfficeList의 데이터를 가져옴
        # daily_data의 딕셔너리에 키 값으로 날자( YYYYMMDD 형식 ) 넣고 
        # 데이터 값에 boxOfficeResult에 dailyBoxOfficeList의 데이터를 리스트 형식으로 넣는다
        self.daily_data = { date_str : js_data[ 'boxOfficeResult']['dailyBoxOfficeList' ] }
        return self
        pass # kobis_connect 끝

    # 데이터 출력
    def top10_print( self ):
        out_str = ''
        # 출력 반복문
        for day in self.daily_data:  # 딕셔너리 저근 for 문
            for data in self.daily_data[ day ]:  # 리스트 접근 for 문
                n_or_o = '' # 문자열을 저장할 임시변수
                # data['rankOldAndNew']의 값에 따라 기존 와 신규를 임시변수에 저장
                if data['rankOldAndNew'] == 'OLD':
                    n_or_o = '기존'
                else:
                    n_or_o = '신규'
                
                # 순위와 영화 이름 그리고 신규 또는 기존으로 출력
                # print( data['rank'] + ' ' + data['movieNm'] + ' ' + n_or_o  )
                out_str += data['rank'] + ' ' + data['movieNm'] + ' ' + n_or_o + '\n'
                pass # data for 문 끝
            pass # day for 문 끝
        return out_str
        pass # top10_print 끝

    def new_movie( self ) -> bool:
        """
        새 영화가 있으면 True, 없으면 False 를 반환
        """
        # 새로운 영화 있는지 탐색
        for day in self.daily_data:  # 딕셔너리 접근 for 문
            for idx in self.daily_data[ day ]:     # 리스트 접근 for 문
                
                # # print( self.daily_data[ day ] )    
                # print( idx )
                # break
                # 새영화가 있는지 탐색
                if idx['rankOldAndNew'] == 'NEW':
                    print( '새영화 발견, 메세지를 보냅니다.' )
                    return True                    
                    pass
                pass            # 리스트 접근 for 문 종료
            pass                # 딕셔너리 접근 for 문 종료
        return False
        pass # new_save 끝

    pass # BoxOffice 끝

# box_of = BoxOffice().main()

import asyncio
import telegram
# from workspace.cht_bot import BoxOffice  # 경로를 적절히 수정하세요

class ChtBot:
    def __init__(self) -> None:
        self.bot = telegram.Bot('')
        self.id = ''
        self.send_test_message()

    async def send_test_message(self):
        bot_token = ''
        chat_id = ''

        boxoffice = BoxOffice()
        boxoffice.kobis_connect()
        in_str = boxoffice.top10_print()

        bot = telegram.Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=in_str)

if __name__ == "__main__":
    try:
        import pymysql
        pymysql.connect(
            host='lee-001.ckuvmhr4e3ny.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='admin',
            password='siFzpOC6dgSWreIQO32n',
            database='test',
            charset='utf8mb4',
        )
        print('데이터베이스 접속 성공')
    except Exception as e:
        print(f'접속 실패: {e}')

    from datetime import datetime
    # open('./log', 'a').write(datetime.now().strftime('%Y-%m-%d %H:%M:%S 로그\n'))

    cht = ChtBot()
    asyncio.run(cht.send_test_message())



# import asyncio
# import telegram

# # from workspace.cht_bot import BoxOffice
# # import BoxOffice

# class cht_bot():
#     def __init__(self) -> None:
        
#         self.bot = telegram.Bot( '7057430361:AAFDR9s_hNFAj85B2XkdXhq_1dAkLwaCoeo' )
#         self.id = '7117704024'
        
#         self.bot.send_message( chat_id = id, text = '테스트' )
        
#         # 비동기 함수 실행
#         # asyncio.run(send_test_message())
#         return self
#         pass
        
#     async def send_test_message(  ):
#         bot_token = '7057430361:AAFDR9s_hNFAj85B2XkdXhq_1dAkLwaCoeo'
#         chat_id = '7117704024'

#         boxoffice = BoxOffice().kobis_connect()
#         in_str = boxoffice.top10_print()
#         # print( type( in_str ) )

#         bot = telegram.Bot(token=bot_token)
#         await bot.send_message(chat_id=chat_id, text=in_str )
#         return self
#     pass



# try:
#     pymysql.connect( 
#         host='lee-001.ckuvmhr4e3ny.ap-northeast-2.rds.amazonaws.com',
#         port = 3306,
#         user = 'admin',
#         password='siFzpOC6dgSWreIQO32n',
#         database = 'test',
#         charset='utf8mb4',
#      )
#     print( '데이터베이스 접속 성공' )
# except:
#     print( '접속실패' )

# from datetime import datetime
# # open('./log', 'a').write(datetime.now().strftime('%Y-%m-%d %H:%M:%S 로그\n'))

# cht = cht_bot()
# cht.asyncio.run(send_test_message())




""" 
crontad : 프로그램이 실행 될때만 돌려주는 프로그램
screen : 백그라운드에서 계속 돌려주는 프로그램

crontad 명령어
i -> insert 모드
esc -> 명령 모드
:wq, 

screen 명령어
컨트롤 + a, d
컨트롤 + d = 터미널 kill
screen -rD = 
컨트롤 + a, K
"""