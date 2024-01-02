from setuptools import setup,find_packages
from typing import List

HYPEN_E = '-e .'

def get_requirements(filepath:str) -> List[str]:
    requirements=[]

    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)

    return requirements

setup(
name='DS_Project',
version='0.0.1',
author='kriShaileshsh',
author_email='shaileshkaliya124@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)