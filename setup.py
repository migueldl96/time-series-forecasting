from setuptools import setup, find_packages

setup(name='tsf',
      version='0.1',
      description='Time series preprocessing based on windows analysis',
      url='https://github.com/migueldl96/TSF-library',
      author='Miguel Diaz',
      author_email='migueldialoz@gmail.com',
      license='Universidad de Cordoba',
      packages=find_packages(),
      install_requires=['sklearn', 'numpy'],
      zip_safe=False)
