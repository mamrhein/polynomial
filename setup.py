# coding=utf-8
"""Setup package 'polynomial'."""

from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
    name="polynomial",
    author="Michael Amrhein",
    author_email="michael@adrhinum.de",
    url="https://github.com/mamrhein/polynomial",
    description="Defining and calculating with univariate polynomials.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=False,
    python_requires=">=3.9",
    install_requires=[],
    tests_require=["pytest"],
    license='BSD',
    keywords='univariate polynomial',
    platforms='all',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
