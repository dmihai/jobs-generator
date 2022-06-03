import config
import constants
from utils.Database import Database


db = Database()
db.connect(config.db_host, config.db_user, config.db_pass, config.db_name)

jobs = []
for asset in constants.assets:
    for year in constants.years:
        for timeframe in ['M5', 'M10']:
            jobs.append({
                "asset": asset,
                "year": year,
                "timeframe": timeframe,
                "params": ""
            })

db.insert_jobs('TestStrategy', 1, jobs)
