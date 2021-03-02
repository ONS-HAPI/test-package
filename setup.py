from setuptools import find_packages
from setuptools import setup


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
   with open(file) as f:
        return f.read()
    
long_description = read_file("README.rst")
requires = read_requirements("requirements.txt")

docs_requires = [
    "sphinx>=2",
    ] + requires

test_requires = [
    "coverage",
    "pytest>=3.6,<4",
    "pytest-cov"
] + docs_requires

setup(
    name="testpackage",
    version="0.1.0",
    url="",
    license='MIT',
    author="",
    author_email="",
    description="A test package",
    packages=find_packages(exclude=('tests',)),
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "docs": docs_requires,
        "testing": test_requires
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Operating System  :: POSIX :: LINUX',
    ],
)
