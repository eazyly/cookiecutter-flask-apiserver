cookiecutter-flask-apiserver
========

[![Build Status](https://drone.ashutoshmishra.net/api/badges/eazyly/cookiecutter-flask-apiserver/status.svg?branch=master)](https://drone.ashutoshmishra.net/eazyly/cookiecutter-flask-apiserver)

Boilerplate for creating Python Flask based API server for production.

# Introduction
This project takes care of the setup and configuration so you can focus on making your service awesome. Scaffolding a project takes seconds and it gives you the essentials of devops and container orchestration, like drone, helm, kubernetes integration to get started. This project aims to get out of your way, and to allow you easily and quickly create web services while providing a solid foundation for your service to mature in the future.

## Features

- Support for RESTful & JSON-RPC services via [Python Eve](http://docs.python-eve.org/en/latest/) & [Python Flask](http://flask.pocoo.org/)
- Support for Web frameworks like [Python Flask](http://flask.pocoo.org/) & [Node.js](https://nodejs.org/en/)
- CI/CD via [Drone.io](https://drone.io)
- [Helm](https://www.helm.sh/) for deployment in [Kubernetes](https://kubernetes.io/)

## Quick Start
Install [cookiecutter](https://github.com/audreyr/cookiecutter):
```bash
pip install cookiecutter
```

Scaffold your project (from [github](https://github.com/eazyly/cookiecutter-flask-apiserver)):
```
cookiecutter gh:eazyly/cookiecutter-flask-apiserver
```
OR (from folder)
```
git clone https://github.com/eazyly/cookiecutter-flask-apiserver.git
cookiecutter cookiecutter-flask-apiserver
```


![scaffolding screencast]()

## Contributing
Want a new feature or find a bug? Submit a Pull Request!
