from django.db import models
from .utils import open_file_with_mode, deleting_file

# Create your models here.
file_r = 'apps/file_methods/demo.txt'
file_a = 'apps/file_methods/demo_2.txt'
print("Open and read....", open_file_with_mode(file=file_r, mode='r'))

deleting_file(file=file_a)