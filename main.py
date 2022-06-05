import json

import config
import constants
from utils.Database import Database


db = Database()
db.connect(config.db_host, config.db_user, config.db_pass, config.db_name)

version = 3

jobs = []
for asset in constants.common_assets:
    for year in constants.years:
        for timeframe in ['M5', 'M10']:
            params = {}
            jobs.append({
                "asset": asset,
                "year": year,
                "timeframe": timeframe,
                "params": json.dumps(params)
            })

db.insert_jobs('TestStrategy', version, jobs)
