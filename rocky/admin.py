from django.contrib import admin
import logging

logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_hanlder = logging.FileHandler(filename='myDjango.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_hanlder.setFormatter(formatter)
logger = logging.getLogger("Main")
logger.addHandler(file_hanlder)

# Register your models here.
