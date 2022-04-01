import time

import cvzone
from snake import Snake

snake = Snake()


class ScoreBoard:
    """
    This class instantiate the ScoreBoard object and manage its attributes and actions
    """

    def __init__(self):
        self.score = 0
        self.still_playing = True

    def score_board(self, img):
        """
        Shows up the updated score on the screen
        :return: score
        """
        cvzone.putTextRect(img, f"{self.score}", [50, 50], scale=3, thickness=3, offset=10,
                           colorR=(0, 0, 0), colorT=(255, 0, 0))

    def game_over(self, img):
        """
        Stops the current game, shows up the final score
        """
        cvzone.putTextRect(img, f"Game Over!", [300, 400], scale=5,
                           thickness=5, offset=20, colorR=(255, 0, 0), colorT=(255, 255, 255))
        cvzone.putTextRect(img, f"Your score is {self.score}", [300, 500], scale=3,
                           thickness=3, offset=20, colorR=(255, 0, 0), colorT=(255, 255, 255))

    def reset_game(self):
        """
        Resets the Snake, its parameters and the score
        """
        self.score = 0
        snake.points = []
        snake.segments = []
        snake.current_length = 0
        snake.maximum_length = 200
