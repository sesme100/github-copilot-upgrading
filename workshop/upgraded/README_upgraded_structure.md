# 업그레이디드 폴더 파일 구조 설명

이 문서는 `/workspaces/github-copilot-upgrading/workshop/upgraded/` 폴더 내의 파일 및 디렉터리 구조를 설명합니다. 이 구조는 `legacy` 폴더의 내용을 그대로 복사한 것입니다.

## 최상위 파일 및 폴더
- `MANIFEST.in` : 패키징 관련 설정 파일
- `README.rst` : 프로젝트 설명 파일
- `distribute-0.6.10.tar.gz` : 배포 관련 압축 파일
- `distribute_setup.py` : 배포 스크립트
- `setup.py` : 파이썬 패키지 설정 파일
- `docs/` : 문서 관련 디렉터리
- `guachi/` : 주요 파이썬 소스 코드 및 테스트 디렉터리
- `guachi.egg-info/` : 패키지 메타데이터 정보 디렉터리

## docs/
- `build/` : 빌드된 문서 파일
  - `doctrees/` : Sphinx 문서 트리 파일
  - `html/` : HTML 문서 및 정적 파일
- `source/` : Sphinx 문서 소스
  - `_static/` : 정적 파일(css 등)
  - 여러 rst, py 파일

## guachi/
- `__init__.py`, `config.py`, `database.py` : 파이썬 모듈 파일
- `tests/` : 테스트 코드

## guachi.egg-info/
- 패키지 메타데이터 파일들

---

이 구조는 레거시(legacy) 폴더의 구조와 동일하게 업그레이디드(upgraded) 폴더에 복사된 것입니다. 각 파일의 실제 내용은 필요에 따라 채워질 수 있습니다.
