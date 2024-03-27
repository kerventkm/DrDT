from setuptools import setup, find_packages

setup(
    name='drdt',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'drdt': ['datasets/*', 'datasets/DecisionRuleSystems/*', 'datasets/UCIMLDatasets/*'],
    },
)