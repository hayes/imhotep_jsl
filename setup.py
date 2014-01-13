from setuptools import setup, find_packages

setup(
    name='imhotep_jsl',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/mghayes/imhotep_jsl',
    license='MIT',
    author='Michael Hayes',
    author_email='michael@hayes.io',
    description='An imhotep plugin for the jsl linter',
    entry_points={
        'imhotep_linters': [
            '.js = imhotep_jsl.plugin:JSL'
        ],
    },
)