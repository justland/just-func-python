from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="just-func",
    version="0.1dev",
    author="Vincent White",
    author_email="xstrengthofonex@gmail.com",
    description="A python interpreter for the just-func language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justland/just-func-python",
    package_dir={"": "justfunc"},
    packages=find_packages(where="justfunc")
)
