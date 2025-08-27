# HBU Monitoring System

DED(Direct Energy Deposition) 공정을 위한 실시간 모니터링 시스템입니다.

## 🚀 주요 기능

- **실시간 센서 모니터링**: NIR 카메라, 파이로미터, 레이저 시스템, CNC 컨트롤러
- **DED 로그 모니터링**: 공정 시작/종료 이벤트 자동 감지
- **데이터 시각화**: 실시간 그래프 및 상태 표시
- **자동 데이터 저장**: CSV 파일로 센서 데이터 및 공정 이벤트 저장

## 📦 설치

```bash
# 저장소 클론
git clone https://github.com/your-username/HBU-monitoring.git
cd HBU-monitoring

# 가상환경 생성
python -m venv venv
venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

## 🎯 사용법

```bash
# 일반 실행
python main.py

# 테스트 모드 (랜덤 데이터)
python main.py --testmode
```

1. 프로그램 실행
2. 센서 연결 상태 확인
3. "시작" 버튼으로 모니터링 시작
4. 실시간 데이터 확인 및 저장

## 📁 프로젝트 구조

```
HBU_monitoring/
├── main.py              # 메인 프로그램
├── Sensors/             # 센서 통신 모듈
├── UI/                  # 사용자 인터페이스
├── config/              # 설정 파일
├── DB/                  # 데이터 저장소
└── requirements.txt     # Python 의존성
```

## ⚙️ 설정

센서별 설정 파일을 `config/` 폴더에서 수정

## 📊 데이터 형식

### 센서 데이터
```csv
time,curpos_x,curpos_y,curpos_z,curpos_a,curpos_c,mpt,melt_pool_area,outpower,process_status
2025-08-18 15:59:58.477,-137.52,-160.48,-64.37,0.0,0.0,699.9,1250.5,0.0,running
```

### 공정 이벤트
```csv
timestamp,datetime,event,message,raw_line
2025-08-25,13:27:52.30,process_start,NC_CS5AXIS;IsRunning;True,...
```

## 🔧 요구사항

- **OS**: Windows 10/11
- **Python**: 3.7+
- **DED System**: C:/DED/ 경로에 설치
- **메모리**: 4GB RAM 이상

---

**HBU Monitoring System** - DED 공정 모니터링 솔루션
