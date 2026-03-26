"""Запуск API: хост, порт и reload читаются из `.env` (см. `.env.example`)."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

_FASTAPI_DIR = Path(__file__).resolve().parent


def _env_bool(key: str, default: bool) -> bool:
    raw = os.getenv(key)
    if raw is None or raw.strip() == "":
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")


def main() -> None:
    load_dotenv(_FASTAPI_DIR / ".env")
    os.chdir(_FASTAPI_DIR)

    host = os.getenv("API_HOST", "127.0.0.1").strip()
    port = int(os.getenv("API_PORT", "8000"))
    use_reload = _env_bool("API_RELOAD", True)

    import uvicorn

    uvicorn.run("main:app", host=host, port=port, reload=use_reload)


if __name__ == "__main__":
    main()
