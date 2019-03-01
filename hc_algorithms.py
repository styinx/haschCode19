from hc_objects import Slide


def sortImages(i):
    return i.num_tags


def matchVerticals(verticals):
    matched = []

    # smart algorithm

    return matched


def match(slides):
    return slides


def createSlides(images):
    slides = []

    images = iter(images)
    for image in images:

        if image.orientation == "V":
            image2 = next(images, None)
            if image2.orientation == "V":
                slides.append(Slide(image, image2))
            else:
                print("image is not vertical")
                exit(1)

        else:
            slides.append(Slide(image))

    return slides
