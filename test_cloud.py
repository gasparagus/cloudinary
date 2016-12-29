import cloudinary
from cloudinary import uploader
import os


cloudinary.config(
  cloud_name = 'gary',  
  api_key = '',  
  api_secret = ''  
)

count = 0

path = 'C:/Users/glombardo/Desktop/to_delete/'

for i in os.listdir('C:/Users/glombardo/Desktop/to_delete'):
	cloudinary.uploader.upload(path+i)
	count += 1

print 'You\'ve uploaded', count, 'images!'