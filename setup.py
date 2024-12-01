from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()
    
setup(
  name='CLGame',
  version='1.0',
  author='Korsy',
  author_email='pgeorg@gmail.com',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/K0RSY/CLGame',
  packages=['CLGame'],
  install_requires=['playsound>=1.3.0', 'pynput>=1.7.7'],
  python_requires='>=3.10'
)
