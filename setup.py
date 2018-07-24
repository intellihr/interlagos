import io
import os
import sys
import atexit

from setuptools import find_packages, setup, Command
from setuptools.command.install import install as _install
from setuptools.command.develop import develop as _develop
from setuptools.command.egg_info import egg_info as _egg_info

# Package meta-data
NAME = 'interlagos'
DESCRIPTION = 'A module with helper functions for NLP preprocessing.'
URL = 'https://gitlab.com/intellihr/interlagos'
EMAIL = 'alfred.see@intellihr.com.au'
AUTHOR = 'Alfred See'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = ['autocorrect==0.3.0', 'nltk==3.3', 'python-rake==1.4.5']

# What packages are optional?
EXTRAS = {}

# What NLTK data are required?
NLTK_DATA = ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger']

# ------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(
            os.path.join(here, NAME, '__version__.py'), encoding='utf-8') as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class ReleaseCommand(Command):
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f'\033[1m{s}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status('Building Source and Wheel (universal) distribution...')
        os.system(f'{sys.executable} setup.py sdist bdist_wheel --universal')

        sys.exit()


def post_install(setup):
    def post_actions():
        import nltk
        for data in NLTK_DATA:
            nltk.download(data)

    post_actions()

    return setup


class InstallCommand(_install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(post_install)


class DevelopCommand(_develop):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(post_install)


class EggInfoCommand(_egg_info):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(post_install)


setup = post_install(
    setup(
        name=NAME,
        version=about['__version__'],
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=EMAIL,
        python_requires=REQUIRES_PYTHON,
        url=URL,
        packages=find_packages(exclude=('tests', )),
        install_requires=REQUIRED,
        extras_require=EXTRAS,
        include_package_data=True,
        license='MIT',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English', 'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        cmdclass={
            'release': ReleaseCommand,
            'install': InstallCommand,
            'develop': DevelopCommand,
            'egg_info': EggInfoCommand
        }))
