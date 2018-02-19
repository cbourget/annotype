from setuptools import (
    find_packages,
    setup
)


package_name = 'annotype'

install_requires = [
    'marshmallow>=3.0.0b7'
]

extras_require={
    'tests': [
        'pytest',
        'coverage',
        'pytest-cov'
    ]
}



setup(
    name=package_name,
    version='0.1.0',
    author='Charles-Eric Bourget',
    author_email='charlesericbourget@gmail.com',
    description='Marshmallow and Python 3 annotations',
    long_description=open('README.rst').read(),
    license='MIT',
    url='https://github.com/cbourget/annotype',
    download_url='https://github.com/cbourget/annotype/archive/0.1.1.tar.gz',
    keywords = 'annotation marshmallow type',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=install_requires,
    extras_require=extras_require
)
