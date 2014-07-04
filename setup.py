from distutils.core import setup

setup(
    name='blockr-python',
    version='0.1.0',
    packages=['blockr'],
    url='https://github.com/stormpat/blockr-python',
    license='MIT',
    author='Patrik Storm',
    author_email='george.sibble@gmail.com',
    description='Integration Library for the Coinbase API',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'requests>=2.2.1',
    ],
)
