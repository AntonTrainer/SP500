class Owl(object):
    def __init__(self):
        pass

    def _only_use_inside_the_class(self):
        pass

    def no_underscore_means_anything_can_use(self):
        self._only_use_inside_the_class()
        pass

owl = Owl()
owl.no_underscore_means_anything_can_use()