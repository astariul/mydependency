import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="mydependency",
    version="1.0",
    author="Nicolas REMOND",
    author_email="remondnicola@gmail.com",
    description="A public github-hosted python package for test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astariul/mydependency",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
)