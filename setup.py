from distutils.core import setup

setup(
    name = 'pymydb',
    packages = ['pymydb'],
    install_requires = ['pymysql'],
    version = '0.2',
    description = 'A wrapper over PyMySQL Package to simplify MySQL database usage',
    author = 'Adarsh Honawad',
    author_email = 'adarsh2397@gmail.com',
    url = 'https://github.com/adarsh2397/PyMyDb',
    download_url = 'https://github.com/adarsh2397/PyMyDb/archive/0.2.tar.gz',
    keywords = ['mysql','sql','database','python','package'],
    classifiers = [],
)