from setuptools import setup, find_packages

setup(
name="rocky-django",
version="1.0.0-RC01-SNAPSHOT",
author="copervan",
author_email="copervan@163.com",
description="rocky-django sdk",
platforms='windows',
# 找到所有包含__init__的包
packages=find_packages(),
# 静态文件等，配合MANIFEST.in (package_data 参数不太好使)
include_package_data=False,
# 单独的一些py脚本,不是在某些模块中
scripts=["manage.py"],
install_requires=['django==1.8.18'],
# 此项需要，否则卸载时报windows error
zip_safe=False
)
