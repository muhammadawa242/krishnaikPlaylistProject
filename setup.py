from setuptools import find_packages, setup

def get_requirements():
    '''
    Returnsd a list of requirements
    '''
    
    with open('requirements.txt') as f:
        lines = f.readlines()
        requirements = [l.replace('\n','') for l in lines]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name='tutorialml',
    version='0.0.1',
    author='Muhammad Awais',
    packages=find_packages(),
    install_requires=get_requirements()
)