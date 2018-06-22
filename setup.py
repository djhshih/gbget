from distutils.core import setup
import sys

sys.path.append('gbget')
import gbget


setup(name='gbget',
      version='0.1',
      author='David J. H. Shih',
      author_email='djh.shih@gmail.com',
      url='http://github.com/djhshih/gbget/',
      description='Download nucleotide sequences from genbank. Based on original work by Simon Greenhill <simon@simon.net.nz>',
      long_description=gbget.__doc__,
      scripts=['gbget.py'],
      py_modules=['gbget'],
      provides=['gbget'],
      keywords='genbank genetics mitchondria bioinformatics fasta',
      license="BSD License",
      classifiers=[
          "Programming Language :: Python", 
          "Intended Audience :: Science/Research", 
          "License :: OSI Approved :: BSD License",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Bio-Informatics",
      ],
     )
