from mpi4py import MPI
import numpy as np
import time as time

class TaskMPI():
    def __init__(self):
        
        self.comm = MPI.COMM_WORLD
        self.size = self.comm.Get_size()
        self.num_workers = self.size - 1
        
    def __call__(self):
        
        self.send_data(generation=1)
        
        # Master does its own work...
        """
        code: master work
        """
        pop_size = self.size

        evaluations = np.zeros(shape=(pop_size,))
        
        # Master starts receiving results...
        self.receive_data(results=evaluations)
        
        return evaluations


    def send_data(self, generation=0):
        """ Send data to dest with tag.

        Args:
            data: data to send.
        """
        requests = [None] * self.num_workers
        decoded_nets = list(range(0,self.size))
        print(f"decoded_nets: {decoded_nets}, shape: {len(decoded_nets)}")
        
        for worker in range(1, self.size):
            id_num = f'{generation}_{worker}'
            print(f"Sending data to worker {worker} with id {id_num}")
            time.sleep(1)
            args = {'id_num': id_num,
                    'net_list': decoded_nets[worker]}

            requests[worker - 1] = self.comm.isend(args, dest=worker, tag=11)
            
    def receive_data(self, results):
        """ Receive data from all workers.

        Args:
            results: ndarray that will store all results.

        Returns:
            modified ndarray containing the received results.
        """

        requests = [self.comm.irecv(source=i, tag=10) for i in range(1, self.size)]

        while not all(r is None for r in requests):
            for i in range(self.num_workers):
                if requests[i] is not None:
                    check_result = requests[i].test()
                    if check_result[0]:
                        print(f'Worker {i+1} done!')
                        results[i+1] = check_result[1]
                        requests[i] = None


        return results