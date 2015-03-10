from setuptools import setup

setup(name='lazyload',
      version='0.0.2',
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
          'Programming Language :: Python :: 3',
          ],
      )
