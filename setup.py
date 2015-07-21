try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description':'Database Implementation',
	'author':'Ismail Elouafiq',
	'url':'https://github.com/nidhog/deebee',
	'download_url':'https://github.com/nidhog/deebee/archive/deebee.zip',
	'author_email':'i.elouafiq@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['deebee'],
	'scripts':[],
	'name':'DeeBee'
}

setup(**config)