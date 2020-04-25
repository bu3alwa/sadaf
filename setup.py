import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sadaf", 
    version="0.0.1",
    author="Ali",
    description="A reverse shell manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bu3alwa/sadaf",
    packages=['sadaf'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {
	'console_scripts': [
		'sadaf = sadaf.cli:main'
	]}
)
