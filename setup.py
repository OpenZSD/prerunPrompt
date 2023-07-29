from setuptools import setup
import setuptools

setup(name = 'PrerunPrompt',
      version = '1.0.0',
      author = 'OpenZSD',
      author_email = 'open@z-softdevelopment.com',
      description = 'A simple python utility to show a dialog before running command',
      url = 'www.z-softdevelopment.com',
      package_dir = { 'PrerunPrompt': 'PrerunPrompt',
                      'PrerunPromptInstall': 'PrerunPromptInstall' },
      packages = setuptools.find_packages(),
      package_data = {
        'PrerunPromptInstall':['setup/installDep.sh']
      },
      install_requires=['argparse', 'screeninfo'],
      entry_points = {
        'console_scripts': ['setupPrerunPrompt = PrerunPromptInstall.main:mainFunc',
                            'prerunPrompt = PrerunPrompt.main:mainFunc']
      })

