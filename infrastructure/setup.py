import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crypto-ml-abhishekpratapa", # Replace with your own username
    version="0.0.1",
    author="Abhishek Pratpa",
    author_email="abhishekpratapa@gmail.com",
    description="A package for easily trading and testing crypto algorithims",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ATCUWgithub/CryptoML",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
