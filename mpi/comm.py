"""
Our first MPI for python example will simply import MPI from the mpi4py package, create a communicator and get the rank of each process:

Run the script with the following command:

mpirun -n 4 python comm.py

-n 4 means that we want to run 4 processes in parallel (the number of processes can be any number, 
but it must be the same as the number of processes in the script)

MPI process rank
Each process has a unique rank, i.e. an integer identifier, within a. communicator. The rank value 
is between 0 and #procs-1. The rank value is used to distinguish one process from another.

https://www.uio.no/studier/emner/matnat/ifi/INF3380/v11/undervisningsmateriale/inf3380-week06.pdf
"""

from mpi4py import MPI
import os
# instantize the communication world
comm = MPI.COMM_WORLD

# get the size of the communication world
size = comm.Get_size()

# get this particular processes' `rank` ID
rank = comm.Get_rank()

PID = os.getpid()

print(f'rank: {rank} has PID: {PID}')

