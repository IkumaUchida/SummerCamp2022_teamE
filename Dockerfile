# FROM  nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04

# ENV DEBIAN_FRONTEND=noninteractive

# RUN apt update \
#     && apt install -y \
#     wget \
#     bzip2 \
#     # ca-certificates \
#     # libglib2.0-0 \
#     # libxext6 \
#     # libsm6 \
#     # libxrender1 \
#     git \
#     # mercurial \
#     # subversion \
#     # zsh \
#     # openssh-server \
#     # gcc \
#     # g++ \
#     # libatlas-base-dev \
#     # libboost-dev \
#     # libboost-system-dev \
#     # libboost-filesystem-dev \
#     curl \
#     make \
#     unzip \
#     ffmpeg \
#     file \
#     xz-utils \
#     sudo \
#     python3 \
#     python3-pip

# RUN apt-get autoremove -y && apt-get clean

# COPY requirements.txt /tmp/

# # For pytorch
# RUN pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

# RUN pip install --no-cache-dir -U pip setuptools wheel \
#     && pip install --no-cache-dir -r /tmp/requirements.txt


ARG python_image_v="python:3.7.14-buster"
FROM ${python_image_v}

WORKDIR /workspace

RUN apt-get -y update
RUN apt-get -y upgrade

# Install ffmpeg
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

# install opencv
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

# install gnu time
RUN apt-get install time

# Install essential packages
Run apt-get install --no-install-recommends -y curl build-essential 

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get install -y git

################
# Install pandoc
################

RUN apt-get install -y pandoc

EXPOSE 8000
EXPOSE 8080

# COPY pyproject.toml .
# RUN pip install poetry
# RUN poetry install
# RUN rm pyproject.toml

COPY requirements.txt /tmp/

# For pytorch
RUN pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

RUN pip install --no-cache-dir -U pip setuptools wheel \
    && pip install --no-cache-dir -r /tmp/requirements.txt