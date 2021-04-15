import pathlib

import setuptools

ROOT = pathlib.Path(__file__).parent
README = (ROOT / "README.md").read_text()
HISTORY = (ROOT / "HISTORY.md").read_text()

requirements = [
    "Click>=7.0",
    "httpx",
    "python-dotenv",
]

setuptools.setup(
    name="hue-api",
    version="0.0.1",
    description="Async API for controlling Hue Lights",
    long_description=README + "\n\n" + HISTORY,
    long_description_content_type="text/markdown",
    author="Nirantak Raghav",
    author_email="hey@nirantak.com",
    url="https://github.com/nirantak/hue-api",
    license="MIT",
    python_requires=">=3.7",
    install_requires=requirements,
    packages=setuptools.find_packages(include=["hue", "hue.*"]),
    include_package_data=True,
    keywords="hue lights async automation",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            "hue=hue.cli:main",
        ],
    },
    project_urls={
        "Documentation": "https://github.com/nirantak/hue-api#readme",
        "Source": "https://github.com/nirantak/hue-api",
        "Tracker": "https://github.com/nirantak/hue-api/issues",
    },
)
