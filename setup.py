from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hr_system/__init__.py
from hr_system import __version__ as version

setup(
	name="hr_system",
	version=version,
	description="HR SYSTEM",
	author="Ahmed Emam",
	author_email="ahmedemamhatem@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
