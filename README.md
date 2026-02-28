# DABEL5 — Private Workspace

한국어 초안 집필, 레퍼런스 노트, 유틸 스크립트를 관리하는 비공개 작업 리포.

웹사이트 코드(Hugo, Terraform 등)는 [dabel5-org](https://github.com/park-jun-woo/dabel5-org)에서 관리한다.

## 워크플로

```
notes/ → workspace/post{NNN}-{slug}.md → draft/{slug}.md → (dabel5-org) content/
```

| 디렉토리 | 용도 |
|----------|------|
| `notes/` | 리서치, 계산, 아이디어 메모 |
| `workspace/` | 한국어 초안 (`post{NNN}-{slug}.md`) |
| `draft/` | 편집 완료 한국어 원고 (`{slug}.md`) |
| `scripts/` | 유틸 스크립트 |

## 관련 리포

| 리포 | 용도 |
|------|------|
| [dabel5-org](https://github.com/park-jun-woo/dabel5-org) | dabel5.org 웹사이트 (Hugo, 다국어 콘텐츠, Terraform) |
| dabel5 (이 리포) | 비공개 작업 파일 |
