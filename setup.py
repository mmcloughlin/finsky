from setuptools import setup
import re

pkg_init_file = open('finsky/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", pkg_init_file))

def readme():
    return open('./README.rst').read()

setup(name='finsky',
      version=metadata['version'],
      description='Google Play API',
      long_description=readme(),
      url='https://github.com/mmcloughlin/finsky',
      author='Michael McLoughlin',
      author_email='mmcloughlin@gmail.com',
      license='MIT',
      packages=['finsky', 'finsky.protos'],
      entry_points={
          'console_scripts': [
              'finsky = finsky.cli:main',
              ]
          },
      install_requires=[
          'requests',
          'pydash',
          'protobuf',
          'pyyaml',
          ],
      )
