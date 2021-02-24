# Shopping Cart (Python)
(README file was adapted from Professor Rossetti's instructions on a previous assignment)

This is the third deliverable of this course, consisting of a grocery store program.

## Prerequisites

  + Anaconda 3.7
  + Python 3.8
  + Pip

## Installation

Fork this [remote repository](https://github.com/kristina-y/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.8 # (first time only)
conda activate shopping-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired tax rate. In the example below, the New York tax rate of 0.0875 is used:

```sh
touch .env
echo TAX_RATE=0.0875 >> .env
```

Note that instead of 0.0875, you may enter your state's tax rate.

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the  script:

```py
python shopping_cart.py
```

