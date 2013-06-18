from setuptools import setup, find_packages

setup(
    name='datastringer',
    version='0.1.4',
    description="Client for datawi.re, submits data to the data wire service.",
    long_description="",
    classifiers=[],
    keywords='data record notifications service client wire',
    author='Friedrich Lindenberg',
    author_email='info@datawi.re',
    url='http://github.com/pudo/datastringer',
    license='AGPLv3',
    py_modules=['datastringer'],
    zip_safe=False,
    install_requires=[
        "requests>=1.2"
    ],
    tests_require=[],
    entry_points=""" """,
)
