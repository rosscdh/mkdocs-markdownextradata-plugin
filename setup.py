import os
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path) as file:
        content = file.read()
    return content if content else 'no content read'


setup(
    name='mkdocs-markdownextradata-plugin',
    version='0.2.6',
    description='A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown extra values',
    url='https://github.com/rosscdh/mkdocs-markdownextradata-plugin/',
    author='Ross Crawford-d\'Heureuse',
    author_email='sendrossemail@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs',
        'pyyaml',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'markdownextradata = markdownextradata.plugin:MarkdownExtraDataPlugin'
        ]
    }
)
