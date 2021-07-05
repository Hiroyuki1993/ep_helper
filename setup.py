import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sample_command",
    version="0.1.0",
    author="hiroyuki-kuromiya",
    author_email="khiroyuki1993@gmail.com",
    description="Support Your Post to Evidence Portal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hiroyuki1993/ep-helper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['sample_command = sample_command.sample_command:main']
    },
    python_requires='>=3.7',
)