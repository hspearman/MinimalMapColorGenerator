class Province:
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def __del_color(self):
        del self._color

    # Color of the province
    color = property(get_color, set_color, __del_color)

    def get_neighbors(self):
        return self._neighbors

    def set_neighbors(self, neighbors):
        self._neighbors = neighbors

    def __del_neighbors(self):
        del self._neighbors

    # List of provinces that share a border with this province
    neighbors = property(get_neighbors, set_neighbors, __del_neighbors)

    def get_visited(self):
        return self._visited

    def set_visited(self, visited):
        self._visited = visited

    def __del_visited(self):
        del self._visited

    # Flags whether or not this node has been visited
    visited = property(get_visited, set_visited, __del_visited)

    def get_name(self):
        return self._name

    def __set_name(self, name):
        self._name = name

    def __del_name(self):
        del self._name

    # Flags whether or not this node has been visited
    name = property(get_name, __set_name, __del_name)

    def __init__(self, name):
        self.visited = False
        self.name = name
        self.color = None