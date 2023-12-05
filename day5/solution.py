import re
import time
import multiprocessing as mp
import threading
from functools import partial
import os
import numpy as np

def findCubes(color: str, line: str) -> int:
    cubeLine = re.findall(r'\b(?:[1-9]|1[0-9]|20)\s' + color + r'\b', line)

def stringToList(line: str):
    return [int(x) for x in line.split(' ')]

def fillMaps(map_line):
    new_map = map_line.split('\n')
    new_map.pop(0)
    for i in range(len(new_map)):
        new_map[i] = stringToList(new_map[i])
    return new_map

def findDest(source: int, to_map):
    for val in to_map:
        if source >= val[1] and source <= (val[1] + val[2] - 1):
            return val[0] + (source - val[1])
    return source
            
def getSmallestLocationForSeeds(seeds, maps):
    size = len(seeds) * 100
    
    for i in range(len(seeds)):
        for map in maps:
            seeds[i] = findDest(seeds[i], map)
        if i % 1000000 == 0:
            print(f"Thread {threading.current_thread().ident}: {i}/{(i / size):.5f}%")
    seeds.sort()
    return seeds[0]

def process_seed_pair(pair, maps):
    process_id = os.getpid()
    before = time.perf_counter()
    new_seeds = []
    new_seeds = np.arange(pair[0], pair[0] + pair[1])
    print(f"Thread {process_id} seeds created: {time.perf_counter() - before:.6f}s")
    smallest_loc = getSmallestLocationForSeeds(new_seeds, maps)
    print(f"Thread {process_id} finished: {time.perf_counter() - before:.6f}s")
    return smallest_loc

if __name__ == "__main__":
    f = open('input.txt')
    file = f.read()
    maps = file.split('\n\n')

    # Get the seeds into a list
    seeds = stringToList(maps[0].split(': ')[1])
    #print(getSmallestLocationForSeeds(seeds)) # 173706076

    # Part 2
    seed_range_pairs = list(zip(seeds[::2], seeds[1::2]))
    print("Seed range pairs: " + str(len(seed_range_pairs)))
    
    smallest_locs = []
    before = time.perf_counter()
    filled_maps = [fillMaps(maps[i]) for i in range(1, 8)]
    process_seed_pair_with_maps = partial(process_seed_pair, maps=filled_maps)
    pool = mp.Pool(mp.cpu_count())
    smallest_locs = pool.map(process_seed_pair_with_maps, seed_range_pairs)
    print(f"Seeds: {smallest_locs}")
    print(f"Size: {sum(smallest_locs)}")
    # smallest_locs.sort()
    # print(f"Smallest location: {smallest_locs[0]}")
    print(f"Time: {time.perf_counter() - before:.6f}s")