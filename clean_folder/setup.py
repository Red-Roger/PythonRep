from setuptools import setup, find_namespace_packages

setup (name='clean_folder',
      version='1',
      description='clean folder code',
      url='https://github.com/Red-Roger/PythonRep/tree/main/clean_folder',
      author='Red Roger',
      author_email='postny@email.ua',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)