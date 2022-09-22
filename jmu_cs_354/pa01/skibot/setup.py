from setuptools import setup
import glob

package_name = 'skibot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/images/', ['images/arrow.png']),
        ('share/' + package_name + '/images/', ['images/indigo.png']),
        ('share/'  + package_name + '/launch/', ['launch/skibot_launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mridul',
    maintainer_email='mridul@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'skibot_node = skibot.skibot_node:main'
        ],
    },
)
