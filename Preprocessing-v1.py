import cv2
import mediapipe as mp
import numpy as np


def detectHands(image, black_screen):
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

        # the BGR image to RGB.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw the hand annotations on the image.
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    black_screen,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
    return image, black_screen


if __name__ == "__main__":
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    black_screen = np.zeros((height, width, 3))
    while cap.isOpened():
        _, image = cap.read()
        image = cv2.flip(image, 1)

        hand_detection, black_screen = detectHands(image, black_screen)

        cv2.imshow('Hands Recognition', hand_detection)
        cv2.imshow('Black Recognition', black_screen)
        if cv2.waitKey(3) & 0xFF == ord('x'):
            break

    cap.release()
    cv2.destroyAllWindows()
