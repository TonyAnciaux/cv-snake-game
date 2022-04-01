import numpy as np
import math
import cv2


class Snake:
    """
    This class instantiates the Snake object and manages all its attributes and behaviors
    """

    def __init__(self):
        self.current_head = 0, 0  # current coordinates of the head
        self.previous_head = 0, 0  # previous coordinates of the head
        self.points = []  # list of all the coordinates for each point
        self.segments = []  # list of all the segments between each points
        self.current_length = 0  # sum of the lengths of each segment
        self.maximum_length = 200  # starting length, will increase with each food eaten

    def update(self, img, head):
        """
        This method will update the new position of the head, the list of points
        and the length of the Snake object
        :param img: window/webcam object
        :param head: current coordinates object of the head (ex.: tip index landmark)
        :return: updated window/webcam frame
        """
        self.current_head = head
        current_x, current_y = self.current_head
        previous_x, previous_y = self.previous_head

        self.points.append([current_x, current_y])
        distance = math.hypot(current_x - previous_x, current_y - previous_y)
        self.segments.append(distance)
        self.current_length += distance
        self.previous_head = current_x, current_y

        # remove the latest segment of the segment list so to stay under maximum length and "move" the Snake
        if self.current_length > self.maximum_length:
            for i, length in enumerate(self.segments):
                self.current_length -= length
                self.segments.pop(i)
                self.points.pop(i)
                if self.current_length < self.maximum_length:
                    break

        # draw the Snake
        if self.points:
            for i, point in enumerate(self.points):
                # because we don't have a previous point for the first one
                if i != 0:
                    # draws a line between previous point and current point
                    cv2.line(img, self.points[i-1], self.points[i], (255, 0, 0), 15)
                cv2.circle(img, self.points[-1], radius=15, color=(255, 0, 0), thickness=cv2.FILLED)

        return img

    def check_for_collision(self, img):
        """
        Checks if the position of the head is interescting with any of the segments of the snake
        :param img: window/webcam object
        :return: boolean
        """
        # The cv2 polylines method requires first to convert the coordinates in a np.array
        pts = np.array(self.points[:-2], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], isClosed=False, color=(200, 0, 0), thickness=15)
        distance = cv2.pointPolygonTest(pts, self.current_head, measureDist=True)
        if - 1 < distance < 1:
            return True
