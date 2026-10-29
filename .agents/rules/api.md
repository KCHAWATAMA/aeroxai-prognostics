---
trigger: glob
globs: api/**/*.py
description: Rules for the FastAPI service
---

# API rules

- Every request and response has a Pydantic model; no bare dicts.
- Routes go in `api/routes/`, logic in `api/services/`; `api/main.py` only wires them together.
- Read config through `api.settings.get_settings()`; never call `os.getenv` elsewhere.
- CSV uploads: 2 MB limit, schema-validated, processed in memory, never written to disk.
- The Gemini assistant receives only computed numbers for one engine; its key comes from Secret Manager.
- Every route has a test using `fastapi.testclient.TestClient`.
