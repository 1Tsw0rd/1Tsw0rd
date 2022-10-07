import requests
from bs4 import BeautifulSoup

#1)html 가져오기
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#숙제 - 순위, 노래제목, 가수명

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
     #순위
     rank = song.select_one('td.number').text[0:2].strip() #문자열 자르기 [시작위치:끝위치], 0번째에서 2번째까지 출력

     #노래 제목 - 저스틴비버 노래제목에 19금 아이콘 있어서, 아이콘 안에 글자까지 추출
     # body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
     # body-content > div.newest-list > div > table > tbody > tr:nth-child(15) > td.info > a.title.ellipsis > span

     #icon 문구 추출
     span_element = song.select_one('td.info > a.title.ellipsis').find('span')
     icon = '';
     if span_element is not None:
          for span in span_element:
               for s in span:
                  icon += s
     #print(icon)

     # icon span 제거
     title = song.select_one('td.info > a.title.ellipsis')
     span_elements = title.find_all("span")
     for span in span_elements:
          span.extract()

     #icon span 문구 + title 문구
     title = icon + title.text.strip()

     #가수
     singer = song.select_one('td.info > a.artist.ellipsis').text.strip()
     print(rank, title, singer)

#extract() 제거된 태그 리턴
#strip() 양쪽공백제거 / lstrip() 왼쪽 공백 제거 / rstrip ()오른쪽 공백 제거 / strip('a') 하면 a자 제거

# 20221007 09:33 센터에서
#
# 파이썬 듣기만 들었지 이렇게 크롤링하는 프로그램까지 만든 적이 없는데
#
# 너무 재밌었다
#
# 다른 사이트에 있는 정보를 내가 만든 프로그램으로 긁어오다니!!
#
# 다른 사람들이 만든 크롤링 프로그램만 보았는데
# 직접 만들다니!! 해보고 싶은게 많이 생길 것 같다!!
#
# 그리고 RDBMS만 알던 내가 직접 noSQL인 몽고DB까지 해보다니!!!
# 정말 IT는 재밌는거 투성이다!!
#
# 화이팅 하자!!
