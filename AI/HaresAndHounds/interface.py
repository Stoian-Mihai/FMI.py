"""
Starting Template

"""
import arcade
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 350
SCREEN_TITLE = "HaresAndHounds"


class HaresAndHoundsGUI(arcade.Window):
    def __init__(self, width, height, title, game):
        super().__init__(width, height, title)
        self.background = None
        self.hareImage = None
        self.wolfImage = None
        self.resetBtn = None
        self.move = []
        self.game = game
        self.infoText = "Make a move!"
        self.counter = time.time()
        self.elapsedTimeAI = 0
        self.elapsedTimeHuman = 0

    def setup(self):
        # Create your sprites and sprite lists here
        self.background = arcade.load_texture("board.png")
        self.hareImage = arcade.load_texture("hare.png")
        self.wolfImage = arcade.load_texture("wolf.png")
        self.resetBtn = arcade.load_texture("resetbtn.png")

    def clear_screen(self):
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

    def draw_wolf(self, position):
        coords = self.map_matrix_position_to_coords(position)
        coords = self.transform_to_lower_left(coords,SCREEN_HEIGHT,60)
        arcade.draw_lrwh_rectangle_textured(coords[0], coords[1],
                                            60, 60,
                                            self.wolfImage)
    def draw_hare(self, position):
        coords = self.map_matrix_position_to_coords(position)
        coords = self.transform_to_lower_left(coords,SCREEN_HEIGHT,60)
        arcade.draw_lrwh_rectangle_textured(coords[0], coords[1],
                                            60, 60,
                                            self.hareImage)
    def draw_info_text(self):
        arcade.draw_text(self.infoText, 20, 45, arcade.color.BLACK, 12)

    def draw_elapsed_time_Human(self):
        formattedTime = float("{:.2f}".format(self.elapsedTimeHuman))
        arcade.draw_text("Human elapsed time:  " + str(formattedTime), 20, 25, arcade.color.BLACK, 12)

    def draw_elapsed_time_ai(self):
        formattedTime = float("{:.2f}".format(self.elapsedTimeAI))
        arcade.draw_text("Ai elapsed time:  " + str(formattedTime), 20, 5, arcade.color.BLACK, 12)

    def draw_entities(self):
        wolfPositions = self.game.getWolfPositions()
        harePosition = self.game.getHarePositions()
        for pos in wolfPositions:
            self.draw_wolf(pos)
        self.draw_hare(harePosition)
        self.draw_info_text()
        self.draw_elapsed_time_ai()
        self.draw_elapsed_time_Human()

    def on_draw(self):

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        arcade.draw_lrwh_rectangle_textured(400, 20,
                                            50, 50,
                                            self.resetBtn)

        self.draw_entities()

    def on_update(self, delta_time):
        self.draw_entities()

    def check_rest_btn(self, x, y):
        return self.check_if_inside_rectangle((400,20), (x,y), 50)

    def reset_btn_pressed(self):
        self.game.reset()
    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.check_rest_btn(x, y):
            self.reset_btn_pressed()
            self.move = []
            return None
        matrixPosition = self.map_coords_to_matrix_position((x, y))
        self.move.append(matrixPosition)
        if len(self.move) == 2:
            self.make_move(self.move)
            self.move = []

        # print(self.map_coordonates_to_matrix(x,y))
        pass

    def make_move(self, move):
        # Makes a move and checks if the status of the move is possible
        if move[0] != None and move[1] != None:
            print(self.game.getHarePositions())
            print(self.game.ai)
            if self.game.getHarePositions() in move and self.game.ai == "hare":
                self.infoText = "That move is impossible, make a new move!"
                return None
            if move[0] in self.game.getWolfPositions() and self.game.ai == "wolf":
                self.infoText = "That move is impossible, make a new move!"
                return None
            if self.game.movePosition(move[0], move[1]) == -1:
                self.infoText = "That move is impossible, make a new move!"
                return None
            else:
                self.infoText = "Make a move!"
                self.elapsedTimeHuman = time.time() - self.counter
            start_time = time.time()
            self.game.makeAIMove()
            elapsed_time = time.time() - start_time
            self.elapsedTimeAI = elapsed_time
            self.counter = time.time()
            if self.game.checkWin() == "hare":
                self.infoText = "Hare won!!!"
            if self.game.checkWin() == "wolf":
                self.infoText = "Hounds won!!!"

    def check_if_inside_rectangle(self, rectTopLeft, points, rectHeightWidth):
        point = Point(points[0], points[1])
        polygon = Polygon([(rectTopLeft[0], rectTopLeft[1]), (rectTopLeft[0] + rectHeightWidth, rectTopLeft[1]),
                           (rectTopLeft[0] + rectHeightWidth, rectTopLeft[1] + rectHeightWidth),
                           (rectTopLeft[0], rectTopLeft[1] + rectHeightWidth)])
        if polygon.contains(point):
            return True
        return False

    def transform_to_lower_left(self, coords, height=SCREEN_HEIGHT, obj_height=0):
        return (coords[0], height - coords[1] - obj_height)

    def map_coords_to_matrix_position(self, coords):
        if self.check_if_inside_rectangle((20, 120), self.transform_to_lower_left(coords), 60):
            return (1, 0)
        if self.check_if_inside_rectangle((120, 20), self.transform_to_lower_left(coords), 60):
            return (0, 1)
        if self.check_if_inside_rectangle((120, 120), self.transform_to_lower_left(coords), 60):
            return (1, 1)
        if self.check_if_inside_rectangle((120, 220), self.transform_to_lower_left(coords), 60):
            return (2, 1)
        if self.check_if_inside_rectangle((220, 20), self.transform_to_lower_left(coords), 60):
            return (0, 2)
        if self.check_if_inside_rectangle((220, 120), self.transform_to_lower_left(coords), 60):
            return (1, 2)
        if self.check_if_inside_rectangle((220, 220), self.transform_to_lower_left(coords), 60):
            return (2, 2)
        if self.check_if_inside_rectangle((320, 20), self.transform_to_lower_left(coords), 60):
            return (0, 3)
        if self.check_if_inside_rectangle((320, 120), self.transform_to_lower_left(coords), 60):
            return (1, 3)
        if self.check_if_inside_rectangle((320, 220), self.transform_to_lower_left(coords), 60):
            return (2, 3)
        if self.check_if_inside_rectangle((420, 120), self.transform_to_lower_left(coords), 60):
            return (1, 4)
        return None

    def map_matrix_position_to_coords(self, matrixPos):
        if matrixPos == (1, 0):
            return (20, 120)
        if matrixPos == (0, 1):
            return (120, 20)
        if matrixPos == (1, 1):
            return (120, 120)
        if matrixPos == (2, 1):
            return (120, 220)
        if matrixPos == (0, 2):
            return (220, 20)
        if matrixPos == (1, 2):
            return (220, 120)
        if matrixPos == (2, 2):
            return (220, 220)
        if matrixPos == (0, 3):
            return (320, 20)
        if matrixPos == (1, 3):
            return (320, 120)
        if matrixPos == (2, 3):
            return (320, 220)
        if matrixPos == (1, 4):
            return (420, 120)

        return None


def interfacePlayPVP(gameState):
    game = HaresAndHoundsGUI(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, gameState)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    pass
