from setuptools import setup

package_name = 'skibot_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='calvin',
    maintainer_email='calvin.d.woo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'skibot_nav_node = skibot_nav.skibot_nav_node:main',
            'service = skibot_nav.move_skibot_to_point:main'
        ],
    },
)
