from setuptools import setup, find_packages


setup(
    name='mkdocs-markdownextradata-plugin',
    version='0.0.1',
    description='A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template',
    long_description='As a user with variables that need to be substituted for multiple projects at the markdown '
                     'and not the template level. '
                     'In order to defined values such as site urls, client names etc '
                     'So that I can build my docs with different values for images and urls. ',
    keywords='mkdocs python markdown extra values',
    url='https://github.com/rosscdh/mkdocs-markdownextradata-plugin/',
    author='Lukas Geiter',
    author_email='info@lukasgeiter.com',
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