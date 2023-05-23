# MPI Working with Master - Slave

This example shows how to use MPI to implement a master-slave pattern. The master process is responsible for distributing the work to the slave processes. The master process is also responsible for collecting the results from the slave processes.


1. Build the image with the following command: `docker build -t mpitest .`
2. Run the image with the following command: 
   1. `docker run --name mstest -it mpitest`
   2. Cluster: `docker run -it --rm  --gpus all  --name mstest mpitest`
   
3. Access the container while running with the following command: `docker exec -it mstest bash` 


The container runs the `run.sh` script, running the `mpirun` command to start the MPI processes. The `mpirun` command will start the master process and the slave processes. The master process will distribute the work to the slave processes. The slave processes will perform the work and send the results back to the master process. The master process will collect the results and print them to the screen.
