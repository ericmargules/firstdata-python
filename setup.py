from setuptools import setup, find_packages

setup(
    name="firstdata",
    version="0.0.1",
    description="FirstData Python Library",
    long_description="The FirstData Python SDK allows access to FirstData Global Payment API.",
    author="Eric Margules",
    author_email="Eric.Margules@firstdata.com",
    url="https://github.com/GBSEcom/Python",
    packages=find_packages(exclude=['docs', 'tests*']),
    zip_safe=False,
    # license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha',"
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ],
    keywords="FirstData Global Payment API"
)
