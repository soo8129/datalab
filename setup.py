from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='UTF-16') as f:
    requirements = [line.strip() for line in f]

setup(
    name='datalab',
    version='0.1.0',
    author='soohyeok_kim',
    author_email='soohyeok_kim@tmax.co.kr',
    url='http://192.168.2.250:11088/fc/datalab_scraper',
    description='네이버 데이터랩 인기검색어 스크래퍼',
    long_description=open("README.md", "r", encoding="UTF-8").read(),
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'datalab = datalab_scraper.main:main'
        ]
    }
)