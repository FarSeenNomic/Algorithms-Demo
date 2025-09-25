#Andres Ugalde

#Open widow for the project

import pygame as pg
import pygame_gui
import matplotlib 
import time
import sys
import random


# Creating the start window
pg.init()
width, height = 1200, 700
screen = pg.display.set_mode((width, height)) #Seting the screen size
pg.display.set_caption("Algo Project") #Window Name

#Setting clock
clock = pg.time.Clock()

#Holds the algorithms chosen by the user in "algo name": algoFunction() key pairs
algo_list = {}

#Setting GUI Maneger 
manager = pygame_gui.UIManager((width, height))


#Define colors
white = (255, 255, 255)
black = (0, 0, 0)
lightBlue = (173, 216, 230)

#Project Tile
project_title = pygame_gui.elements.UILabel(relative_rect=pg.Rect((500, 10), (200, 25)), text="Sorting Algorithm Visualizer", manager=manager, object_id="#project_title")

#Input Instructions
input_title = pygame_gui.elements.UILabel(
    relative_rect=pg.Rect((10, 75), (400, 25)),  # Position and size
    text="Input a list of numbers seperated by commas",
    manager=manager
    )


#List Input
List_Input = pygame_gui.elements.UITextEntryBox(relative_rect=pg.Rect((50, 100), (700, 100)), manager=manager, object_id="#list_input")

# Generate List instructions
list_Instructions = pygame_gui.elements.UILabel(relative_rect=pg.Rect((50, 225), (700, 25)), text="You can generate a list of number by inputing the size and which type you want by pressing the button",manager=manager, object_id="#list_instruction" )

#Set Generate list lenght size input
list_Size = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((50, 250), (100, 25)),placeholder_text="List size: ", manager = manager, object_id="#list_size_input")

# Create the randomly generated list button
random_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((200, 250), (100, 25)), text="Random", manager=manager, object_id="#random_button")

# Create the randomly generated sorted list button
sorted_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((350, 250), (100, 25)), text="Sorted", manager=manager, object_id="#sorted_button")

#Creating all the Sorting option check boxs
# Bubble Sort
check_bubble_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((50, 400), (25, 25)), text="Bubble sort", manager=manager, object_id="#option_bubble_sort")

# Insertion Sort
check_insertion_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((50, 450), (25, 25)), text="Insertion Sort", manager=manager, object_id="#option_insertion_sort")

# Merge Sort
check_merge_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((50, 500), (25, 25)), text="Merge Sort", manager=manager, object_id="#option_merge_sort")

# Quick Sort
check_quick_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((50, 550), (25, 25)), text="Quick Sort", manager=manager, object_id="#option_quick_sort")

# Heap Sort
check_heap_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((50, 600), (25, 25)), text="Heap Sort", manager=manager, object_id="#option_heap_sort")

# Counting Sort
check_counting_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((300, 400), (25, 25)), text="Counting Sort", manager=manager, object_id="#option_counting_sort")

# Radix Sort
check_radix_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((300, 450), (25, 25)), text="Radix Sort", manager=manager, object_id="#option_radix_sort")

# Bucket Sort
check_bucket_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((300, 500), (25, 25)), text="Bucket Sort", manager=manager, object_id="#option_bucket_sort")

# Quick Select Sort
check_quickSelect_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((300, 550), (25, 25)), text="Quick Select Sort", manager=manager, object_id="#option_quickSelect_sort")

# Binary Search Sort
check_binarySearch_sort = pygame_gui.elements.UICheckBox(relative_rect=pg.Rect((300, 600), (25, 25)), text="Binary Search Sort", manager=manager, object_id="#option_binarySearch_sort")

# The Start Button for the Visualtion
start_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((750, 600), (150, 25)), text="Start Sorting", manager=manager, object_id="#start_button")

# Random List generate
def randomList(size):
    if isinstance(size, int) :
        randList = [random.randint(0, 1000) for _ in range(size)]
        return randList
    else:
        return 0






#Setting Star Window
def StartWindow():
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
                        current_list = randomList(int(entered_size)) #Creats the random list
                        List_Input.set_text(str(current_list)) # Sets the random list to be displayed in the text box
                        pg.display.flip()
                # The Sorted Button is pressed
                if event.ui_object_id == "#sorted_button":
                    entered_size = list_Size.get_text()
                    if entered_size:
                        current_list = randomList(int(entered_size)) # Makes a random list
                        current_list.sort() # Has the random list sorted from lowest to highest
                        print(current_list)
                        List_Input.set_text(str(current_list)) # Sets the list to be displayed in the textbox
                        pg.display.flip()
                # The Start button is pressed 
                if event.ui_object_id == "#start_button":
                    entered_list = List_Input.get_text() # Gets the list input 
                    if entered_list:
                        print("works")
                        # viusual algo
            # When a box is checked it adds the sorting algorithm to the algo list
            if event.type == pygame_gui.UI_CHECK_BOX_CHECKED:
                if event.ui_object_id == "#option_bubble_sort":
                    algo_list["Bubble Sort"] = "Bubble sort algo"
                if event.ui_object_id == "#option_insertion_sort":
                    algo_list["Insertion Sort"] = "Insertion Sort algo"
                if event.ui_object_id == "#option_merge_sort":
                    algo_list["Merge Sort"] = "Merge sort algo"
                if event.ui_object_id == "#option_quick_sort":
                    algo_list["Quick Sort"] = "Quick Sort algo"
                if event.ui_object_id == "#option_heap_sort":
                    algo_list["Heap Sort"] = "Heap sort algo"
                if event.ui_object_id == "#option_counting_sort":
                    algo_list["Counting Sort"] = "Counting Sort algo"
                if event.ui_object_id == "#option_radix_sort":
                    algo_list["Radix Sort"] = "Radix Sort algo"
                if event.ui_object_id == "#option_bucket_sort":
                    algo_list["Bucket Sort"] = "Bucket Sort algo"
                if event.ui_object_id == "#option_quickSelection_sort":
                    algo_list["Quick Select Sort"] = "Quick Select sort algo"
                if event.ui_object_id == "option_binarySearch_sort":
                    algo_list["Binary Search Sort"] = "Binary Search Sort algo"
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
                if event.ui_object_id == "#option_quickSelection_sort":
                    del algo_list["Quick Select Sort"]
                if event.ui_object_id == "option_binarySearch_sort":
                    del algo_list["Binary Search Sort"]


            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)

        screen.fill(white)

        manager.draw_ui(screen)

        pg.display.flip()

# Setting up randomw Button

StartWindow()
