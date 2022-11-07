# trial_1 = {"Bob", "Charley", "Georgia", "John"}
# trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}
#
# check_set = trial_1.intersection(trial_2)
# print(check_set)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)

mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)
