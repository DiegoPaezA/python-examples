#!/bin/sh
echo "Running master_slave example"
mpirun -n 4 -mca orte_base_help_aggregate 0 -mca btl_base_warn_component_unused 0 python3 ms_test.py

#python3 tf_test.py

# Run the script in an infinite loop
echo "Work done, running forever"
while true; do
    sleep 1
done