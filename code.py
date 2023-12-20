import cv2
import numpy as np

img = cv2.imread('image.png', 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)

cimg = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))

    # Sort circles based on x-coordinate
    circles_sorted = sorted(circles[0, :], key=lambda x: x[0])

    # Create an array to store colors
    ball_colors = []

    for i, circle in enumerate(circles_sorted):
        center = (circle[0], circle[1])
        radius = circle[2]

        # Extract the color from the center pixel
        color = img[center[1], center[0]]

        # Convert BGR to RGB
        color = (int(color[2]), int(color[1]), int(color[0]))

        # Append the color to the array
        ball_colors.append(color)

        # Draw the circle with its color
        cv2.circle(img, center, radius, color, 5)
        cv2.putText(img, f'Ball {i + 1}', (center[0] - 20, center[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the image with circles and colors
    # cv2.imshow('Image with Colors', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Display the extracted colors in sequential order from left to right
    print("Colors of balls in sequential order (left to right):")
    for i, color in enumerate(ball_colors, start=1):
        if color[2] > color[1] and color[2] > color[0]:
            print("blue")
        else:
            print("red")
else:
    print('No circles detected.')
