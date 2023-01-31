import cv2

# Open the video file
cap = cv2.VideoCapture("video.mp4")

# Get the first frame
_, first_frame = cap.read()
gray_first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

while True:
    # Read the current frame
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the current frame and the first frame
    diff = cv2.absdiff(gray_first_frame, gray_frame)

    # Threshold the difference image
    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Show the difference image
    cv2.imshow("Difference", diff)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
