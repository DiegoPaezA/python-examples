'''
Broadcasting takes a variable and sends an exact copy of it to all processes on a communicator. 

Broadcasting a dictionary: In this example, the dictionary is broadcasted from the root 
process (rank 0) to all other processes point-to-point by using the bcast() function.

Run the code with:
mpirun -n 4 python broadcasting_p2p.py

'''
# Import MPI
from mpi4py import MPI

# Define world
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Create some data in the RANK_0 worker
if rank == 0:
    data = {'key1' : [7, 2.72, 2+3j], 'key2' : ( 'abc', 'xyz')}
else:
    data = None

# Broadcast the data from RANK_0 to all workers
data = comm.bcast(data, root=0)

# Append the RANK ID to the data
data['key1'].append(rank)

# Print the resulting data
print(f"Rank: {rank}, data: {data}")