from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        super().__init__(name)
        self.set_image(image)

    def can_breathe_fire(self):
        return True
