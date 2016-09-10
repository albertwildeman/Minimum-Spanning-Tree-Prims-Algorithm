from FileReadLib import get_array
from PrimsAlgorithmLib import prim
# from GreedySchedulerLib import greedy_scheduler

# Calculates optimal scheduling using two greedy algorithms, only one on of which is correct.
edges = get_array("edges")

mst_cost = prim(edges)

print("Cost of MST: " + str(mst_cost))

print("done.")