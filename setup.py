from setuptools import find_packages,setup
from typing import List

E_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requiremants
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requiremants=file_obj.readlines()
        requiremants=[req.replace("\n","") for req in requiremants]

        if E_dot in requiremants:
            requiremants.remove(E_dot)

    return requiremants
setup(
name='mlproject',
version='0.0.1',
auther='amarnadh',
auther_email='amarnadh748@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)