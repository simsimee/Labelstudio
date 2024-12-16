# Labelstudio

## OCR, 이미지, 비디오 레이블링 프로젝트

## 프로젝트 개요

이 프로젝트는 LabelStudio 오픈소스를 활용하여 OCR(광학 문자 인식), 이미지, 비디오 데이터에 대한 레이블링을 수행하는 것을 목표로 합니다. 또한 Hugging Face의 사전 훈련된 모델을 활용하여 오토레이블링 기능을 구현할 예정입니다.

## 주요 기능

1. **다양한 데이터 유형 지원**
   - OCR: 문서 이미지에서 텍스트 추출 및 레이블링
   - 이미지: 객체 감지, 분류, 세그멘테이션 등
   - 비디오: 객체 추적, 분류, 타임라인 세그멘테이션 등

2. **자동 레이블링**
   - Hugging Face 모델을 활용한 초기 레이블 생성
   - 사용자 검토 및 수정 기능

3. **유연한 레이블링 인터페이스**
   - 사용자 정의 가능한 레이블링 템플릿
   - 다양한 주석 도구 (바운딩 박스, 폴리곤, 키포인트 등)

## 기술 스택

- **LabelStudio**: 메인 레이블링 플랫폼
- **Python**: 백엔드 및 모델 통합
- **Hugging Face Transformers**: 사전 훈련된 모델 및 파이프라인
- **Docker**: 환경 일관성 및 배포 용이성

### 설치 방법

1. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

2. Label Studio 실행:
```bash
label-studio start
```

3. ML 백엔드 서버 실행:
```bash
python server.py
```

## Label Studio 프로젝트 설정

1. Label Studio 웹 인터페이스에서 새 프로젝트 생성
2. 다음 레이블링 설정을 사용:

```xml
<View>
  <Image name="image" value="$image"/>
  <TextArea name="transcription" toName="image" 
            editable="true" perRegion="false"
            required="true" maxSubmissions="1"/>
</View>
```

3. ML 백엔드 연결:
   - Settings > Machine Learning > Add Model
   - URL: http://localhost:9090
   - 연결 후 자동 레이블링 활성화 