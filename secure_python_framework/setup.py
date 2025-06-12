from setuptools import setup, find_packages

setup(
    name='secure_python_framework',
    version='0.1.0',
    author='Soundheard',
    description='A framework for encoding and decoding text using custom mappings.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/secure_python_framework',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add any dependencies your project needs here
    ],
)