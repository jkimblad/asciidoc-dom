from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup (
    name = "Asciidoc-dom",
    version = "0.1.0",
    description = "A DOM library for asciidoc",
    long_description = readme,
    author = "Jacob Kimblad",
    author_email = "jacob.kimblad01@gmail.com",
    url = "",
    license = "",
    packages=find_packages(exclude=("tests"))
)
