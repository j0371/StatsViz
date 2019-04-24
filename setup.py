import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statsviz",
    version="1.2.1",
    author="Marcus Higgins",
    author_email="halo2305@gmail.com",
    description="A package that provides a gui to plot graphs from CSV files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j0371/StatsViz",
    packages=setuptools.find_packages(),
    install_requires=[
        "matplotlib",
        "scipy",
        "natsort"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

