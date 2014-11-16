import random
from Province import Province

hex_color_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
available_colors = []


def main():

    # Initialize provinces
    a = Province("a")
    b = Province("b")
    c = Province("c")
    d = Province("d")
    e = Province("e")
    f = Province("f")
    g = Province("g")
    h = Province("h")

    # Set neighbors
    a.set_neighbors([b, e, d])
    b.set_neighbors([a, c, d, e, f])
    c.set_neighbors([b, f, h])
    d.set_neighbors([a, e, g])
    e.set_neighbors([a, b, d, f, g, h])
    f.set_neighbors([b, c, e, h])
    g.set_neighbors([d, e, h])
    h.set_neighbors([c, f, e, g])

    provinces = [a, b, c, d, e, f, g, h]

    # Run the algorithm
    process_provinces(provinces)

    # Print out the results
    print("Colors of provinces:")
    for province in provinces:
        print(province.get_name() + ": " + province.get_color())
    print("")

    if is_valid_solution(provinces):
        print("Solution is valid!")
    else:
        print("Solution is invalid!")


def process_provinces(provinces):

    # loop through provinces
    for province in provinces:
        calculate_color(province)


def calculate_color(province):

        # If we already calculate the color, return it
        visited = province.get_visited()
        if visited:
            return province.get_color()

        # Otherwise, calculate it
        else:
            province.set_visited(True)

            colors_of_neighbors = []

            # Get the colors of the province's neighbors
            neighbors = province.get_neighbors()
            for neighbor in neighbors:
                colors_of_neighbors.append(calculate_color(neighbor))

            # Choose a color that no neighboring province use
            for color in available_colors:
                if color not in colors_of_neighbors:
                    province.set_color(color)

            # If no unique color is available, generate a new one
            if None == province.get_color():
                color = generate_color()
                province.set_color(color)
                available_colors.append(color)

            return province.get_color()


def is_valid_solution(provinces):

    is_valid = True

    max_neighbors = 0

    # Loop through all the provinces
    for province in provinces:
        province_color = province.get_color()

        neighbors = province.get_neighbors()
        num_of_neighbors = len(neighbors)
        if num_of_neighbors > max_neighbors:
            max_neighbors = num_of_neighbors

        # Make sure each province doesn't have the same color as any bordering provinces
        for neighbor in neighbors:
            if neighbor.get_color() == province_color:
                is_valid = False
                break

    return is_valid


def generate_color():
    return "#" + ''.join(random.sample(hex_color_characters, 6))

main()