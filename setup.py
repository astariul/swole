import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="dummygummy",
    version="0.1",
    author="Nicolas REMOND",
    author_email="nicolas.remond@42maru.com",
    description="Short description of the package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/colanim/python-repo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
)
