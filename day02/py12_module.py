# py12_module.py - 모듈/패키지지

import py10_function as calc

calc.multi(10, 4)

#  수학 함수를 편하게 모아둔 모듈듈
import math

Result = math.pow(2, 10)
print(Result)

Result = math.log2(4)
print(Result)

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests

import requests

res = requests.get('https://www.naver.com') # 네이버 사이트를 접속하라
print(res.status_code) #200

print(res.content)