# OpensourceProject_Team7

사용자 설명서:
실행에 앞서 app.py, storefunction.py, papagoAPI.py, myprog.sh, Tokenizer_ver1.py, WebCrawling_TIMES.py, static/, summarization/,  templates/ 파일들과 디렉터리들을 같은 위치에 둔다. myprog.sh 파일에 실행권한을 주고 파일을 실행시키면 로컬 웹페이지에 구현한 내용들이 모두 나타난다. 

주의점 : 요약본 해석은 네이버 파파고 open API를 사용하여 하루에 10000자 번역까지만 제공되고 있다. App.py 파일을 여러 번 실행하게 되어서 번역하는 글자 수가 10000자 이상 초과하게 되면 사이트에서 제한이 되어 번역 텍스트를 받아오지 않기 때문에 오류가 발생하여 웹페이지에 번역본이 나타나지 않는 경우가 발생할 수 있다.

파일 설명:
myprog.sh – 자동실행 쉘스크립트
app.py – 메인 실행 파일
papagoAPI.py – 파파고 API를 활용하여 데이터 번역
Tokenizer_ver1.py – 데이터 요약에 필요한 문장 분리
Storefunction.py – WebCrawling_TIMES.py 을 활용하여 TIMES의 분야별 데이터를 가져와서 요약하고 딕셔너리로 정리
WebCrawling_TIMES.py – 파라미터에 TIMES의 주제를 넘겨주면 그 카테고리의 상위 3개 뉴스 크롤링
static/ - 웹페이지 디자인에 필요한 css와 이미지 파일들이 존재
summarization/ - 자연어 처리 요약기능을 가진 파일들 존재
templates/ - 웹페이지를 구성하는 html파일들이 존재

시연 영상 유튜브 링크:
https://www.youtube.com/watch?v=glGjKIRos9Q
