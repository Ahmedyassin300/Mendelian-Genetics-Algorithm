# Mendelian-Genetics-Algorithm

# Mendelian Inheritance Algorithm for Plant Science students

This project implements a genetic algorithm to simulate the Mendelian inheritance and hybridization process of Plants species. The algorithm introduces the genetic makeup of two wheat species, performs crossover and mutation to produce the genetic makeup of the offspring, and evaluates the fitness of the resulting hybrid.

## Features

- **Mendelian Inheritance**: Uses principles of Mendelian inheritance to determine the genetic makeup of the offspring.
- **Crossover Mechanism**: Implements a crossover mechanism using a Punnett Square.
- **Mutation Process**: Introduces random mutations to the genetic makeup of the offspring.
- **Fitness Evaluation**: Evaluates the fitness of the offspring based on genetic diversity.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Ahmedyassin300/Menelian-Algorithm.git
    cd Menelian-Algorithm
    ```

2. (Optional) Create a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install any required packages (if any):

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you are in the project directory:

    ```sh
    cd Menelian-Algorithm
    ```

2. Run the genetic algorithm script:

    ```sh
    python wheat_genetic_algorithm.py
    ```

3. The script will output the genetic makeup of the parents and the resulting offspring, along with the fitness of the offspring.

    ```plaintext
    Parent 1: [('A', 'a'), ('B', 'b'), ('C', 'c')]
    Parent 2: [('X', 'x'), ('Y', 'y'), ('Z', 'z')]
    Offspring: [('A', 'x'), ('B', 'y'), ('C', 'z')]
    Offspring Fitness: 6
    ```

## Example

Below is an example of how the genetic algorithm works:

1. Define the genetic makeup of the parent species:

    ```python
    parent1 = PlantSpecies([('A', 'a'), ('B', 'b'), ('C', 'c')])
    parent2 = PlantSpecies([('X', 'x'), ('Y', 'y'), ('Z', 'z')])
    ```

2. Create offspring through hybridization and mutation:

    ```python
    offspring = hybridize_and_mutate(parent1, parent2)
    ```

3. Output the genetic makeup and fitness of the offspring:

    ```python
    print(f"Parent 1: {parent1.genetic_makeup}")
    print(f"Parent 2: {parent2.genetic_makeup}")
    print(f"Offspring: {offspring.genetic_makeup}")
    print(f"Offspring Fitness: {fitness(offspring)}")
    ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss any improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


