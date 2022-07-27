import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='algodocs',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/algodocs/algodocs-python',
    license='MIT',
    author='Ibrahim Nalbant',
    author_email='support@algodocs.com',
    description='A python client for the AlgoDocs API',
    long_description=README,
    install_requires=["requests>=2.24.0"],
    keywords=["AlgoDocs", "API"],
    long_description_content_type="text/markdown"
)
