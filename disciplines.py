import cv2
import numpy as np
import time

np.random.seed(1234)

height, width = 640, 1080 # revise directly
flash_time = 0.05 # revise directly
name_window = "Disciplines Game"
FONT = cv2.FONT_HERSHEY_COMPLEX_SMALL
disciplines_path = "disciplines.txt" # revise directly
disciplines = []

with open(disciplines_path) as f:
    for line in f:
        disciplines.append(line.strip())

np.random.shuffle(disciplines)
number_choices = len(disciplines)
grid_size = int(np.ceil(np.sqrt(number_choices)))

# create a black image
img = np.zeros((height, width), np.uint8)

# calculate grid unit
grid_unit_width = int(width/grid_size)
grid_unit_height = int(height/grid_size)

# draw lines
def draw_line():
    for i_line in range(0, grid_size + 1):
        x, y = grid_unit_width * i_line, grid_unit_height * i_line
        cv2.line(img, (x, 0), (x, height), (255,))
        cv2.line(img, (0, y), (width, y), (255,))

def calculate_grid_coor(index):
    w_index = index % grid_size
    h_index = int(index / grid_size)
    return w_index, h_index

def calculate_pixel_coor(text):
    text_size = cv2.getTextSize(text, FONT, 1, 2)[0]
    x_text = int((grid_unit_width - text_size[0]) / 2)
    y_text = int((grid_unit_height + text_size[1]) / 2)
    return x_text, y_text
    
def draw_rec_put_text(rec_color, text, w_index, h_index, x_text, y_text):
    cv2.rectangle(img, 
                  (grid_unit_width * w_index + 1, grid_unit_height * h_index + 1), 
                  (grid_unit_width * (w_index + 1) - 1, grid_unit_height * (h_index + 1) - 1), 
                  (rec_color,), 
                  thickness=-1)
    cv2.putText(img, text, 
                (grid_unit_width * w_index + x_text, grid_unit_height * h_index + y_text), 
                FONT, 1, 
                (255 - rec_color,), 
                2, cv2.LINE_AA)

# create default texts
def create_default_text():
    for i_index in range(number_choices):
        w_index_default, h_index_default = calculate_grid_coor(i_index)
        default_text = disciplines[i_index]
        x_text, y_text = calculate_pixel_coor(default_text)
        draw_rec_put_text(0, default_text, w_index_default, h_index_default, x_text, y_text)

# start to choose randomly
def main():
    used_rand = None
    while True:
        # choose the index of the text in the 'disciplines' list, 
        # so that the results of 2 consecutive choices are not repeated.
        chosen_index = np.random.randint(0, number_choices)
        if chosen_index == used_rand:
            chosen_index = np.random.randint(0, number_choices)
        used_rand = chosen_index

        # determine the grid coordinates of the choice
        w_index, h_index = calculate_grid_coor(chosen_index)

        # determine the name and the pixel relative coordinates of the choice
        chosen_text = disciplines[chosen_index]
        x_text, y_text = calculate_pixel_coor(chosen_text)
        
        # choose by drawing white rectangle and put text
        draw_rec_put_text(255, chosen_text, w_index, h_index, x_text, y_text)
        cv2.imshow(name_window, img)
        time.sleep(flash_time)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        # unchoose by drawing black rectangle and put text
        draw_rec_put_text(0, chosen_text, w_index, h_index, x_text, y_text) 
        cv2.imshow(name_window, img)
        time.sleep(flash_time)
        cv2.waitKey(1)

if __name__ == "__main__":
    draw_line()
    create_default_text()
    main()
    cv2.waitKey(0)
    cv2.destroyAllWindows()