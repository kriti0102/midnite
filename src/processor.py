import pandas as pd
import logging
import os
import shutil
from db import insert_bets

REQUIRED_COLUMNS = [
    'id', 'user_id', 'bet_outcome_id', 'game_id', 'wager', 'is_cash_wager',
    'winnings', 'created_at', 'settled_at'
]

PROCESSED_DIR = "/opt/src/processed"
FAILED_DIR = "/opt/src/failed"

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(FAILED_DIR, exist_ok=True)

def process_bet_file(filepath):
    try:
        df = pd.read_csv(filepath)

        if not all(col in df.columns for col in REQUIRED_COLUMNS):
            raise ValueError("Missing required columns in CSV")

        logging.info(f"📥 Found file: {filepath}")
        logging.info(f"📊 Inserting {len(df)} bets into raw.bet...")
        insert_bets(df)
        logging.info(f"✅ Successfully inserted bets from {filepath}")

        dest_path = os.path.join(PROCESSED_DIR, os.path.basename(filepath))
        shutil.move(filepath, dest_path)
        logging.info(f"📁 Moved to processed/: {dest_path}")

    except Exception as e:
        logging.exception(f"❌ Failed to process {filepath}")
        dest_path = os.path.join(FAILED_DIR, os.path.basename(filepath))
        shutil.move(filepath, dest_path)
        logging.info(f"📁 Moved to failed/: {dest_path}")

    # Always log this, no matter success or failure
    logging.info("🔄 Looking for new files...")
