import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alpaca-lumnis-trader",
    packages = ['alpaca-lumnis-trader'],
    version="0.0.2",
    author="Abubakarr Jaye",
    author_email="contact@lumnis.io",
    description="Lumnis Alternative Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lumnisfactors/AlpacaLumnisTrader/archive/refs/tags/0.0.2.tar.gz",
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
        'tqdm'
],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

