from setuptools import setup, find_packages

setup(
    name='profane_detector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'word_finder',
    ],
    entry_points={
        'console_scripts': [
            'profane_detector=profane_detector:main',
        ],
    },
)
