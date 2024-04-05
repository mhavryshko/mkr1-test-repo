def read_population_data(filename):
    """
    Reads population data from a file.

    Parameters:
    filename (str): The name of the file containing population data.

    Returns:
    list: A list of tuples containing country name, area, and population.
    """
    population_data = []
    with open(filename, 'r') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            population_data.append((country.strip(), float(area.strip()), int(population.strip())))
    return population_data

    
def read_population_data(filename):
    population_data = []
    with open(filename, 'r') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            population_data.append((country.strip(), float(area.strip()), int(population.strip())))
    return population_data


def sort_by_area(population_data):
    return sorted(population_data, key=lambda x: x[1])


def sort_by_population(population_data):
    return sorted(population_data, key=lambda x: x[2])


def main():
    filename = 'text.txt'  # Assuming the file is named 'text.txt' now
    population_data = read_population_data(filename)
    
    sorted_by_area = sort_by_area(population_data)
    sorted_by_population = sort_by_population(population_data)
    
    print("Sorted by area:")
    for country, area, population in sorted_by_area:
        print(f"{country}: area - {area} km², population - {population}")
    
    print("\nSorted by population:")
    for country, area, population in sorted_by_population:
        print(f"{country}: area - {area} km², population - {population}")


if __name__ == "__main__":
    main()
