## Problem: Velocity at t+1 = velocity at t + velocity at t+1
moons = ["<x=-1, y=0, z=2>", "<x=2, y=-10, z=-7>", 
 "<x=4, y=-8, z=8>", "<x=3, y=5, z=-1>"]

moons = ["<x=-8, y=-10, z=0>","<x=5, y=5, z=10>", "<x=2, y=-7, z=3>", 
         "<x=9, y=-8, z=-3>"]
moons_pos = []

puzzle = Puzzle(year=2019, day = 12)
data = puzzle.input_data

moons = data.split("\n")

initial = {}
names = ["Io", "Europa", "Ganymede", "Callisto"]
for i, element in enumerate(moons):
    x = int(element.split(",")[0].split("=")[1])
    y = int(element.split(",")[1].split("=")[1])
    z = int(element.split(",")[2].split("=")[1][:-1])
    initial[names[i]] = (x, y, z)
    
moons_pos.append(initial)

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
            


def main(initial_pos, steps = 100):
    all_velocities = {}
    all_
    moon_velocity = {}
    for moon in names: 
        moon_velocity[moon] = (0,0,0)

    moon_pos = initial_pos
    #print(moons_pos)
    step = 0
    dupes = False
    while dupes == False:
        velocities = {}
        for permutation in itertools.permutations(moon_pos, 2):
            velo = calculate_difference(moon_pos, permutation[0], permutation[1])
            if permutation[0] in velocities.keys():
                velocities[permutation[0]].append(velo)
            else: 
                velocities[permutation[0]] = [velo]
            
        #print(velocities)

        final_velocities = {}
        for planet in initial.keys():
            vel = calculate_total_velocity(velocities, planet, moon_velocity)
            final_velocities[planet] = vel

        moon_velocity = final_velocities
        #print(moon_velocity)
        positions = calculate_position(moon_pos, moon_velocity)
        moons_pos = positions

        step += 1
        

        
            moon_pos_list = moons_pos[step][moon]
            moon_velo_list = moon_velocity[step][moon]
            pot_energy = abs(moon_pos_list[0]) + abs(moon_pos_list[1]) + abs(
                moon_pos_list[2])
            kin_energy = abs(moon_velo_list[0]) + abs(moon_velo_list[1]) + abs(moon_velo_list[2])
            total = pot_energy * kin_energy
            energy += total
        energy_all.append(energy)
    return energy_all

print(main(initial, steps = 1001)[1000])

    
    



    
    


