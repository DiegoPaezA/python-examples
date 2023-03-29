'''
An effective way of distributing computationally intensive tasks is to scatter 
pieces of a large dataset to each task. The separate tasks perform some analysis 
on their chunk of data and then the results are gathered by RANK_0.

This example takes a large array of random numbers and splits it into pieces for 
each task. These smaller datasets are analyzed (taking an average in this example) 
and the results are returns to the main task with a Gather call.

Run the code with:
mpirun -n 4 python scattering_gatter.py

'''
# import libraries
from mpi4py import MPI
import numpy as np

# set up MPI world
comm = MPI.COMM_WORLD
size = comm.Get_size() # new: gives number of ranks in comm
rank = comm.Get_rank()

# generate a large array of data on RANK_0
numData = 100000000 # 100milion values each
data = None
if rank == 0:
    data = np.random.normal(loc=10, scale=5, size=numData)

# initialize empty arrays to receive the partial data
partial = np.empty(int(numData/size), dtype='d')

# send data to the other workers
comm.Scatter(data, partial, root=0)

# prepare the reduced array to receive the processed data
reduced = None
if rank == 0:
    reduced = np.empty(size, dtype='d')

# Average the partial arrays, and then gather them to RANK_0
comm.Gather(np.average(partial), reduced, root=0)

if rank == 0:
    print('Full Average:',np.average(reduced))