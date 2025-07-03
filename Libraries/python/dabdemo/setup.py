# Filename: setup.py
from setuptools import setup, find_packages

import dabdemo

setup(
  name = "dabdemo",
  version = dabdemo.__version__,
  author = dabdemo.__author__,
  url = "https://demorz1@dev.azure.com/demorz1/databricks%20cicd/_git/databricks%20cicd",
  author_email = "daizhang@microsoft.com",
  description = "democicd",
  packages = find_packages(include = ["dabdemo"]),
  entry_points={"group_1": "run=dabdemo.__main__:main"},
  install_requires = ["setuptools"]
)