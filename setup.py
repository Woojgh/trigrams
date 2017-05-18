from setuptools import setup

dependencies = ['ipython']
extra-Packages = {'testing': ['pytest', 'pytest-watch']}

setup(
    name='trigram',
    description='Implements the trigram function.',
    version='0.1',
    author=['JamesT', 'EricE'],
    #author_email='',
    #license='',
    py_modules=['ackermann'],
    #package_dir={'': 'src'}
    install_requires=dependencies,
    extra_require=extra_packages

)