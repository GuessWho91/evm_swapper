from setuptools import setup

setup(
   name='evm_swapper',
   version='0.1.0',
   description='Module to swap with EVM web3 wallets',
   author='GuessWho',
   author_email='eu1qjqaw8dda@mail.ru',
   packages=['evm_swapper'],
   include_package_data=True,  # Include non-Python files specified in MANIFEST.in
   package_data={
      'evm_swapper': ['contracts/*'],  # Explicitly include the contracts directory
   },
   install_requires=[]
)
