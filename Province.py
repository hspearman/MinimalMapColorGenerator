class Province:
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color
    def __del_color(self):
        del self._color

    # Color of the province
    _color = property(get_color, set_color, __del_color)

    def get_neighbors(self):
        return self._color
    def __set_neighbors(self, neighbors):
        self._neighbors = neighbors
    def __del_neighbors(self):
        del self._neighbors

    # List of provinces that share a border with this province
    _neighbors = property(get_neighbors, __set_neighbors, __del_neighbors)

    def get_visited(self):
        return self._visited
    def __set_visited(self, visited):
        self._visited = visited
    def __del_visited(self):
        del self._visited

    # Flags whether or not this node has been visited
    _visited = property(get_visited, __set_visited, __del_visited)

    def __init__(self):
        self._visited = False