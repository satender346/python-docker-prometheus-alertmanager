from setuptools import setup

setup(
    name='monitoring_scripts',
    version='1.0',
    packages=['monitoring_scripts'],
    author='Satender Yadav',
    author_email='satender346@gmail.com',
    description='Script to monitor application and send alerts to email',
    install_requires=['prometheus_client', 'requests']
)
