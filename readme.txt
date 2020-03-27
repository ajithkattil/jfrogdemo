##############################################################################

Readme.txt

##############################################################################

This process will deploy a simple Python application to Kubernetes, including :

Creating Python Container image
Publishing the container images to an image registry
Deploying the Python application to Kubernetes

##############################################################################

You will need Docker, kubectl, and this python application :artifact_query.py

1. To install Docker, Kubectl , follow the official documentation
2. Create a requirements.txt file with the name and versions of all Python packages to be installed
( I copied the "pip list" from my laptop to create this , hence too long)
3. Create Docker file for the Python application using docker
