# Modernized setup.py for Python 3 and setuptools
import os
from setuptools import setup, find_packages

install_requires = [
	'pytest',
]

setup(
	name="guachi",
	version="0.0.6",
	packages=find_packages(),
	include_package_data=True,
	install_requires=install_requires,
	author="Alfredo Deza",
	author_email="alfredodeza@gmail.com",
	description="Global, persistent configurations as dictionaries",
	long_description_content_type="text/x-rst",
	long_description=open("README.rst").read() if os.path.exists("README.rst") else "",
	license="MIT",
	keywords="configuration management persistent dictionaries dictionary parse map mapping",
	url="https://github.com/sesme100/guachi",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Build Tools',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
	],
)
