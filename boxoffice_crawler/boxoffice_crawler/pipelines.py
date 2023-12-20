# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class BoxofficeCrawlerPipeline:

    def __init__(self):
        self.csvwriter = csv.writer(
            open("boxoffice_1990_2022.csv", "w", newline=''))
        self.csvwriter.writerow(["title", "domestic_revenue", "world_revenue", "distributor",
                                "opening_revenue", "opening_theaters", "budget", "MPAA", "genres", "in_release","release_date"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["domestic_revenue"])
        row.append(item["world_revenue"])
        row.append(item["distributor"])
        row.append(item["opening_revenue"])
        row.append(item["opening_theaters"])
        row.append(item["budget"])
        row.append(item["MPAA"])
        row.append(item["genres"])
        row.append(item["in_release"])
        row.append(item["release_date"])
        self.csvwriter.writerow(row)
        return item
