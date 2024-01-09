import glob
import os.path as osp
from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension


ROOT_DIR = osp.dirname(osp.abspath(__file__))
include_dirs = [osp.join(ROOT_DIR, "include")]

sources = glob.glob('*.cpp')+glob.glob('*.cu')


setup(
    name='cppcuda_tutorial',
    version='1.0',
    author='gaost-Sun',
    author_email='sunhao5871@126.com',
    description='cuda volume rendering library',
    long_description='cuda volume rendering library',
    ext_modules=[
        CUDAExtension(
            name='cppcuda_tutorial',
            sources=sources,
            include_dirs=include_dirs
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)