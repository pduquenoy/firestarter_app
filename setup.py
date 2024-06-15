from setuptools import setup, find_packages

setup(
    name="firestarter",
    version="0.5.18",
    # packages=find_packages(),
    packages=["firestarter"],
    include_package_data=True,
    install_requires=[
        "argparse",
        "PySerial",
    ],
    entry_points={
        "console_scripts": [
            "firestarter=firestarter.main:main",
        ],
    },
    package_data={
        "firestarter": ["database.json", "pin-map.json"],
    },
    author="Henrik Olsson",
    author_email="henols@gmail.com",
    description="A brief description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/henols/firestarter_app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
