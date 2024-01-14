FROM debian:11.8

# Install minimal dependencies
RUN apt-get update && apt-get install -y \
    ansible \
    python3

# Install required packages (from ansible role "install-packages")
RUN apt-get update && apt-get install -y \
    gdisk \
    kpartx \
    dosfstools \
    e2fsprogs \
    gnupg \
    qemu-utils \
    python3-lxml \
    grub-efi-amd64 \
    grub-efi-amd64-bin \
    grub-common \
    isolinux \
    python3-requests \
    rsync \
    unzip \
    zlib1g-dev \
    squashfs-tools \
    xorriso \
    build-essential

# Install not required dependencies
RUN apt-get install -y \
    git \
    mc \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Make build directory
RUN mkdir -p /home/build
WORKDIR /home/build
