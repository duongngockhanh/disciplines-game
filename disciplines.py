import cv2
import numpy as np
import time

np.random.seed(1234)

height, width = 640, 1080
number_choices = 16
flash_time = 0.2
name_window = "Disciplines Game"
disciplines_path = "disciplines.txt"
disciplines = []

with open(disciplines_path) as f:
    for line in f:
        disciplines.append(line.strip())

number_choices = len(disciplines)
grid_size = int(np.ceil(np.sqrt(number_choices)))

img = np.zeros((height, width), np.uint8)

grid_unit_width = int(width/grid_size)
grid_unit_height = int(height/grid_size)

# draw lines
for i_line in range(1, grid_size):
    x, y = grid_unit_width * i_line, grid_unit_height * i_line
    cv2.line(img, (x, 0), (x, height), (255,))
    cv2.line(img, (0, y), (width, y), (255,))

# start to choose randomly
while True:
    chosen_index = np.random.randint(0, number_choices)
    chosen_text = disciplines[chosen_index]
    font = cv2.FONT_HERSHEY_COMPLEX
    text_size = cv2.getTextSize(chosen_text, font, 1, 2)[0]
    x_text = int((grid_unit_width - text_size[0]) / 2)
    y_text = int((grid_unit_height + text_size[1]) / 2)

    cv2.rectangle(img, (grid_unit_width * 1, grid_unit_height * 1), (grid_unit_width * 2, grid_unit_height * 2), (255,), thickness=-1)
    cv2.putText(img, chosen_text, (grid_unit_width * 1 + x_text, grid_unit_height * 1 + y_text), font, 1, (0,), 2, cv2.LINE_AA)
    cv2.putText
    cv2.imshow(name_window, img)
    time.sleep(flash_time)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    cv2.rectangle(img, (grid_unit_width * 1 + 1, grid_unit_height * 1 + 1), (grid_unit_width * 2 - 1, grid_unit_height * 2 - 1), (0,), thickness=-1)
    cv2.imshow(name_window, img)
    time.sleep(flash_time)
    cv2.waitKey(25)

cv2.waitKey(0)
cv2.destroyAllWindows()