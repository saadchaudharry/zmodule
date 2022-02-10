from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zmodule/__init__.py
from zmodule import __version__ as version

setup(
	name="zmodule",
	version=version,
	description="saad",
	author="saaad",
	author_email="saadchauhdary646@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
