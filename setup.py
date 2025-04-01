from setuptools import setup
from codecs import open
from os import path
from se3dif import __version__


setup(
    name='se3dif',
    version=__version__,
    description='SE(3)-DiffusionFields. A library to learn and sample from diffusion models on SE(3). We show how to train and use them for learning 6D grasp distributions.',
    author='Julen Urain',
    author_email='julen@robot-learning.de',
    packages=['se3dif', 'isaac_evaluation'],
)
