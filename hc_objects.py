class Image:
    def __init__(self, index, orientation, num_tags, tags):
        self.id = index
        self.orientation = orientation
        self.num_tags = num_tags
        self.tags = tags


class Slide:
    def __init__(self, image1, image2=None):
        self.images = []
        self.tags = []
        self.num_tags = 0

        self.addImage(image1)
        self.addImage(image2)

    def addImage(self, image):
        if image is not None:
            self.images.append(image)
            self.tags = set(list(self.tags) + image.tags)
            self.num_tags = len(self.tags)
