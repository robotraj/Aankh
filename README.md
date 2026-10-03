# SafeView AI Prototype

Phase 1 prototype: webcam in, faces blurred by default, blurred-only recording out.

Specs and company context live in the Obsidian vault (`Downloads/Aaakh`):
`projects/safeview-ai/prototype-spec.md` (written by task 003) and `company/mission.md`.

## Design rules
- Blur by default; only a confident match is shown (matching not implemented yet).
- Blur before encode; raw frames are never written to disk.
- Everything runs locally.
- Use only synthetic or consented test footage. No real children's data.

## Setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPATH=src
python -m safeview.demo
```
Press `q` to quit, `r` to toggle recording (blurred output only, saved to `recordings/`).

## Status
Stage 0: detect faces and blur ALL of them (the "strict mode" baseline). Next: tracking, enrolment and matching, per task 002/003.
