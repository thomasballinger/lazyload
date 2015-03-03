from setuptools import setup
import ast
import os

setup(name='lazyload',
      version='0.0.1',
      description='Force modules loaded later not to be loaded until attribute access',
      url='https://github.com/thomasballinger/lazyload',
      author='Thomas Ballinger',
      author_email='thomasballinger@gmail.com',
      license='MIT',
      packages=['lazyload'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
      )