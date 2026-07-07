# 로또 추첨기 (MVP)

간단한 웹 기반 로또 번호 생성기입니다. 이 저장소에는 다음 파일이 포함되어 있습니다:

- `lotto.html` — 웹 UI: 번호 생성, 보너스 포함, 결과 저장/불러오기, 내 번호 비교 기능
- `lotto.py` — 간단한 커맨드라인 기반 로또 생성기
- `DESIGN.md` — 디자인 토큰과 스타일 가이드

사용 방법

1. `lotto.html` 열기 (로컬 파일로 더블클릭하거나 로컬 서버 사용):

```powershell
start lotto.html
```

또는 로컬 서버로 서빙:

```bash
python -m http.server 8000
# 브라우저에서 http://localhost:8000/lotto.html 열기
```

2. UI 설명
- `추첨 횟수`: 생성할 회수
- `보너스 포함`: 보너스 번호 포함 여부
- `생성`: 추첨 실행
- `내 번호 비교`: 6개 번호 입력 후 `비교` 버튼으로 매칭 확인
- `내보내기`: 현재 결과를 JSON으로 저장
- `불러오기`: 저장한 JSON 파일 불러오기

3. `lotto.py` 예제

```bash
python lotto.py -n 5 -b
# 5회 추첨, 보너스 포함
```

4. 역대 당첨번호 표시

- 저장소 루트에 `history.json`을 위치시키면 `lotto.html`이 자동으로 불러와 표시합니다.
- 또는 제공한 `fetch_history.py` 스크립트를 사용해 최신 데이터를 내려받아 `history.json`을 생성할 수 있습니다:

```bash
pip install requests
python fetch_history.py --start 1 --end 0 --out history.json
# --end 0 은 마지막 회차까지 자동으로 가져옵니다 (인터넷 연결 필요)
```

저작권 및 라이선스

원하시면 LICENSE 파일을 추가해 드립니다.
