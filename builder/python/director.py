from builder.python.builder import Builder

class Director:
    def construct_car(self, builder: Builder):
        builder.set_engine()
        builder.set_color()
        builder.set_tires()