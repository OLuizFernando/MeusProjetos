import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

reconhecimento_facial = mp.solutions.face_detection
reconhecedor_facial = reconhecimento_facial.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    verificador, frame = webcam.read()

    if not verificador:
        break

    lista_rostos = reconhecedor_facial.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)

    cv2.imshow('Reconhecimento Facial', frame)

    if cv2.waitKey(5) == 27:
        break

webcam.release()