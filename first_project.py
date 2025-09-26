#Andres Ugalde
#Open widow for the project

import time
import sys
import random
import json
import pygame_gui
import matplotlib.pyplot as ply
import pygame as pg
import algorithms

# Creating the start window
pg.init()
width, height = 1200, 700
screen = pg.display.set_mode((width, height)) # Seting the screen size
pg.display.set_caption("Algorithms Project") # Window Name

# Setting clock
clock = pg.time.Clock()

# Holds the algorithms chosen by the user in "algo name": algoFunction() key pairs
algo_list = {}

# Setting GUI Maneger
manager = pygame_gui.UIManager((width, height))

# Define colors
white = (255, 255, 255)
#black = (0, 0, 0)
#light_blue = (173, 216, 230)

# Project Tile
project_title = pygame_gui.elements.UILabel(relative_rect=pg.Rect((500, 10), (200, 25)), text="Sorting Algorithm Visualizer", manager=manager, object_id="#project_title")

# Input Instructions
input_title = pygame_gui.elements.UILabel(
    relative_rect=pg.Rect((10, 75), (510, 25)),  # Position and size
    text="Input a list of numbers seperated by commas and begins and starts with []",
    manager=manager
    )

# List Input
List_Input = pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((50, 100), (700, 100)), manager=manager, object_id="#list_input")

# Generate List instructions
list_Instructions = pygame_gui.elements.UILabel(relative_rect=pg.Rect((50, 225), (700, 25)), text="You can generate a list of number by inputing the size and which type you want by pressing the button",manager=manager, object_id="#list_instruction" )

# Set Generate list lenght size input
list_Size = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((50, 250), (100, 25)),placeholder_text="List size: ", manager = manager, object_id="#list_size_input")

# Create the randomly generated list button
random_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((200, 250), (100, 25)), text="Random", manager=manager, object_id="#random_button")

# Create the randomly generated sorted list button
sorted_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((350, 250), (100, 25)), text="Sorted", manager=manager, object_id="#sorted_button")

# Creating all the sorting option check boxes
for position, name, option in [
    [(50, 400), "Bubble sort", "#option_bubble_sort"],
    [(50, 450), "Insertion Sort", "#option_insertion_sort"],
    [(50, 500), "Merge Sort", "#option_merge_sort"],
    [(50, 550), "Quick Sort", "#option_quick_sort"],
    [(50, 600), "Heap Sort", "#option_heap_sort"],
    [(300, 400), "Counting Sort", "#option_counting_sort"],
    [(300, 450), "Radix Sort", "#option_radix_sort"],
    [(300, 500), "Bucket Sort", "#option_bucket_sort"],
    [(300, 550), "Quick Select Sort", "#option_quickSelect_sort"],
]:
    pygame_gui.elements.UICheckBox(relative_rect=pg.Rect(position, (25, 25)), text=name, manager=manager, object_id=option)

# The Start Button for the Visualtion
start_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((750, 600), (150, 25)), text="Start Sorting", manager=manager, object_id="#start_button")

# Random List generate
def random_list(size):
    try:
        return [random.randint(0, 1000) for _ in range(size)]
    except TypeError:
        return []

def time_complexity(sorting_algorithm, target):
    start = time.perf_counter()
    sorting_algorithm(target)
    end = time.perf_counter()
    time_delta = end - start
    time_delta *= 1000
    return round(time_delta, 6)

def cull_str(li, length=1000):
    return str(li[:length])

# Setting Star Window
def start_window():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # Checks to see if a button is pressed
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # The Random list button is pressed
                if event.ui_object_id == "#random_button":
                    entered_size = list_Size.get_text() # Gets the text input inside of the input box
                    # Only runs if these is a text input in the box
                    if entered_size:
                        current_list = random_list(int(entered_size)) # Creats the random list
                        List_Input.set_text(cull_str(current_list)) # Sets the random list to be displayed in the text box
                        pg.display.flip()
                # The Sorted Button is pressed
                if event.ui_object_id == "#sorted_button":
                    entered_size = list_Size.get_text()
                    if entered_size:
                        current_list = random_list(int(entered_size)) # Makes a random list
                        current_list.sort() # Has the random list sorted from lowest to highest
                        print(f"{current_list=}")
                        List_Input.set_text(cull_str(current_list)) # Sets the list to be displayed in the textbox
                        pg.display.flip()
                # The Start button is pressed
                if event.ui_object_id == "#start_button":
                    entered_list = List_Input.get_text() # Gets the list input
                    if entered_list:
                        #r = algorithms.sorts
                        temp_list = json.loads(entered_list)
                        temp_algo = {}
                        for key, value in algo_list.items():
                            temp_algo[key] = time_complexity(value, temp_list.copy())
                        algo_names = list(temp_algo.keys())
                        algo_times = list(temp_algo.values())
                        ply.figure(figsize=(10, 6))
                        ply.bar(algo_names, algo_times, color="skyblue")

                        ply.xlabel("Sorting Algorithms")
                        ply.ylabel("Time Complexity (milliseconds)")
                        ply.title(f"Sorting Algorithm Preformance For a List of {entered_size}")
                        ply.xticks(rotation=45)
                        ply.tight_layout()
                        ply.show()

            # When a box is checked it adds the sorting algorithm to the algo list
            if event.type == pygame_gui.UI_CHECK_BOX_CHECKED:
                if event.ui_object_id == "#option_bubble_sort":
                    algo_list["Bubble Sort"] = algorithms.bubble_sort
                if event.ui_object_id == "#option_insertion_sort":
                    algo_list["Insertion Sort"] = algorithms.insertion_sort
                if event.ui_object_id == "#option_merge_sort":
                    algo_list["Merge Sort"] = algorithms.mergesort
                if event.ui_object_id == "#option_quick_sort":
                    algo_list["Quick Sort"] = algorithms.quicksort
                if event.ui_object_id == "#option_heap_sort":
                    algo_list["Heap Sort"] = algorithms.heapsort
                if event.ui_object_id == "#option_counting_sort":
                    algo_list["Counting Sort"] = algorithms.counting_sort
                if event.ui_object_id == "#option_radix_sort":
                    algo_list["Radix Sort"] = algorithms.radix_sort_py
                if event.ui_object_id == "#option_bucket_sort":
                    algo_list["Bucket Sort"] = algorithms.bubble_sort
                if event.ui_object_id == "#option_quickSelect_sort":
                    algo_list["Quick Select Sort"] = algorithms.selection_sort
            # When the checkbox is uncheck it removes the algorithm from the algolist
            if event.type == pygame_gui.UI_CHECK_BOX_UNCHECKED:
                if event.ui_object_id == "#option_bubble_sort":
                    del algo_list["Bubble Sort"]
                if event.ui_object_id == "#option_insertion_sort":
                    del algo_list["Insertion Sort"]
                if event.ui_object_id == "#option_merge_sort":
                    del algo_list["Merge Sort"]
                if event.ui_object_id == "#option_quick_sort":
                    del algo_list["Quick Sort"]
                if event.ui_object_id == "#option_heap_sort":
                    del algo_list["Heap Sort"]
                if event.ui_object_id == "#option_counting_sort":
                    del algo_list["Counting Sort"]
                if event.ui_object_id == "#option_radix_sort":
                    del algo_list["Radix Sort"]
                if event.ui_object_id == "#option_bucket_sort":
                    del algo_list["Bucket Sort"]
                if event.ui_object_id == "#option_quickSelect_sort":
                    del algo_list["Quick Select Sort"]

            manager.process_events(event)
        manager.update(UI_REFRESH_RATE)
        screen.fill(white)
        manager.draw_ui(screen)
        pg.display.flip()

if __name__ == '__main__':
    start_window()
