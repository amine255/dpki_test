# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 02:20:36 2016

@author: Amine
"""
"""
import csv
from deepki import settings

def write_to_csv(item):
    writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
    writer.writerow(item[key] for key in item.keys())

class WriteToCsv(object):
    def process_item(self, item, spider):
        write_to_csv(item)
        return item      
    
"""