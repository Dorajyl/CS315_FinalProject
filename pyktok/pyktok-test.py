import json
import pyktok as pyk

with open('tiktok_history_sample.json') as fin:
	data = json.load(fin)

urls = [entry['Link'] for entry in data]

pyk.specify_browser('chrome')

pyk.save_tiktok_multi_urls(urls, False, # save video file
                		   'tiktok_data.csv',
                		    5)