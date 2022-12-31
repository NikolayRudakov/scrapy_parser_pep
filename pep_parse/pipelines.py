# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import csv
import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
results = {}
item_count = 0


class PepParsePipeline:
    def open_spider(self, spider):
        global item_count
        item_count = 0

    def process_item(self, item, spider):
        global item_count
        item_count += 1
        if item["status"] not in results.keys():
            results[item["status"]] = 1
        else:
            results[item["status"]] += 1
        return item

    def close_spider(self, spider):
        global item_count
        results["Total"] = item_count
        # Не проходит проверку на W504 и W503 одновременно
        # filename = (
        #    str(BASE_DIR)
        #     + "/results/status_summary_"
        #     + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        #     + ".csv"
        # )
        filename = str(BASE_DIR) + "/results/status_summary_"
        filename = filename+ dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = filename + ".csv"

        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Статус", "Количество"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for key, value in results.items():
                writer.writerow({"Статус": key, "Количество": value})
