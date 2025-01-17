from setuptools import setup, Extension
import os

os.environ["CC"] = "gcc"
os.environ["CXX"] = "g++"

setup(
    name='rdrand',
    version='1.5.0',
    description="Python interface to Intel hardware rng",
    long_description= "".join(open('rdrandom.rst').readlines()),
    author="Chris Stillson",
    author_email="stillson@gmail.com",
    url='https://github.com/stillson/rdrand',
    license="New BSD license",
    ext_modules=[Extension('_rdrand', ['rdrand.c'])],
    py_modules = ['rdrand'],
    keywords = ['rdrand', 'rdseed', "intel","hardware","random","number","generator","rng"],
    data_files=[('share', ['rdrandom.rst'])],
    classifiers = ["Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",],
    extras_require={
        'tests': [],
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme']}
)


