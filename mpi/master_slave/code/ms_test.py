""" 
    Master-slave example using MPI.
"""
from mpi4py import MPI
import time
import taskmpi


#import tensorflow as tf

def send_stop_signal(comm):
    """ Helper function for master to send a stop message to workers, so they can finish their
        work and stop waiting for messages.

    Args:
        comm: MPI.COMM_WORLD.
    """

    for worker in range(1, comm.Get_size()):
        comm.send('stop', dest=worker, tag=11)


def master(comm):
    """ Master function -> run the evolution and send parameters of evaluation task to workers.

    Args:
        args: dict with command-in-line parameters.
        comm: MPI.COMM_WORLD.
    """
    task_test = taskmpi.TaskMPI() # Initialize task
    results = task_test() # Send data to workers and receive results
    
    print("Master does its own work...")
    time.sleep(2)
    results[0] = 10
    print(f"Master Results: {results}")
    
    send_stop_signal(comm)


def slave(comm):
    """ Worker function -> in a loop: waits for parameters from master, trains a network and
        send the results back;

    Args:
        comm: MPI.COMM_WORLD.
    """

    def check_stop():
        """ Check if message is a *stop* message to end task."""

        if type(params) == str:
            if params == 'stop':
                return True

    while True:
        # Waits for master to send parameters
        params = comm.recv(source=0, tag=11)
        print(f"Worker {comm.Get_rank()} received params: {params}")

        if check_stop():
            # If master sends stop message, end things up.
            break
        print(f"Worke {comm.Get_rank()} is working...")
        time.sleep(1)
        results = params['net_list']
        # Send results back to master.
        comm.send(results, dest=0, tag=10)


def main():

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        master(comm)
    else:
        slave(comm)


if __name__ == '__main__':
    main()