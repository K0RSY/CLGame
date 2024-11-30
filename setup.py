from setuptools import setup, find_packages

setup(
  name='CLGame',
  version='1.0',
  author='Korsy',
  author_email='pgeorg@gmail.com',
  packages=['CLGame'],
  install_requires=['playsound>=1.3.0', 'pynput>=1.7.7'],
  python_requires='>=3.10'
)
