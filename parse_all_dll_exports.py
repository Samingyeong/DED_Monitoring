import os
import subprocess
import pandas as pd
from openai import OpenAI

# 1. 설정
client = OpenAI(api_key="sk-...")  # OpenAI API 키 입력 (개인용 API Key 입력하면됨)
MODEL = "gpt-4o"
DUMPBIN_PATH = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.44.35207\bin\Hostx64\x64\dumpbin.exe"

DLL_FOLDER = r"F:\DED monitoring\DED"
TXT_FOLDER = r"F:\DED dll및ini파일 분석 자동화\DLL txt파일"
CSV_FOLDER = r"F:\DED dll및ini파일 분석 자동화\DLL csv파일"
COMMENTED_TXT_FOLDER = r"F:\DED dll및ini파일 분석 자동화\DLL 주석txt파일"
os.makedirs(TXT_FOLDER, exist_ok=True)
os.makedirs(CSV_FOLDER, exist_ok=True)
os.makedirs(COMMENTED_TXT_FOLDER, exist_ok=True)


def convert_dll_to_txt(dll_path, txt_path):
    result = subprocess.run(
        [DUMPBIN_PATH, "/exports", dll_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=False
    )
    if result.returncode == 0:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(result.stdout)
        print(f"[✓] {os.path.basename(dll_path)} → TXT 저장 완료")
        return True
    else:
        print(f"[X] dumpbin 실패: {dll_path}")
        return False


def extract_functions_from_txt(txt_path):
    functions = []
    with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 4 and parts[0].isdigit():
                functions.append(parts[-1])
    return functions


def analyze_functions_with_llm(functions):
    prompt = (
        "다음은 DLL에서 추출한 export 함수 목록입니다.\n"
        "각 함수의 기능이나 용도를 한국어로 간단히 설명해 주세요.\n"
        "출력 형식은 '함수명: 설명' 으로 해주세요.\n\n"
        + "\n".join(functions[:100])
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


def save_analysis_to_csv_and_txt(dll_name, functions, llm_result):
    rows = []
    comment_dict = {}

    for line in llm_result.splitlines():
        if ":" in line:
            func, desc = line.split(":", 1)
            func = func.strip()
            desc = desc.strip()
            rows.append({"함수명": func, "설명": desc})
            comment_dict[func] = desc

    # CSV 저장
    df = pd.DataFrame(rows)
    csv_path = os.path.join(CSV_FOLDER, f"{dll_name}.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    # TXT 저장 (주석 포함)
    txt_path = os.path.join(COMMENTED_TXT_FOLDER, f"{dll_name}_commented.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        for func in functions:
            comment = comment_dict.get(func, "")
            f.write(f"{func}  // {comment}\n")

    print(f"[✓] {dll_name}.csv 및 주석txt 저장 완료 ({len(df)}개 함수)")


def main():
    for file in os.listdir(DLL_FOLDER):
        if file.endswith(".dll"):
            dll_path = os.path.join(DLL_FOLDER, file)
            dll_name = os.path.splitext(file)[0]
            txt_path = os.path.join(TXT_FOLDER, dll_name + ".txt")

            if not convert_dll_to_txt(dll_path, txt_path):
                continue

            functions = extract_functions_from_txt(txt_path)
            if not functions:
                print(f"[!] {dll_name}: 함수 없음 또는 추출 실패")
                continue

            print(f"[•] {dll_name} 분석 중... ({len(functions)}개 함수)")
            try:
                llm_result = analyze_functions_with_llm(functions)
                save_analysis_to_csv_and_txt(dll_name, functions, llm_result)
            except Exception as e:
                print(f"[X] {dll_name} 분석 실패: {e}")


if __name__ == "__main__":
    main()
