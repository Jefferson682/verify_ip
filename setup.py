from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="verify ip",
    author="J. Jefferson N. do Vale",
    version="0.0.1",
    description="Verification and send IP for security group on AWS",
    packages=find_packages(exclude="../.venv/"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")}
)