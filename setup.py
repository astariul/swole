import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="swole",
    version="0.0.3",
    author="Nicolas REMOND",
    author_email="remondnicola@gmail.com",
    description="Streamlit, but better.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astariul/swole",
    packages=setuptools.find_packages(),
    package_data={'swole': ['skins/*.css']},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
)
