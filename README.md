# DED DLL Function Analyzer

이 프로젝트는 `dumpbin`으로 추출한 DED 장비용 DLL 파일의 export 함수 목록을 분석하고, GPT-4o 또는 로컬 LLM을 사용해 각 함수의 기능을 자동으로 설명하여 `.csv` 파일로 저장하는 자동화 스크립트입니다.

---

## 프로젝트 구조

DED dll및ini파일 분석 자동화/
├── DLL txt파일/ ← dumpbin 결과 .txt 파일 모음
├── DLL csv파일/ ← 분석 결과 저장 폴더
├── parse_all_dll_exports.py ← 메인 자동화 스크립트
└── README.md

yaml
코드 복사

---

## 주요 기능

- DLL export 함수 목록 `.txt`에서 함수명 자동 추출
- GPT-4o 또는 로컬 LLM을 사용하여 함수 기능 설명
- 결과를 `.csv`로 저장

---

## 사용 방법

### 1. 의존성 설치

```bash
pip install openai pandas
2. 폴더 구성
DLL txt파일/ 폴더에 dumpbin /exports 결과로 생성된 .txt 파일들을 넣습니다.

DLL csv파일/ 폴더는 스크립트 실행 시 자동 생성됩니다.

3. API 키 설정
parse_all_dll_exports.py 파일 내에서 OpenAI API 키를 설정합니다.

python
코드 복사
client = OpenAI(api_key="sk-...")
🔐 보안 팁: API 키는 코드에 직접 입력하지 말고 .env 파일이나 환경변수로 관리하는 것을 권장합니다.

4. 실행
bash
코드 복사
python parse_all_dll_exports.py

📌 예시 결과
cs
코드 복사
함수명,설명
HX_StartMotion, 장비의 모션을 시작하는 함수
HX_StopMotion, 장비의 모션을 정지시키는 함수
HX_SetSpeed, 장비의 이동 속도를 설정하는 함수
...