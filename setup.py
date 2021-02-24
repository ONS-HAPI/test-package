from setuptools import find_packages
from setuptools import setup

setup(
    name="test-package",
    version="0.1.0",
    url="",
    license='MIT',
    author="",
    author_email="",
    description="A test package",
    packages=find_packages(exclude=('tests',)),
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',

    ],
)
