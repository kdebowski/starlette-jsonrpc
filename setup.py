import os
import setuptools


dir_path = os.path.dirname(os.path.realpath(__file__))


def read(fname):
    with open(fname, "r") as f:
        return f.read()


install_requires = [
    l
    for l in read(os.path.join(dir_path, "requirements.txt")).splitlines()
    if l and not l.startswith("#")
]


setuptools.setup(
    name="starlette-jsonrpc",
    version="0.2.1",
    author="Kamil Dębowski",
    author_email="poczta@kdebowski.pl",
    description="JSON-RPC implementation for Starlette framework",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/kdebowski/starlette-jsonrpc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    install_requires=install_requires,
    include_package_data=True,
)
