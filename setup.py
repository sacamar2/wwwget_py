from setuptools import find_packages, setup
import os
import sys

try:
    os.system('wsl echo WSL is ready!')
except:
    print('WSL is not available. Check https://learn.microsoft.com/en-us/windows/wsl/install')
    sys.exit(1)

setup(
	name="wwwgetpy",
    version="0.1",
    description="It is a Windows WSL wget python lib to use it for HTML folder directories in paralel",
    package_dir={"":"src"},
    packages=find_packages(where="src"),
	author="sacamar2",
    url="https://github.com/sacamar2/wwwget_py",
    classifiers=[
        "Operating System :: Windows",
        "License :: OSI Approved :: MIT License"
    ],
	license="MIT",
    extras_require={"dev":"twine>=4"},
	python_requeries=">=3.11"
)
