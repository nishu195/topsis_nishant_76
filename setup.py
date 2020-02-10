import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis_nishant_76", # Replace with your own username
    version="12.1.4",
    author="Nishant Goel",
    author_email="ngoel_be17@thapar.edu",
    description="A topsis Implementation in python for multi-criteria decision making",
    url="https://github.com/nishu195/nishant_outlier_76",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["topsis_nishant_76"],
    package_dir={'':'src'},
    keywords = ['command-line', 'Outliers', 'outlier-removal','row-removal'],  
    install_requires=[            
          'numpy',
          'pandas',
          'scipy',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["bin/topsis_cli"],
    python_requires='>=3.6',
)