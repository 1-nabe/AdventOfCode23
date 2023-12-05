import time
import multiprocessing as mp
from functools import partial
import os
import numpy as np

def stringToList(line: str):
    return [int(x) for x in line.split(' ')]

def fillMaps(map_line):
    new_map = map_line.split('\n')
    new_map.pop(0)
    for i in range(len(new_map)):
        new_map[i] = stringToList(new_map[i])
    return sorted(new_map, key=lambda x: x[1])

def findDest(seed: int, to_map):
    for val in to_map:
        source = val[1]
        if source <= seed <= (source + val[2] - 1):
            return val[0] + (seed - source)
    return seed
            
def getSmallestLocationForSeeds(seeds, maps, process_id):
    size = len(seeds)
    for i in range(size):
        for map in maps:
            seeds[i] = findDest(seeds[i], map)
        if i % 1000000 == 0:
            print(f"Thread {process_id}: {i/1000000}/{size/1000000}") # | {((i / size) * 100):.1f}%")
    return min(seeds)

def process_seeds(seeds, maps):
    print(f"Thread {os.getpid()} started")
    process_id = os.getpid()
    before = time.perf_counter()
    smallest_loc = getSmallestLocationForSeeds(seeds, maps, process_id)
    print(f"Thread {process_id} finished: {time.perf_counter() - before:.6f}s")
    return smallest_loc

def process_pairs(pairs):
    seed_arrays = []
    for pair in pairs:
        seed_arrays.append(np.arange(pair[0], pair[0] + pair[1]))
    seeds = np.concatenate(seed_arrays)
    return seeds

def batch_generator(original_array, batch_size):
    start_index = 0
    while start_index < len(original_array):
        end_index = start_index + batch_size
        yield original_array[start_index:end_index]
        start_index = end_index

if __name__ == "__main__":
    f = open('input.txt')
    file = f.read()
    maps = file.split('\n\n')

    # Get the seeds into a list
    seeds = stringToList(maps[0].split(': ')[1])
    #print(getSmallestLocationForSeeds(seeds)) # Smallest location: 173706076

    # Part 2
    seed_range_pairs = list(zip(seeds[::2], seeds[1::2]))
    print("Seed range pairs generated")
    seeds = process_pairs(seed_range_pairs)
    print("Seeds generated")
    batches = batch_generator(seeds, 100_000_000)
    print("Batches generated")

    smallest_locs = []
    before = time.perf_counter()
    filled_maps = [fillMaps(maps[i]) for i in range(1, 8)]
    process_seed_pair_with_maps = partial(process_seeds, maps=filled_maps)
    pool = mp.Pool(mp.cpu_count())
    smallest_locs = pool.map(process_seed_pair_with_maps, batches)
    smallest_locs.sort()
    print(f"Smallest location: {smallest_locs[0]}") # Smallest location: 11611182
    print(f"Time: {time.perf_counter() - before:.6f}s") # Time: 3166.706568s