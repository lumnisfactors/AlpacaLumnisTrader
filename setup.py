import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alpaca-lumnis-trader",
    packages = ['AlpacaLumnisTrader'],
    version="0.1.0",
    author="Abubakarr Jaye",
    author_email="contact@lumnis.io",
    description="Lumnis Alternative Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lumnisfactors/AlpacaLumnisTrader/archive/refs/tags/0.1.0.tar.gz",
    py_modules = ["alpaca-lumnis"],
    install_requires=[
        'grequests',
        'pandas',
        'scipy',
        'numpy',
        'scikit-learn',
        'seaborn',
        'matplotlib',
        'alpaca-trade-api',
        'alpaca-py',
        'lumnisfactors',
        'tqdm',
        'arcticdb'
],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

