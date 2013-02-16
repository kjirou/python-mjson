import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup (
    name='mjson',
    version='0.2',
    description='Extended "python -mjson.tool"',
    long_description=read_file('README.txt'),
    author='kjirou',
    author_email='sorenariblog@gmail.com',
    url='http://blog.kjirou.net/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    keywords=['json', 'tool', 'command'],
    license='MIT License',
)
