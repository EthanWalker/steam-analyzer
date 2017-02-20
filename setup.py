from setuptools import setup
from codecs import open

def lines(text):
    """
    Returns each non-blank line in text enclosed in a list.
    """
    return [l.strip() for l in text.strip().splitlines() if l.strip()]

setup(
    name='steam-analyzer',
    version='0.1.0',
    author='Ethan Walker',
    author_email='ethan@foundationtech.us',
    description='Flask app for Steam data comparison ',
    long_description=open('README.md', encoding='utf-8').read(),
    url='https://github.com/EthanWalker/steam-analyzer',
    license='Attribution-NonCommercial 2.0',
    #packages=['steam-analyzer'],
    py_modules = ['steam'],
    setup_requires=[],
    install_requires=['Flask==0.11.1',
                      'requests==2.11.1',
                      'requests-cache==0.4.13',],
    tests_require=['tox', 'pytest',],
    zip_safe=False,
    keywords='steam',
    classifiers=lines("""
        Development Status :: 2 - Pre-Alpha
        Operating System :: OS Independent
        License :: Free for non-commercial use
        Intended Audience :: End Users/Desktop
        Programming Language :: Python :: 3.5
        Topic :: Internet
    """)
)
