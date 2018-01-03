## Presentation
[https://docs.google.com/presentation/d/17ikjcuUZOd2MBCBKHDTNHQxTlDe1NF9aKgTa6cc79Bs/edit?usp=sharing](https://docs.google.com/presentation/d/17ikjcuUZOd2MBCBKHDTNHQxTlDe1NF9aKgTa6cc79Bs/edit?usp=sharing)

## Run on cpu
`docker run --rm -it -v $(pwd):/project -w /project tensorflow/tensorflow:latest python 1.py`

## Run on gpu
`docker run --rm -it --runtime nvidia -v $(pwd):/project -w /project tensorflow/tensorflow:latest-gpu python 1.py` (nvidia-docker and nvidia drivers required)

## Run tensorboard
`docker run --rm -it -p 6006:6006 -v $(pwd):/project -w /project tensorflow/tensorflow:latest tensorboard --logdir ./logs` - then enter `localhost:6006`

## Run jupyter
`docker run --rm -it -p 8888:8888 tensorflow/tensorflow:latest`
