import random
import cv2


class Food:
    """
    This class instantiate the food object and manages all its attributes and actions
    """

    def __init__(self, food_path):
        # the parameter is to leave the transparency of the png file unchanged
        self.food_image = cv2.imread(food_path, cv2.IMREAD_UNCHANGED)
        self.height, self.width, _ = self.food_image.shape  # we don't want the chanels, hence the _
        self.food_location = 0, 0
        # this method is called right from the beginning so the location is never "0, 0"
        self.random_food_location()

    def random_food_location(self):
        """
        This simple method selects random coordinates for the food location
        The range are the width and heigth of the window in pixels minus the marging you want to leave
        :return: new food location
        """
        self.food_location = random.randint(100, 1000), random.randint(100, 600)

