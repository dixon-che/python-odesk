from distutils.core import setup

version = __import__('odesk').get_version()


setup(name='python-odesk',
      version=version,
      description='Python bindings to odesk API',
      long_description='Python bindings to odesk API',
      author='odesk',
      author_email='python@odesk.com',
      packages = ['odesk',],
      url='http://github.com/odesk/python-odesk',
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities',
                   ''],)