from setuptools import find_packages,setup #finds all pakages in the entire project
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]: #return List[str]
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
   
    return requirements

get_requirements('requirements.txt')
setup(
name='mlprojectpractice',
version='0.0.1',
author='jimpi',
author_email='eg6@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
