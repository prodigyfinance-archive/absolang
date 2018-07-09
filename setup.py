from setuptools import setup, find_packages

setup(
    name="absolang",
    version="0.0.2",
    url='http://github.com/prodigyfinance/absolang',
    license='Unknown',
    description=(
        "A sentiment analysis library for detecting absolutist language."
    ),
    long_description=open('README.rst', 'r').read(),
    author='Prodigy Finance',
    author_email='devops@prodigyfinance.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'spacy',
    ],
    extras_require={
        'dev': ['flake8', 'pytest==3.6.0', 'pytest-flake8==1.0.1'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
