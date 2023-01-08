# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import csv, os
import datetime as dt
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parent.parent
FIELDNAMES = ["Статус", "Количество"]
results = defaultdict(int)



class PepParsePipeline:

    item_count = 0

    def open_spider(self, spider):
        PepParsePipeline.item_count = 0

    def process_item(self, item, spider):
        PepParsePipeline.item_count += 1
        results[item["status"]] += 1
        return item

    def close_spider(self, spider):
        global item_count
        results["Total"] = PepParsePipeline.item_count
        now_time = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f'status_summary_{now_time}.csv'
        filename = os.path.join(BASE_DIR, 'results', filename)
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()
            for key, value in results.items():
                writer.writerow({FIELDNAMES[0]: key, FIELDNAMES[1]: value})
