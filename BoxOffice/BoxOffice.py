# 정의
# 부모 정의
from BoxOffice.Crawling import Crawling

# 클레스 내 필요한거
import datetime as dt
import json
import sys

# 커스텀 클레스 정의
# 환경변수 등록
sys.path.append( r'C:\Users\SDA12\Desktop\AiWork' )

# 커스텀 모둘 업핸드
from De_to_En.EntoDe_code import EntoDe_code

class BoxOffice( Crawling ):

    def __init__(self) -> None:
        # 부모 생성자 호출
        super().__init__()

        # 속성 정의
        # self.js_data
        self.daily_data = {}
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

    def new_save( self ):
        """
        새 영화가 있으면 영화를 저장 하고 아니면 저장 하지 않는다.
        """
        # 새로운 영화 있는지 탐색
        for day in self.daily_data:  # 딕셔너리 접근 for 문
            for idx in self.daily_data[ day ]:     # 리스트 접근 for 문
                
                # # print( self.daily_data[ day ] )    
                # print( idx )
                # break
                # 새영화가 있는지 탐색
                if idx['rankOldAndNew'] == 'NEW':
                    print( '새영화 발견, 데이터를 저장 합니다.' )
                    # 저장된 파일을 가져온다
                    f = open( 'BoxOffice/BoxOffice.sav', 'r' )
                    # 가져온 데이터를 json 형식으로 불러온다
                    load_json = json.load( f )
                    f.close()   # 파일 닫기
                    
                    # 새로 받은 데이터에서 키값을 추출
                    # 어느 순서가 되었든 마지막 것만 가져온다
                    li_key = list( self.daily_data.keys() )[-1]  
                    # 기존 데이터에 업데이트 되는 데이터를 추가한다.
                    load_json[ li_key ] = self.daily_data[ li_key ] 
                    
                    # 파일을 불러오기
                    f = open( 'BoxOffice/BoxOffice.sav', 'w' )
                    json.dump( load_json, f )   # 기존 데이터에 새 데이터 덮어쓰기
                    f.close()   # 파일 닫기

                    # break   # 새영화가 있는지 탐색을 끝내고 모든 반복문 종료
                    pass
                pass            # 리스트 접근 for 문 종료
            pass                # 딕셔너리 접근 for 문 종료
        pass # new_save 끝

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

    def main( self ):

        self.kobis_connect()

        self.top10_print()

        # self.new_save()

        pass # main 끝

    pass # BoxOffice 끝

# box_of = BoxOffice().main()

