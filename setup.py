from setuptools import setup, find_packages
import sys, os

# The dependencies variable is used by MAP Client to
# determine if further downloads are required.  Please
# list all dependencies here.
dependencies = [] # Insert plugin dependencies here

setup(name=u'mapclientplugins.transformpointcloudstep',
      version='0.0',
      description='',
      long_description="",
      classifiers=[],
      author=u'Hugh Sorby',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup',]),
      namespace_packages=['mapclientplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=dependencies,
      )
