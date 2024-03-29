import setuptools


VERSION = '0.1.2'


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='gpt3_simple_primer',
    version=VERSION,
    author='happilyeverafter95',
    author_email='author@example.com',  # TODO: update email
    description='GPT-3 wrapper for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/happilyeverafter95/gpt-3',
    install_requires=['openai==0.11.0'],
    project_urls={
        'Bug Tracker': 'https://github.com/happilyeverafter95/gpt-3/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=['gpt-3', 'text generation', 'language model', 'priming'],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.7.1',
)
