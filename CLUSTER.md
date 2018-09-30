# Cluster Usage

## Setup
Connect to ETH through VPN, then you can login to the cluster using you NETHZ username and password.
First, upload the data and code files to the cluster
```angular2html
scp -r -v <data and code folder> <user>@login.leonhard.ethz.ch:data
```
Make sure to rename the data folder to "data" for the code to run correctly.

Then login to the cluster using ```ssh``` and load the required modules
```angular2html
ssh <user>@login.leonhard.ethz.ch
module load python_gpu/3.6.1
```

## Running the code
Run the [preProcessor.py](preProcessor.py) to generate the required numpy files in "data/preprocessingOut/"
```angular2html
bsub -n 8 -R "[mem=8000]" python preProcessor.py  
```
Then use the batch submission system to submit the job 
```angular2html
bsub -W 4:00 -n 8 -R "rusage[mem=8000,ngpus_excl_p=1]" python <file name>.py
```
Options:
- ```W```: maximum time for the job in the format of HH:MM (4 hours in the example above)
- ```n```: number of CPU cores to use (8 in the example above)
- ```R```: resources to use:
	- ```mem``` memory (RAM) in mega bytes per CPU core (8 cores * 8000 MB = 64GB)
	- ```ngpus_excl_p``` number of GPUs to use 
-```I```: interactive mode, this directs the output to 

The regular GPU models used are NVIDIA GTX 1080 with approximately 10GB of dedicated memory. 

## Checking job status
To show the stats of all the jobs you have in queue or running after submission:
```angular2html
bbjobs
``` 
Or, for less information:
```
bjobs
```
To check a jobs output (a job which is not in interactive mode)
```angular2html
bpeek <job ID>
```
After the job finishes execution, it will generate a file in your home directory with the output of the job called ```lsf.<job ID>``` 

To terminate a job
```angular2html
bkill <job ID>
```


## Max resources without having to wait
- Memory: 160 GB
- Cores: 24 Cores
- GPUs: 1 GPU
- Run time: 120 hours

Click [here](https://scicomp.ethz.ch/wiki/Using_the_batch_system) for more information about the batch system and clusters.
