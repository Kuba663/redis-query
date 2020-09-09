import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="redis-query",
    version="0.0.1",
    description="A query language for redis.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Kuba663/redis-query",
    author="VirtualFox",
    author_email="virtualfox@onet.pl",
    license="GNU GPL V3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Development Status :: 2 - Pre-Alpha",
    ],
    packages=["RedisQuery"],
    include_package_data=True,
    install_requires=["redis", "rejson", "rply"],
)
