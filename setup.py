#!venv/bin/python

from setuptools import setup

setup(
    name='scapely',
    version='0.0.1',
    description='Polygonal approximation of terrains and height fields',
    author='Karsten Deininger',
    url='https://github.com/karsten-d/scapely',
    packages=['scapely'],
    license='License :: OSI Approved :: BSD License',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Other Environment',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    install_requires=[
        'shapely'
    ]
)
