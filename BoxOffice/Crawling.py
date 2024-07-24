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

        pass # 생성자 끝

    def url_connect( self, URL, headers = {}, data = [] ) -> int:
        """
        URL : str, 접속할 사이트주소
        reutnr : int, respoonse 상태를 알려준다.
        """

        # 사이트에 요청
        self.respoonse = requests.get( URL, headers, data )
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