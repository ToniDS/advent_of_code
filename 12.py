from aocd import Puzzle
import itertools

moons = ["<x=-1, y=0, z=2>", "<x=2, y=-10, z=-7>", 
 "<x=4, y=-8, z=8>", "<x=3, y=5, z=-1>"]

moons = ["<x=-8, y=-10, z=0>","<x=5, y=5, z=10>", "<x=2, y=-7, z=3>", 
         "<x=9, y=-8, z=-3>"]
moons_pos = []

puzzle = Puzzle(year=2019, day = 12)
data = puzzle.input_data

moons = data.split("\n")


initial_pos = {}
names = [0, 1, 2, 3]
for i, element in enumerate(moons):
    x = int(element.split(",")[0].split("=")[1])
    y = int(element.split(",")[1].split("=")[1])
    z = int(element.split(",")[2].split("=")[1][:-1])
    initial_pos[names[i]] = (x, y, z)
    

#one idea: parallelization/multithreading + write to sql
# no jupyter

#other idea: 
# dictionary of vectors => dictionary of planets => lists of positions

moon_velocity = []
initial_velocity = {}
for moon in names: 
    initial_velocity[moon] = (0,0,0)
moon_velocity.append(initial_velocity)
first_step = []

def calculate_difference(initial, planet1, planet2):
    vel_difference = []
    for i in range(len(initial[planet1])):
        if initial[planet1][i] < initial[planet2][i]:
            vel_difference.append(1)
        if initial[planet1][i] == initial[planet2][i]:
            vel_difference.append(0)
        if initial[planet1][i] > initial[planet2][i]:
            vel_difference.append(-1)
    return tuple(vel_difference)

def calculate_total_velocity(velocities, planet1, velocities_now):
    """ What is velocities?, what is velocities_t?"""
    velocity = []
    for j in range(3):
        vel = (velocities[planet1][0][j] + velocities[planet1][1][j] +
        velocities[planet1][2][j] + velocities_now[planet1][j])
        velocity.append(vel)
    return tuple(velocity)
    
def calculate_position(position, velocity):
    positions = {}
    for planet in position.keys():
        pos_values = []
        for i in range(3):
            pos = position[planet][i] + velocity[planet][i]
            pos_values.append(pos)
        positions[planet] = tuple(pos_values)
    return positions

def write_to_dict(moon_dict, moon, pos, step):
    try:
        moon_dict[pos][moon].append(step)
    except:
        moon_dict[pos] = {0: (), 
                          1: (),
                          2: (),
                          3: ()}
        moon_dict[pos][moon].append(step)

            


def main(initial_pos):
    all_velocities = {}
    all_positions = {}
    moon_velocity = {}
    
    for moon in names: 
        moon_velocity[moon] = (0,0,0)
        write_to_dict(all_velocities, moon, (0,0,0), 0)
        wri
        try: 
            all_velocities[moon_velocity[moon]][moon].append(0)
        except:
            all_velocities[moon_velocity[moon]] = {0: (),
                                                   1: (), 
                                                   2: (),
                                                   3: ()}            
            all_velocities[moon_velocity[moon]][moon].append(0)

        try: 
            all_positions[initial_pos[moon]][moon].append(0)
        except: 
            all_positions[initial_pos[moon]][moon] =   {0: [],
                                                   1: [], 
                                                   2: [],
                                                   3: []}
            all_positions[moon_velocity[moon]][moon].append(0)

        
            

    moon_pos = initial_pos
    #print(moons_pos)
    
    step = 0
    dupes = False
    while not dupes:
        velocities = {}
        for permutation in itertools.permutations(moon_pos, 2):
            velo = calculate_difference(moon_pos, permutation[0], permutation[1])
            if permutation[0] in velocities.keys():
                velocities[permutation[0]].append(velo)
            else: 
                velocities[permutation[0]] = [velo]
            
        #print(velocities)

        final_velocities = {}
        for moon in initial_pos.keys():
            vel = calculate_total_velocity(velocities, moon, moon_velocity)
            final_velocities[moon] = vel

        moon_velocity = final_velocities
        print(moon_velocity)
        positions = calculate_position(moon_pos, moon_velocity)
        moons_pos = positions
        for moon in names: 
            try: 
                all_velocities[moon_velocity[moon]][moon].append(step)
            except:
                all_velocities[moon_velocity[moon]] = {0: (),
                                                   1: (), 
                                                   2: (),
                                                   3: ()}
                all_velocities[moon_velocity[moon]][moon].append(step)
        
            try: 
                all_positions[moon_pos[moon]][moon].append(step)
            except: 
                all_positions[moon_pos[moon]][moon] = {0: (),
                                                   1: (), 
                                                   2: (),
                                                   3: ()}
                all_positions[moon_pos[moon][moon]].append(step)

            #if len(all_positions[moon_pos][moon]]) > 1:
        step += 1
        if step == 10:
            dupes=True

        


        
print(main(initial)[10])

    
    



    
    


