import cloudinary
from cloudinary import uploader
import os


cloudinary.config(
  cloud_name = '',  
  api_key = '',  
  api_secret = ''  
)

resource_list = []

cloudinary_folder = 'test/'

count = 0

list_results_1 = cloudinary.api.resources(type='upload', prefix=cloudinary_folder, max_results=500)

# If the folder has more than 500 images (max value from API), it will return a 'next_cursor' key. The code will then run until complete.
if 'next_cursor' in list_results_1:

	next_cursor_1 = list_results_1['next_cursor']

	for ids in list_results_1['resources']:
		with open('list.txt','a') as f:
			f.write(ids['public_id']+'\n')
			resource_list.append(ids['public_id']+'\n')
			count += 1
			print count

# Try to scan a folder with over 500 but not much over to see if it breaks.
	while True:
		try:
			list_results_1 = cloudinary.api.resources(type='upload', prefix=cloudinary_folder, max_results=500, next_cursor=list_results_1['next_cursor'])
			for ids in list_results_1['resources']:
				with open('list.txt','a') as f:
					f.write(ids['public_id']+'\n')
					resource_list.append(ids['public_id']+'\n')
					count += 1
					print count
		except: break
# IF folder has less than 500 images, no next_cursor key is returned. Therefore the API will not include the next_cursor kwarg.
else:

	list_results_1 = cloudinary.api.resources(type='upload', prefix=cloudinary_folder, max_results=500)

	for ids in list_results_1['resources']:
		with open('list.txt','a') as f:
			f.write(ids['public_id']+'\n')
		resource_list.append(ids['public_id']+'\n')
		count += 1
		print count
