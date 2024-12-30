from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''this application return the requirements'''
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements= file_obj.readline()
        requirements=[req.replace('\n',"")for req in requirements]
        return requirements

setup(
    name="Corona Project",
    version="0.01",
    author="Piyush",
    author_email="piyushrawal93@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
       
    
)