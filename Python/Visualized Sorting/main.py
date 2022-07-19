import random
from matplotlib import pyplot as plt

"""
========== Sorting Algorithms - Python Visualizer ==========
Version 1.0.0 - Notes

A very primitive algorithm visualizer. Currently, the following methods have 
been implemented to be used in a demo teaching session.

1. Insertion Sort
2. Selection Sort
3. Bubble Sort
4. Graph Visualizer (Using matplotlib)
5. Randomized Inputs := 1 <= x <= 1000
============================================================
"""


def generate_inputs() -> list:
    input_mapping = []
    # You can change the number of entries to generate...
    # I find that 25 is a good value to test with, however.
    num_elements = int(input("> Number of elements to generate / sort: "))
    while len(input_mapping) < num_elements:
        generator = random.randint(1, 1000)
        if generator not in input_mapping:
            input_mapping.append(generator)
    return input_mapping


def configure_visual(sorting: str, indices: list, array: list) -> None:
    plt.cla()
    plt.title("{} Sorting Algorithm - Visualization".format(sorting))
    plt.style.use("seaborn")
    plt.xlabel("Index Position")
    plt.ylabel("Index Value")
    plt.grid(False)
    plt.bar(indices, array)
    plt.pause(0.0001)


def insertion_sort(array: list) -> None:
    indices = list(range(0, len(array)))
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            temp_val = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp_val
            j = j - 1
            configure_visual("Insertion", indices, array)
    plt.show()


def selection_sort(array: list) -> None:
    indices = list(range(0, len(array)))
    for i in range(0, len(array) - 1):
        configure_visual("Selection", indices, array)
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        if min_index != i:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
    plt.show()


def bubble_sort(array: list) -> None:
    indices = list(range(0, len(array)))
    for i in range(1, len(indices)):
        for j in range(0, len(indices) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
        configure_visual("Selection", indices, array)
    plt.show()


print("=========== Sorting Visualizer ===========")
print("Version 1.0.0")
print("Select a sorting algorithm to visualize:")
print("1) Insertion Sort\n2) Selection Sort\n3) Bubble Sort\n4) TBA")
print("==========================================")

try:
    controller = int(input("> "))

    array_in = generate_inputs()
    if controller == 1:
        insertion_sort(array_in)
    elif controller == 2:
        selection_sort(array_in)
    elif controller == 3:
        bubble_sort(array_in)
    else:
        raise Exception("Error: This has not been implemented yet... TBA")

except ValueError:
    raise Exception("Incorrect Sequence has been sent. Program has now been closed.")


