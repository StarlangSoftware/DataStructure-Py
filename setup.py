from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-DataStructure',
    version='1.0.10',
    packages=['DataStructure', 'DataStructure.Cache'],
    url='https://github.com/StarlangSoftware/DataStructure-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Simple Data Structures Library',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
