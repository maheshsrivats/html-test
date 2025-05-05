from setuptools import setup

setup(
    name='your-streamlit-project',
    version='1.0.0',
    description='A simple Streamlit project for Azure Static Web Apps',
    py_modules=['test_streamlit'],
    install_requires=[
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'run-app=test_streamlit:main',
        ],
    },
)
