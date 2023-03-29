'''
Broadcasting a numpy array using the Bcast method (again note the capital B). 
Here we will modify the point-to-point code from broadcasting_p2p.py to instead broadcast the 
array data to all processes in the communicator (rather than just from process 0 to 1):

Run the code with:
mpirun -n 4 python broadcast_all.py

'''
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # create a data array on process 0
    # in real code, this section might
    # read in data parameters from a file
    numData = 10  
    data = np.linspace(0.0,3.14,numData)  
else:
    numData = None

# broadcast numData and allocate array on other ranks:
numData = comm.bcast(numData, root=0)
if rank != 0:    
    data = np.empty(numData, dtype='d')  

comm.Bcast(data, root=0) # broadcast the array from rank 0 to all others

print('Rank: ',rank, ', data received: ',data)