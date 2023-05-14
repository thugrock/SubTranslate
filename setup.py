from setuptools import setup, find_packages

setup(
    version="1.0",
    name="SubErate",
    packages=find_packages(),
    py_modules=["SubTranslate"],
    author="Polapragada Yashwant",
    install_requires=[
        'translator',
    ],
    description="Automatically translate the SRT",
    entry_points={
        'console_scripts': ['SubTranslate=SubTranslate.cli:main'],
    },
    include_package_data=True,
)
