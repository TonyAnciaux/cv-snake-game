# Snake-Game 
## Description 

Classic Snake Game meets Computer Vision. 

## Installation 

This program is running on python 3.10 and requires the following dependencies:
* OpenCV 
* NumPy
* CVzone
* Random 

In order to function properly, it also requires access to a functionning webcam and a screen with a minimum resolution of 1280*720 pixels. 

## Usage

### Running the game
Once all dependencies installed, open your terminal, go to the directory containing the game and type `python main.py`.
A window should open and the game will start as soon as an index finger is detected through the webcam. 

### Rules of the game 

The Snake follows the Index on the screen. When eating a cookie, the user wins a point. 
If the head of the snake hits its body, the game is over and the final score will display. 
If the finger gets out of the screen or the hand stops being detected, the game is paused and the snake disappears from the screen. 

### Extras

- A `hand_detection.py` file exists in the directory. It just labels the fingers of the last hand appearing on the screen.
- A `face_detection.py` file will, as its name indicate, detect a face seen through the webcam as well as eyes. 
- the `resize_logo.py` is used to conform a png file to 75*75 pixel image used as cookies in the snake game. 


## Future developments
- Highest Score display at the end of the game 
- Detection of border of the screen 
