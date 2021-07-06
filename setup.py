from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tasks",
    version="0.1.0",
    author="hiroyuki-kuromiya",
    author_email="khiroyuki1993@gmail.com",
    description="Support Your Post to Evidence Portal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hiroyuki1993/ep_helper",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)