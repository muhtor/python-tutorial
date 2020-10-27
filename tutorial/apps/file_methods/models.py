from django.db import models
from .utils import open_file_with_mode, deleting_file, write_json

# Create your models here.
file_r = 'apps/file_methods/demo.txt'
file_a = 'apps/file_methods/demo_2.txt'
# print("Open and read....", open_file_with_mode(file=file_r, mode='r'))

# deleting_file(file=file_a)


payload = {
  "access_token": "Some-TOKEN-@@@333444",
  "expires_in": 7200,
  "token_type": "Application Access Token"
}
file_json = 'apps/file_methods/auth_data'

write_json(file=file_json, payload=payload)
