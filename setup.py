"""Setup file for small-kg package."""
from setuptools import setup

setup(
    name='small_kg',
    version='0.1.0',
    author='Patrick Wang',
    author_email='patrick@covar.com',
    url='https://github.com/patrickkwang/small-kg',
    description='Small KG',
    packages=['small_kg'],
    package_data={'small_kg': ['*.csv', '*/*.csv']},
    zip_safe=False,
    license='MIT',
    python_requires='>=3.6',
)
