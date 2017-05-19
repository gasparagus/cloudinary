import cloudinary
from cloudinary import uploader
import os


cloudinary.config(
  cloud_name = 'mdxvitals',  
  api_key = '211682179748443',  
  api_secret = 'six6YgE4by7NFFRNSM_DUJ7uTVY'  
)


#cloudinary.api.delete_resources_by_prefix('test_01242017/')

resource_list = []

cloudinary_folder = 'all_care_guides/'

count = 0

list_results_1 = cloudinary.api.resources(type='upload', prefix=cloudinary_folder, max_results=500)

if 'next_cursor' in list_results_1:

	next_cursor_1 = list_results_1['next_cursor']

	for ids in list_results_1['resources']:
		with open('list.txt','a') as f:
			f.write(ids['public_id']+'\n')
			resource_list.append(ids['public_id']+'\n')
			count += 1
			print count

	while True:
		list_results_1 = cloudinary.api.resources(type='upload', prefix=cloudinary_folder, max_results=500, next_cursor=list_results_1['next_cursor'])
		for ids in list_results_1['resources']:
			with open('list.txt','a') as f:
				f.write(ids['public_id']+'\n')
				resource_list.append(ids['public_id']+'\n')
				count += 1
				print count
else:

	list_results_1 = cloudinary.api.resources(type='upload', prefix=cloudinary_folder, max_results=500)

	for ids in list_results_1['resources']:
		with open('list.txt','a') as f:
			f.write(ids['public_id']+'\n')
		resource_list.append(ids['public_id']+'\n')
		count += 1
		print count
