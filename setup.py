from setuptools import setup

REQUIRES = [
    "requests",
    "allure-pytest",
    "pydantic",
]

setup(
    name='dm_api_account',
    version='0.0.2',
    packages=['dm_api_account'],
    url='https://github.com/vladgerasimov94/dm_api_account.git',
    license='MIT',
    author='Vladislav Gerasimov',
    author_email='-',
    install_requires=REQUIRES,
    description='dm api account with response models'
)
