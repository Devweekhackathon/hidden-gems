import random


def compute_gems(points, num_gems):
    gems = []
    # For each requested gem, fetch a pair of adjacent points from points list and place a gem randomly between them
    for _ in range(num_gems):
        # Find two points between which to place the gem
        start_index = random.randrange(len(points)-1)
        start = points[start_index]
        finish = points[start_index+1]

        # Pick the point of the gem
        lat_diff = finish['lat'] - start['lat']
        lng_diff = finish['lng'] - start['lng']
        interspace_position = random.random()       # Pick the gem position 0-1, 0 being start and 1 being finish
        gem_pos = {
            'lat': start['lat'] + lat_diff * interspace_position,
            'lng': start['lng'] + lng_diff * interspace_position
        }

        # Add gem to the gems list
        gems.append(gem_pos)

    return gems


