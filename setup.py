import pathlib

import setuptools

ROOT = pathlib.Path(__file__).parent
README = (ROOT / "README.md").read_text()
CHANGELOG = (ROOT / "CHANGELOG.md").read_text()
REQUIREMENTS = (ROOT / "requirements.txt").read_text().split()

setuptools.setup(
    name="hue-api",
    version="0.2.1",
    description="Async API for controlling Hue Lights",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Nirantak Raghav",
    author_email="hey@nirantak.com",
    url="https://github.com/nirantak/hue-api",
    license="MIT",
    python_requires=">=3.7",
    install_requires=REQUIREMENTS,
    packages=setuptools.find_packages(include=["hue", "hue.*"]),
    include_package_data=True,
    keywords="hue lights async automation",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "hue=hue.cli:app",
        ],
    },
    project_urls={
        "Documentation": "https://github.com/nirantak/hue-api#readme",
        "Source": "https://github.com/nirantak/hue-api",
        "Tracker": "https://github.com/nirantak/hue-api/issues",
    },
)
