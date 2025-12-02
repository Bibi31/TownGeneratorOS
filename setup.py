"""Setup file for the Medieval Fantasy City Generator Python port."""
from setuptools import setup, find_packages

with open("README_PYTHON.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="towngenerator",
    version="0.1.0",
    author="Oleg Dolya (original), Python port contributors",
    description="Medieval Fantasy City Generator - Python port",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bibi31/TownGeneratorOS",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "towngenerator=watabou.towngenerator.main:main",
        ],
    },
)
