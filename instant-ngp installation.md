# The environment
* GUP: A100 
* ubuntu: 20.04
* CUDA: 11.7
* Pytorch: 1.13.0+cu117 (torchvision, torchaudio are coresponding to the version on the official website)
* python: 3.8.18
* cmake: 3.21.0 (>=3.21.0)
* gcc: 9.4.0(>=8.0.0)

# tiny-cuda-nn installation
* Install the following packages:<br/>
`sudo apt-get install build-essential git`

* Adding the CUDA installation to your PATH. For example, if you have CUDA 11.7, add the following to your ~/.bashrc.<br/>
`export PATH="/usr/local/cuda-11.7/bin:$PATH"`<br/>
`export LD_LIBRARY_PATH="/usr/local/cuda-11.7/lib64:$LD_LIBRARY_PATH"`

* Clone this repository and all its submodules using the following command ***(easy to fail && slow)***:<br/>
`git clone --recursive https://github.com/nvlabs/tiny-cuda-nn`<br/>
beacuse there are two link  in tiny-cuda-nn/dependencies
![Alt text](img/image-2.png)

* So there is a replace way(Work):<br/>
`git clone https://github.com/nvlabs/tiny-cuda-nn`<br/>
or `git clone https://gitee.com/xubin1994/tiny-cuda-nn.git`***(Faster)***<br/>
`cd tiny-cuda-nn/dependencies`<br/>
`git clone https://gitee.com/qijunniu/fmt.git`<br/>
`git clone https://gitee.com/git_mirror/cutlass.git`

* Move to ./tiny-cuda-nn. Then, use CMake to build the project: <br/>
`tiny-cuda-nn$ cmake . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo`<br/>
`tiny-cuda-nn$ cmake --build build --config RelWithDebInfo -j`

* Then,<br/>
`tiny-cuda-nn$ cd bindings/torch`<br/>
`tiny-cuda-nn/bindings/torch$ python setup.py install`

# Problem List
* P1: cannot find -lcuda: No such file or directory(in the step "python setup.py install")
![Alt text](img/image.png)

* solution: https://github.com/NVlabs/tiny-cuda-nn/issues/183
![Alt text](img/image-1.png)

