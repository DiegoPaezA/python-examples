"""
Now we will look at how to pass data from one process to another. Here is a very simple 
example where we pass a int from process 0 to process 1:

The code to run this example is:

mpirun -n 4 python p2p_int.py

"""
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    idata = 1
    comm.send(idata, dest=1)
elif rank == 1:
    idata = comm.recv(source=0)
    print('On process 1, data is ',idata)