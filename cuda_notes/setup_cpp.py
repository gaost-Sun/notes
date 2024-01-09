from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

setup(
    name='cppcuda_tutorial',
    version='1.0',
    author='gaost-Sun',
    author_email='sunhao5871@126.com',
    description='cppcuda example',
    long_description='cppcuda example',
    ext_modules=[
        CppExtension(
            name='cppcuda_tutorial',
            sources=['interpolation.cpp'])
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
    
)