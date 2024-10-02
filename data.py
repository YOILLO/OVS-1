import copy
import random
from random import shuffle

size = 7

repeat = 30

circle = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

square = [[0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0]]

triangle = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0]]

def print_image(img):
    global size

    print("-------")
    for x in range(size):
        for y in range(size):
            if img[x][y]:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print("-------")

def copy_img(img):
    return copy.deepcopy(img)

def rand_coord():
    global size

    return random.randint(0, size - 1)

def add_noise(img, count):
    for _ in range(count):
        x = rand_coord()
        y = rand_coord()

        img[x][y] = 0 if img[x][y] else 1

    return img

def move_copy(img, dx, dy):
    global size

    img_copy = copy_img(img)

    for x in range(size):
        for y in range(size):
            img_copy[x][y] = 0 if x + dx < 0  or y + dy < 0 or x + dx >= size  or y + dy >= size else img[x + dx][y + dy]

    return img_copy

def generate_dataset(max_noize):
    global repeat, size, circle, square, triangle

    circle_moved = [copy_img(circle)]
    square_moved = [copy_img(square)]
    triangle_moved = [copy_img(triangle)]

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            circle_moved.append(move_copy(circle, dx, dy))
            square_moved.append(move_copy(square, dx, dy))
            triangle_moved.append(move_copy(triangle, dx, dy))

    circles = []
    squares = []
    triangles = []

    for i in range(max_noize):
        for _ in range(repeat):
            for img in circle_moved:
                circles.append(add_noise(copy_img(img), i + 1))

            for img in square_moved:
                squares.append(add_noise(copy_img(img), i + 1))

            for img in triangle_moved:
                triangles.append(add_noise(copy_img(img), i + 1))

    circles_pair = [(img, [1, 0, 0]) for img in circles]
    squares_pair = [(img, [0, 1, 0]) for img in squares]
    triangles_pair = [(img, [0, 0, 1]) for img in triangles]

    return circles_pair + squares_pair + triangles_pair

def what_figure(arr):
    if arr[0] > arr[1] and arr[0] > arr[2]:
        return "circle"
    if arr[1] > arr[0] and arr[1] > arr[2]:
        return "square"
    return "triangle"