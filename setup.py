from setuptools import setup, find_packages

setup(
    name='Sorty',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sorty=sorty:main',  # Assuming 'main' is the entry point in sorty module
        ],
    },
    description='A sorting application packaged with PyInstaller',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/zanndatsu/Sorty',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
)