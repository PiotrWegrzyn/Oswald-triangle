from drawers.table_drawer import TableDrawer
from geometry import Vector
from models.line_info import LineInfo


class Table:
    def __init__(self):
        self.top = 650
        self.bot = 300
        self.height = self.top - self.bot
        self.left = 850
        self.right = 950
        self.width = self.right - self.left
        self.columns = 2
        self.rows = 15
        self.data = [[1, 2] for i in range(self.rows)]

        self.lines = {
            "top": LineInfo(Vector(self.left, self.top, self.right, self.top)),
            "bot": LineInfo(Vector(self.left, self.bot, self.right, self.bot)),
            "right": LineInfo(Vector(self.right, self.top, self.right, self.bot)),
            "left": LineInfo(Vector(self.left, self.top, self.left, self.bot))
        }

    def draw(self, canvas):
        TableDrawer(canvas, self).draw()
