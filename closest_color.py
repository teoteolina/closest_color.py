import math

def closest_color(requested_color, colors):
    """Ищет ближайший цвет из заданной палитры colors к заданному цвету requested_color"""
    min_distance = math.inf
    closest_color = None
    for color in colors:
        distance = math.sqrt(sum([(requested_color[i] - color[i]) ** 2 for i in range(3)]))
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    return closest_color

# Пример использования
colors = [
    [255, 0, 0], # красный
    [0, 255, 0], # зеленый
    [0, 0, 255], # синий
    [255, 255, 0], # желтый
    [255, 255, 255], # белый
    [0, 0, 0] # черный
]
requested_color = [192, 192, 192] # серый
closest_color = closest_color(requested_color, colors)
print(closest_color) # [255, 255, 255] - белый
