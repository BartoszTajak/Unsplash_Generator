from distutils.core import setup

setup(name='gallery_generator',
      version='1.0',
      packages=['gallery_generator'],
      install_requires=[
            "Pillow",
            "requests",
            "python-dotenv"
      ]
      )
