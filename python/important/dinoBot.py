import pyautogui
from PIL import ImageGrab
import time


def isCollide(data):
    for i in range(300,500):
        for j in range(300,400):
            if data[i, j] < 100:
                pyautogui.keyDown("down")
                return

    for i in range(300, 500):
        for j in range(400,500):
            if data[i, j] < 100:
                pyautogui.keyDown("up")
                return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 1 seconds")
    time.sleep(1)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # Draw the rectangle for cactus
        for i in range(300, 500):
            for j in range(400,500):
                data[i, j] = 0

        # Draw the rectangle for birds
        for i in range(300,500):
            for j in range(300,400):
                data[i, j] = 171

        image.show()
        break
