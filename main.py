import sys
from hc_io import read, write
from hc_algorithms import createSlides, sortImages, matchVerticals

if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit(1)

    filename = sys.argv[1]

    images, tags = read("in/" + filename)

    verticals = [x for x in images if x.orientation == "V"]
    horizontals = [x for x in images if x.orientation == "H"]

    verticals.sort(key=sortImages)
    horizontals.sort(key=sortImages)

    slides = createSlides(verticals) + createSlides(horizontals)

    write("out/" + filename, slides)
