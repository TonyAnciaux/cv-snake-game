import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

from score import ScoreBoard
from snake import Snake
from food import Food


def main():
    """
    The main function of the game
    """
    score = ScoreBoard()
    snake = Snake()
    food = Food("becode_logo_75.png")

    # Creates the window object
    webcam = cv2.VideoCapture(0)
    webcam.set(3, 1280)
    webcam.set(4, 720)

    # Creates the HandDetector object
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    while score.still_playing:
        success, main_img = webcam.read()
        main_img = cv2.flip(main_img, 1)
        hands, img = detector.findHands(img=main_img, flipType=False, draw=True)

        if hands:
            landmark = hands[0]["lmList"]
            tip_index = landmark[8][0:2]  # we only need coordinates for x and y, not z
            if snake.check_for_collision(main_img):
                score.game_over(main_img)
            else:
                snake.update(main_img, tip_index)

        # We'll need both coordinates to divide them by two so the middle of the food image gets the coordinates
        # In order to detect properly when the Snake eats the food
        current_x, current_y = snake.current_head
        random_x, random_y = food.food_location
        if random_x - food.width // 2 < current_x < random_x + food.width // 2 \
                and random_y - food.height // 2 < current_y < random_y + food.height // 2:
            food.random_food_location()
            snake.maximum_length += 50
            score.score += 1

        main_img = cvzone.overlayPNG(main_img, food.food_image, (random_x - food.width // 2, random_y - food.height // 2))
        score.score_board(main_img)

        cv2.imshow("Snake Game", main_img)
        key = cv2.waitKey(1)
        # Resets the game when pressing "r" on keyboard
        if key == ord("r"):
            score.reset_game()
            main()


if __name__ == "__main__":
    main()
