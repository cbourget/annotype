from setuptools import setup


package_name = 'annotype'

install_requires = [
    'marshmallow>=3.0.0b7',
    'wheel'
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
    author='Charles-Éric Bourget',
    author_email='charlesericbourget@gmail.com',
    description='Marshmallow and Python 3 annotations',
    license='MIT',
    url='https://github.com/cbourget/annotype',
    keywords = [
        'annotation',
        'marshmallow',
        'type'
    ],
    classifiers=[],
    install_requires=install_requires,
    extras_require=extras_require
)
