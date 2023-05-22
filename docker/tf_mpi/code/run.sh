#!/bin/sh
echo "Running master_slave example"
#mpirun -n 4 python3 ms_test.py

python3 tf_test.py

# Run the script in an infinite loop
echo "Work done, running forever"
while true; do
    sleep 1
done