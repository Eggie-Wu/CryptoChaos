from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="cryptochaos",
    version="1.0.0",
    description="Simple encryption/decryption algorithms based on chaotic maps.",
    url="https://github.com/Eggie-Wu/CryptoChaos",
    author="Eggie Wu",
    author_email="qihan.wu@mail.mcgill.ca",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    project_urls={
        "Bug Reports": "https://github.com/Eggie-Wu/CryptoChaos/issues",
        "Source": "https://github.com/Eggie-Wu/CryptoChaos",
    },
)
