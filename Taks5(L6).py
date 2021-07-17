class Stationary:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}))")


class Pen(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pencil(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} pencill!")


class Marker(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")

stat = Stationary()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencill = Pencil("Faber")
pencill.draw()
marker = Marker("Edding")
marker.draw()


