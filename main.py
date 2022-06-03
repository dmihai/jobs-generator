import json

import config
import constants
from utils.Database import Database


db = Database()
db.connect(config.db_host, config.db_user, config.db_pass, config.db_name)

costs = db.get_trading_costs()

jobs = []
for asset in constants.all_assets:
    cost = costs.get(asset, constants.default_trading_cost)
    for year in constants.years:
        for timeframe in ['M5', 'M10']:
            params = {
                "trading_cost": cost
            }
            jobs.append({
                "asset": asset,
                "year": year,
                "timeframe": timeframe,
                "params": json.dumps(params)
            })

# db.insert_jobs('TestStrategy', 1, jobs)
