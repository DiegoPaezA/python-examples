""" 
    Master-slave example using MPI.
"""
from mpi4py import MPI
import taskmpi
from cnn import train
from cnn.utils import load_CIFAR10
import helper_functions as hf

#import tensorflow as tf

def send_stop_signal(comm):
    """ Helper function for master to send a stop message to workers, so they can finish their
        work and stop waiting for messages.

    Args:
        comm: MPI.COMM_WORLD.
    """

    for worker in range(1, comm.Get_size()):
        comm.send('stop', dest=worker, tag=11)


def master(comm, train_data, test_data, num_classes):
    """ Master function -> run the evolution and send parameters of evaluation task to workers.

    Args:
        args: dict with command-in-line parameters.
        comm: MPI.COMM_WORLD.
    """
        
    # Load nets and params
    nets = hf.load_nets("cnn_nets/cnn_nets.yml")
    params = hf.load_params("cnn_nets/cnn_params.yml")
    
    # Initialize task
    task_test = taskmpi.TaskMPI()
    # Send data to workers and receive results
    results = task_test(train_data, test_data, num_classes, nets, params)
    print(f"Results: {results}")
    
    send_stop_signal(comm)


def slave(comm, train_data, test_data, num_classes):
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

        if check_stop():
            # If master sends stop message, end things up.
            break
        #print(f"Worker {comm.Get_rank()} is working...")
        actual_worker = comm.Get_rank()
        #time.sleep(1)
        results = train.calculate_fitness(train_data, test_data, num_classes, params['net_list'], params['params'], actual_worker)
        #results = 1
        # Send results back to master.
        comm.send(results, dest=0, tag=10)

def main():
    
    # Load Data
    num_classes = 10
    train_data, test_data = load_CIFAR10("cifar-10-batches-py")
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        master(comm, train_data, test_data, num_classes)
    else:
        slave(comm, train_data, test_data, num_classes)


if __name__ == '__main__':
    main()