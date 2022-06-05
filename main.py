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
        for timeframe in ["M5"]:
            for start_offset in [3, 2, 1]:
                for stop_offset in [3, 2, 1]:
                    params = {
                        "start_offset": start_offset,
                        "stop_offset": stop_offset
                    }
                    jobs.append({
                        "asset": asset,
                        "year": year,
                        "timeframe": timeframe,
                        "params": json.dumps(params)
                    })

db.insert_jobs('TestStrategy', version, jobs)
