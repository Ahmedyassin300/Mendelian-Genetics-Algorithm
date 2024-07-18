import random

class PlantSpecies:
    def __init__(self, genetic_makeup):
        self.genetic_makeup = genetic_makeup  # List of allele pairs, e.g., [('A', 'a'), ('B', 'b')]

def punnett_square(alleles1, alleles2):
    """Generate possible allele combinations from two allele pairs."""
    return [
        (alleles1[0], alleles2[0]),
        (alleles1[0], alleles2[1]),
        (alleles1[1], alleles2[0]),
        (alleles1[1], alleles2[1])
    ]

def crossover(parent1, parent2):
    """Perform crossover between two parents to produce offspring using Mendelian inheritance."""
    offspring_genetic_makeup = []
    for gene1, gene2 in zip(parent1.genetic_makeup, parent2.genetic_makeup):
        offspring_alleles = random.choice(punnett_square(gene1, gene2))
        offspring_genetic_makeup.append(offspring_alleles)
    return PlantSpecies(offspring_genetic_makeup)

def mutate(plant_species, mutation_rate=0.01):
    """Introduce mutations in the genetic makeup of the species."""
    for i in range(len(plant_species.genetic_makeup)):
        if random.random() < mutation_rate:
            allele_pair = list(plant_species.genetic_makeup[i])
            allele_to_mutate = random.randint(0, 1)
            allele_pair[allele_to_mutate] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            plant_species.genetic_makeup[i] = tuple(allele_pair)

def fitness(plant_species):
    """Evaluate the fitness of the species based on genetic diversity."""
    unique_alleles = set()
    for alleles in plant_species.genetic_makeup:
        unique_alleles.update(alleles)
    return len(unique_alleles)

def hybridize_and_mutate(parent1, parent2, mutation_rate=0.01):
    """Hybridize two parent species and apply mutation."""
    offspring = crossover(parent1, parent2)
    mutate(offspring, mutation_rate)
    return offspring

# Example usage
parent1 = PlantSpecies([('A', 'c'), ('v', 'N'), ('o', 'B')])
parent2 = PlantSpecies([('O', 'Q'), ('n', 'M'), ('S', 'G')])

# Create offspring through hybridization and mutation
offspring = hybridize_and_mutate(parent1, parent2)

print(f"Parent 1: {parent1.genetic_makeup}")
print(f"Parent 2: {parent2.genetic_makeup}")
print(f"Offspring: {offspring.genetic_makeup}")
print(f"Offspring Fitness: {fitness(offspring)}")
