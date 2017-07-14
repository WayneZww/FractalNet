FractalNet
==========

Use the FractalNet of caffe version from `gustavla <https://github.com/gustavla/fractalnet>`__. Add the Windows PowerShell scripts and python scripts to generate the prototext  file for caffe with fixing the encoding problem.

A fractal-based neural network architecture:

* `Project page <http://people.cs.uchicago.edu/~larsson/fractalnet/>`__
* `arXiv paper <https://arxiv.org/abs/1605.07648>`__

Drop-path
---------
The auther provide a reference implementation for the elementwise-mean layer with local
drop-path. There is still no public release of local+global, but we suggest
implementing this through tying weights. 

Caffe
--------
See the ``caffe`` directory for code and more information.

Fractal pattern generation
--------------------------
Use the provided simple Python scripts, and fixed some problems. See the ``generation`` directory for
code and more information.

Data augmentation
-----------------
Try to use the lmdb file as input layer in Caffe to implement data augmentation. 
The way to build a cifar10 dataset for caffe can been see 

Cite
----
Please consider citing ::

    @article{larsson2016fractalnet,
      title={FractalNet: Ultra-Deep Neural Networks without Residuals},
      author={Larsson, Gustav and Maire, Michael and Shakhnarovich, Gregory},
      journal={arXiv preprint arXiv:1605.07648},
      year={2016}
    }

