# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    line_list = line.split()
    star.R = int(line_list[1])
    star.color = line_list[2]
    star.m = float(line_list[3])
    star.x = float(line_list[4])
    star.y = float(line_list[5])
    star.Vx = float(line_list[6])
    star.Vy = float(line_list[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    line_list = line.split()
    planet.R = int(line_list[1])
    planet.color = line_list[2]
    planet.m = float(line_list[3])
    planet.x = float(line_list[4])
    planet.y = float(line_list[5])
    planet.Vx = float(line_list[6])
    planet.Vy = float(line_list[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f %f %f %f %f" % (obj.type.capitalize(),
                                             obj.R, obj.color, obj.m,
                                             obj.x, obj.y, obj.Vx, obj.Vy))

def write_statistics_to_file(output_filename, space_objects, physical_time):
    with open(output_filename, 'a') as out_file:
        for obj in space_objects:
            if obj.type == "planet":
                out_file.write(str(obj.type.capitalize()) + " " + str(obj.x) + " " + str(obj.y) +
                               " " + str(obj.Vx) + " " + str(obj.Vy) + " " + str(physical_time) + "\n")
        out_file.close()

import matplotlib.pyplot as plt

def make_graphs_from_data(output_filename):
    times = []
    radii = []
    velocities = []
    with open(output_filename) as input_file:
        for line in input_file:
            x = float(line.split()[1])
            y = float(line.split()[2])
            vx = float(line.split()[3])
            vy = float(line.split()[4])
            time = float(line.split()[5])
            times.append(time)
            radii.append((x**2+y**2)**0.5)
            velocities.append(((vx**2)+(vy**2))**0.5)
    plt.plot(times, radii, 'b-')
    plt.xlabel('время, с')
    plt.ylabel('расстояние от звезды, м')
    plt.savefig('radii_over_time.png')
    plt.clf()
    plt.plot(times, velocities, 'r-')
    plt.xlabel('время, с')
    plt.ylabel('скорость планеты, м/с')
    plt.savefig('velocities_over_time.png')
    plt.clf()
    plt.plot(radii, velocities, 'g-')
    plt.xlabel('расстояние от звезды, м')
    plt.ylabel('скорость планеты, м/с')
    plt.savefig('velocities_over_radii.png')
    plt.clf()
    print(velocities)
    print(times)



if __name__ == "__main__":
    print("This module is not for direct call!")