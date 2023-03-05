from setuptools import setup , find_packages

def get_requirements(filepath:str)->list:
    requirements=[]
    hyp_e='-e .'
    with open(filepath) as f:
        requirements=f.readlines()
    requirements=[req.replace('\n','') for req in requirements]
    if hyp_e in requirements:
        requirements.remove(hyp_e)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Naveed',
    author_email='imnaveed000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
