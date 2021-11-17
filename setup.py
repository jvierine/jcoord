import setuptools

#Genrate long description using readme file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jcoord",
    version="1.0.0",
    author="Juha Vierinen",
    author_email="juha-pekka.vierinen@uit.no",
    description="Simple geographic coordinate conversion routines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'numpy>=0.13.1',
        'scipy>=0.0.1',
        'matplotlib>=1.0.4'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=2.0",
)
