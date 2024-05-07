from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='e'
def get_requirements(file_path: str):
    '''
    This function will return the list of requirements.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != '-e .']

        if  HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='end_to_end_ml_project',
    version='0.0.1',
    author='Laddu',
    author_email='fiftybucks001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)