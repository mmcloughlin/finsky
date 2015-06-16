from setuptools import setup
import re

pkg_init_file = open('finsky/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", pkg_init_file))

setup(name='finsky',
      version=metadata['version'],
      description='Google Play API',
      url='https://github.com/mmcloughlin/finsky',
      author='Michael McLoughlin',
      author_email='mmcloughlin@gmail.com',
      license='MIT',
      packages=['finsky'],
      )
