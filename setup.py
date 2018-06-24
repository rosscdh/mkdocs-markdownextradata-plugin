import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-markdownextradata-plugin',
    version='0.0.4',
    description='A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template',
    long_description=read('README.md'),
    keywords='mkdocs python markdown extra values',
    url='https://github.com/rosscdh/mkdocs-markdownextradata-plugin/',
    author='Ross Crawford-d\'Heureuse',
    author_email='sendrossemail@gmail.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=0.17'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'markdownextradata = markdownextradata.plugin:MarkdownExtraDataPlugin'
        ]
    }
)
