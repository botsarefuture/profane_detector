from setuptools import setup, find_packages

setup(
    name='profane_detector',
    version='0.1',
    packages=find_packages(),
    authors = [
    { name="Verso Vuorenmaa", email="verso.vuorenmaa@sinimustaahallitustavastaan.org" },
    ],
    package_data={
        'profane_detector': ['swear-words/*'],
    },
    install_requires=[
        'fuzzywuzzy',
        'python-Levenshtein'
    ],
    entry_points={
        'console_scripts': [
            'profane_detector = profane_detector:main',
        ],
    },
)
