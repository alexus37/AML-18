# AML-18
Repo for the advanced machine learning class at ETH Autumn semester 2018

## Required software
1. [Pycharm Professional](https://www.jetbrains.com/pycharm/): Python IDE used for development and debugging.
2. [Anaconda3](https://www.anaconda.com/download/): Python Data Science Platform, used for the Conda environment variables.

## Setting up the environment
After installing the required software, you must setup the environment. This can be done by one of these two methods:
### Importing an environment
This will create the new conda environment "aml" and install all the required software.
#### Linux (CPU)
Import the [environment.yml](../blob/master/environment.yml). To do so open a terminal and type the following command 
 
```
conda env create -f environment.yml
```
### Activating the environment
To install new libraries or modify the environment you must first activate the environment.
#### Linux
Launch a terminal, and issue this command
```
conda activate aml
```

### Jupyter-notebook
If you want to use the environment in the a notebook as a kernel run:
```
python -m ipykernel install --user --name aml --display-name "Python3 (aml)"
```

### Installing new libraries
After activating the environment in a terminal in Linux, or the Anaconda prompt in Windows, you can install new packages by issuing this command
```
conda install <package name>
```

### Changing the PyCharm interpreter
The steps are almost the same for Linux and Windows:
1. Open the project folder *AML* in PyCharm
2. Go to "**File>Settings**"
3. From the tabs on the left select "**Project:AML**" then **Project Interpreter**
4. Click on the **Gear** symbol (Settings) next to the list of available interpreters, and then **Add...**
5. In the pop-up window, select "**Existing environment**", then the "**...**" button next to the "**interpreter**" list.
6. Navigate to the location of the new conda environment you created, by default it is located in (/home/<USER>/Anaconda3/bin/python) for Linux and (C:\Users\<USER>\Anaconda3\python.exe) for Windows.

This should make Pycharm use the conda environment we created called **aml** for this project.

## Running the project
First, load the projects environment, you can do so through PyCharm or using the terminal (Anaconda prompt for Windows):  
```
conda activate aml
cd /path/to/project
```