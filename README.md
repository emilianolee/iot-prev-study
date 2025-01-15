# iot-prev-study-2025
2025 IOT 개발자과정 선행학습

## 1일차
기본 과정 설명 및 개발환경 설정, 파이썬 기본학습

### 과정소개

### 개발환경 설치

#### 깃허브 사용법
- 리모트 리포지토리 생성
- 깃허브데스크톱으로 로컬 리포지토리로 클로닝
- 로컬에서 작성 후 커밋(**Commit**)후
- 리모트로 푸시(**Push**)
- 다른 사용자가 리모트에 있는 최신 내용을 풀(`Pull`)

### 마크다운 학습

#### 마크다운이란?
- Markdown은 웹페이지에 리포팅을 하기 위한 마크업 언어
    - 주요사용처 - 위키피디아, 나무위키, 깃허브, 주피터노 등...
    - 문법이 간단하고 쉽게 배울 수 있음
    - 표준이 없는 단점

1.  번호목록
    1. 첫번째 목록
    2. 두번째 목록
        1. 두번째 하위 목록 1
        2. 두번째 하위 목록 2
        - 일반 목록

##### 기본 문법(제목 5)
- 링크 사용법
[네이버](https://www.naver.com)

- 이미지 사용법
![환수사](https://ssl.pstatic.net/melona/libs/1522/1522020/aa5b48b7e7f7e1e6d44c_20250109174152630.jpg)

- HTML 이미지 방법(이미지 크기 조정)
<img src="https://ssl.pstatic.net/melona/libs/1522/1522020/aa5b48b7e7f7e1e6d44c_20250109174152630.jpg" width="300">

###### 추가사항(제목 6)
추가사항입니다

### 파이썬 학습

#### 파이썬 이란?
- 귀도 반 로썸이 1990년경에 개발한 초간단! 인터프리터 프로그래밍 언어

##### 파이썬 특징
- 컴파일러언어(exe 실행파일이 생성되는 언어)가 아닌 .py 파일로 바로 실행할 수 있는 인터프리터 언어
- 객체지향언어(Object Oriented Program)
- 아주 쉬운 언어(진입장벽 낮음)
- 프로그래머가 아닌 과학자들도 쉽게 프로그램개발에 진입
- https://www.tiobe.com/tiobe-index/ 에서 2020년 이후 1위 고수
- 빅데이터분석, 인공지능, 웹개발(!) 등 다양한 분야 활용

##### 파이썬 설치
- Install Now로 설치하면 안됨! Costmoize installation으로 설치
- Add Python.exe to Path 는 체크
- 경로 변경
- 설치 후 Disable MAX Langs PATH... 체크 필수
- 설치 확인
    - cmd(명령프롬프트) 또는 powershell 실행 후 python 입력

- VS Code 확장 > Python 검색색
- 확장자 .py(thon)
- 탐색기 > day01 폴더 생성
- py01_first.py 파일 생성

## 2일차
- 파이썬 기본 문법

### 문법학습 순서
1. 변수
2. 데이터 타입
    - 파이썬에서는 입력 수의 크기에 제약이 없다
3. 입출력 - 파일입출력 포함함
    - 한국어만(ANSI/EUC-KR)와 국제어통용(UTF-8) 인코딩 주의!
4. 연산자
5. 흐름제어
    1. if문
        - 단일 if, if - else, if - elif - else
    2. for문 - 프로그래밍 꽃
    3. while문 - for문과 동일
6. 함수
7. 객체지향, 클래스 - 패스!
8. 모듈, 패키지
9. 예외처리
10. 디버깅
