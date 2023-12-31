from setuptools import setup, find_packages

REQUIRES = [
    "requests",
    "allure-pytest",
    "pydantic",
]

setup(
    name='dm_api_account',
    version='0.0.3',
    packages=find_packages(),
    url='https://github.com/vladgerasimov94/dm_api_account.git',
    license='MIT',
    author='Vladislav Gerasimov',
    author_email='-',
    install_requires=REQUIRES,
    description='dm api account with response models'
)
