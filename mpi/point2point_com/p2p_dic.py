"""
Now we will look at how to pass data from one process to another. Here is a very simple 
example where we pass a dictionary from process 0 to process 1:

The code to run this example is:

mpirun -n 4 python p2p_dic.py

"""

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print('On process 1, data is ',data)