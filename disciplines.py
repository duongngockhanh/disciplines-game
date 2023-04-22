import cv2
import numpy as np
import time

np.random.seed(1234)

height, width = 640, 1080
flash_time = 0.05
name_window = "Disciplines Game"
disciplines_path = "disciplines.txt"
disciplines = []

with open(disciplines_path) as f:
    for line in f:
        disciplines.append(line.strip())

np.random.shuffle(disciplines)
number_choices = len(disciplines)
grid_size = int(np.ceil(np.sqrt(number_choices)))

img = np.zeros((height, width), np.uint8)

grid_unit_width = int(width/grid_size)
grid_unit_height = int(height/grid_size)

# draw lines
for i_line in range(0, grid_size + 1):
    x, y = grid_unit_width * i_line, grid_unit_height * i_line
    cv2.line(img, (x, 0), (x, height), (255,))
    cv2.line(img, (0, y), (width, y), (255,))

# start to choose randomly
used_rand = None
while True:
    chosen_index = np.random.randint(0, number_choices)
    if chosen_index == used_rand:
        chosen_index = np.random.randint(0, number_choices)
    used_rand = chosen_index
    w_index = chosen_index % grid_size
    h_index = int(chosen_index / grid_size)
    chosen_text = disciplines[chosen_index]
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    text_size = cv2.getTextSize(chosen_text, font, 1, 2)[0]
    x_text = int((grid_unit_width - text_size[0]) / 2)
    y_text = int((grid_unit_height + text_size[1]) / 2)

    cv2.rectangle(img, 
                  (grid_unit_width * w_index, grid_unit_height * h_index), 
                  (grid_unit_width * (w_index + 1), grid_unit_height * (h_index + 1)), 
                  (255,), 
                  thickness=-1)
    cv2.putText(img, chosen_text, 
                (grid_unit_width * w_index + x_text, grid_unit_height * h_index + y_text), 
                font, 1, (0,), 2, cv2.LINE_AA)
    cv2.putText
    cv2.imshow(name_window, img)
    time.sleep(flash_time)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    cv2.rectangle(img, 
                  (grid_unit_width * w_index + 1, grid_unit_height * h_index + 1), 
                  (grid_unit_width * (w_index + 1) - 1, grid_unit_height * (h_index + 1) - 1), 
                  (0,), thickness=-1)
    cv2.putText(img, chosen_text, 
                (grid_unit_width * w_index + x_text, grid_unit_height * h_index + y_text), 
                font, 1, (255,), 2, cv2.LINE_AA)
    cv2.imshow(name_window, img)
    time.sleep(flash_time)
    cv2.waitKey(1)

cv2.waitKey(0)
cv2.destroyAllWindows()