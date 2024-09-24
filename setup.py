from setuptools import setup, find_packages

setup(
    name='budget-cli',           
    version='1.0.0',            
    packages=find_packages(),    
    install_requires=[           
        'supabase',
        'python-dotenv',
        'certifi',  
    ],
    entry_points={
        'console_scripts': [
            'budget = budget.budget:main',  
        ],
    },
)