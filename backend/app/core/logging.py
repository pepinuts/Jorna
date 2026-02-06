import logging
import sys

def setup_logging(env: str) -> None:
    level = logging.DEBUG if env == "local" else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )
