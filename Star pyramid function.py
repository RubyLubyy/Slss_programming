# Star pyramid function

def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        print(stars (current_layer))


pyramid(2)
pyramid(3)
pyramid(20)


def pyramid_mirror(num_layers: int) -> None:
    """Print a pyramid mirrored of given number
    of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        # Spaces is equal to total num of layers
        # minus the stars in the current layer
        spaces = " " * (num_layers - current_layer)

        print(spaces + stars(current_layer))


pyramid_mirror(2)
pyramid_mirror(3)
pyramid_mirror(20)