import pakuri as pakuri_module


class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri = []
        print(f"The Pakudex can hold {self.capacity} species of Pakuri.\n")

    def get_size(self):
        return len(self.pakuri)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if len(self.pakuri) == 0:
            return None
        species_name_list = []
        for pakuri in self.pakuri:
            species_name_list.append(pakuri.get_species())
        return species_name_list

    def get_stats(self, species):
        for i in self.pakuri:
            if i.get_species() == species:
                return [i.attack, i.defense, i.speed]
        return None

    def sort_pakuri(self):
        self.pakuri.sort(key=lambda x: x.get_species())

    def add_pakuri(self, species):
        for pakuri in self.pakuri:
            if pakuri.get_species() == species:
                return False
        self.pakuri.append(pakuri_module.Pakuri(species))
        return True

    def evolve_species(self, species):
        for i in self.pakuri:
            if i.species == species:
                i.evolve()
                return True
        return False
