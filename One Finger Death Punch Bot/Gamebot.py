import pygetwindow as gw
import pyautogui
import cv2
import numpy as np

def find_window_by_name(window_name):
    try:
        return gw.getWindowsWithTitle(window_name)[0]
    except IndexError:
        return None

def is_image_visible(image_path, window):
    window_region = (window.left, window.top, window.width, window.height)
    screenshot = np.array(pyautogui.screenshot(region=window_region))
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert template to grayscale

    # Apply Gaussian blur to the template
    template = cv2.GaussianBlur(template, (5, 5), 0)

    # Convert screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Use a different matching method (cv2.TM_CCOEFF_NORMED) for better results
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, confidence, _, _ = cv2.minMaxLoc(result)

    print(f"Confidence: {confidence}")  # Add this line for debugging    
    return confidence > 0.86  # Adjust confidence threshold as needed

def press_left_arrow():
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')

def press_right_arrow():
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')

def main():
    window_name = "One Finger Death Punch"
    blue_image_path = "blue.png"
    red_image_path = "red.png"

    while True:
        window = find_window_by_name(window_name)
        if window:
            if is_image_visible(blue_image_path, window):
                print("Blue is visible in the window.")
                press_left_arrow()

            if is_image_visible(red_image_path, window):
                print("Red is visible in the window.")
                press_right_arrow()

        else:
            print(f"Window '{window_name}' not found.")

if __name__ == "__main__":
    main()
