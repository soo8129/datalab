from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='datalab',
    version='0.1.0',
    author='soohyeok_kim',
    author_email='soohyeok_kim@tmax.co.kr',
    url='http://192.168.2.250:11088/fc/datalab_scraper',
    description='네이버 데이터랩 인기검색어 스크래퍼',
    packages=find_packages(where='src', include=['datalab_scraper', 'datalab_scraper.*']),
    install_requires=requirements,
)