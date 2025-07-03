@echo off
:: Visual Studio 2022 환경 변수 설정
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

:: 분석할 Python 스크립트 경로로 이동
cd /d "F:\DED dll및ini파일 분석 자동화"

:: Python 스크립트 실행
"C:\Program Files\Python312\python.exe" parse_all_dll_exports.py

:: 콘솔 유지
echo.
echo ------------------------------------------------
echo ? 분석이 완료되었습니다. 결과를 확인하세요.
echo ? 이 창을 닫으시려면 아무 키나 누르세요.
pause > nul
