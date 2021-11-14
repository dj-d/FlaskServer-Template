from setuptools import find_packages, setup

requirements = [
    'flask',
    'Flask-WTF',
    'python-dotenv',
    'waitress'
]

setup(
    name='AmazonPriceTracker-Backend',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    extra_require={
        'dev': [
            'pytest',
            'coverage'
        ]
    }
)
