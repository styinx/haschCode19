from hc_objects import Image


def read(filename):
    file = open(filename, "r")

    _ = int(file.readline())
    images = []

    for index, line in enumerate(file.readlines()):
        args = line.split(" ")
        images.append(Image(index, args[0], int(args[1]), args[1:]))

    return images


def write(filename, slides):
    file = open(filename, "w")

    file.write(str(len(slides)) + "\n")
    for slide in slides:

        image_ids = ""
        for image in slide.images:
            image_ids += str(image.id) + " "

        file.write(image_ids[:-1] + "\n")
