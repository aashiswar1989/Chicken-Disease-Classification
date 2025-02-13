import os
import sys
import logging
from pathlib import Path

logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

log_dir = Path('logs')
log_filepath = log_dir/'running_logs.log'

if not log_dir.is_dir():
    log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('CNNClassifierLogger')