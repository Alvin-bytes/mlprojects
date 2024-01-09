from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
#This will return a list of requirements
def get_requirements(file_path:str)->list[str]:

   requirements=[]
   with open(file_path) as file_obj:
      requirements=file_obj.readlines()
      #replace \n with a blank in requiremnts.txt
      requirements=[req.replace("\n","")for req in requirements]

      if HYPHEN_E_DOT in requirements:
         requirements.remove(HYPHEN_E_DOT)

      return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Alvin',
    author_email='alvinlamb123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)