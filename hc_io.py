from hc_objects import Image


def readTags(tags, tag_container):

    for tag in tags:
        if tag in tag_container:
            tag_container[tag] += 1
        else:
            tag_container[tag] = 1

    return tag_container


def read(filename):
    file = open(filename, "r")

    _ = int(file.readline())
    images = []
    tags = {}

    for index, line in enumerate(file.readlines()):
        args = line.replace("\n", "").split(" ")
        tags = readTags(args[1:], tags)
        images.append(Image(index, args[0], int(args[1]), args[1:]))

    return images, sorted(tags, key=tags.get, reverse=True)


def write(filename, slides):
    file = open(filename, "w")

    file.write(str(len(slides)) + "\n")
    for slide in slides:

        image_ids = ""
        for image in slide.images:
            image_ids += str(image.id) + " "

        file.write(image_ids[:-1] + "\n")
