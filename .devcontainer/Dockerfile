FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update && \
    apt-get install -y gpg-agent python-is-python3 software-properties-common python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install \
    ocp_vscode==1.2.2 ocp cadquery https://github.com/CadQuery/OCP-stubs/archive/refs/tags/7.7.0.zip
