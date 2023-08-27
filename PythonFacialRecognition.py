# # # import datetime
# # # infile = open("cattleFolder\D3490093 Herd Profile on 200823 (68 animals) (3).csv")

# # # # Get the current date and time
# # # current_date = datetime.datetime.now()
# # # print(current_date)

# # # for line in infile:
# # #     line = line.split(",")
# # #     line = line[4]
# # #     if line == "Date Moved In":
# # #         print("not this one")
# # #     else:
# # #         year = line[6:]
# # #         print(year)
# # #         day = line[:2]
# # #         print(day)
# # #         month = line[3:5]
# # #         print(month)
# # #         inputdate1 = year + "-" + month + "-" + day
# # #         print()

        
        
# # #             # Subtract the two dates
# # #             date_difference = current_date - input_date

# # #         # Print the result
# # #         #print(date_difference)

# # #         # Print the result
# # #         #print(date_difference)


# # import datetime
# # import re


# # # Get today's date
# # today = datetime.date.today()


# # # Create a list of dates
# # infile = open("cattleFolder\D3490093 Herd Profile on 200823 (68 animals) (3).csv")
# # dates = []
# # no_date = []

# # for line in infile:
# #     #line = line.split(",")
# #     print(line)
# # #     if line[4] == "Date Moved In":
# # #         continue
# # #     if line[4] == "":
# # #         number = float(re.sub(r'E\+\d+', '', line[0]))
# # #         no_date.append(number)
# # #     else:
# # #         date = line[4][6:] + "-" + line[4][3:5] + "-" + line[4][:2]
# # #         #print(date)
# # # print(no_date)
# # #print(dates)
    
# #     # if line[4] != "Date Moved In" or line[4] != " ":
# #     #     date = line[4][6:] + "-" + line[4][3:5] + "-" + line[4][:2]
# #     #     dates.append(date)

# # #print(dates)
# # # dates = ['2023-08-22', '2023-08-21', '2023-08-20']
# # # print(dates)
# # # Subtract today's date from each date in the list
# # # days_difference = []
# # # for date in dates:
# # #     print(date)
# # #     if date == "--":
# # #         continue
# # #     date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
# # #     days_difference.append((today - date_object).days)

# # # # Print the list of days difference
# # # print(days_difference)

# import mediapipe as mp
# import cv2

# # Initialize the face detector
# face_detector = mp.solutions.face_detection.FaceDetection()

# # Load the image
# image = cv2.imread('C:\Users\tomca\OneDrive\Documents\WhatsApp Image 2023-08-24 at 14.06.42.jpg')

# # Convert the image to RGB
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Process the image
# faces = face_detector.process(image)

# # Print the number of faces detected
# print(len(faces))

# # Loop over the detected faces
# for face in faces:
#     # Get the bounding box of the face
#     bounding_box = face.bounding_box

#     # Get the face landmarks
#     landmarks = face.landmarks

#     # Draw the bounding box and landmarks on the image
#     cv2.rectangle(image, bounding_box, (0, 255, 0), 2)
#     for landmark in landmarks:
#         cv2.circle(image, landmark, 2, (0, 0, 255), -1)

# # Show the image
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

refernce_img = cv2.imread("cattleFolder\WhatsApp Image 2023-08-24 at 14.06.42.jpg")
refernce_img2 = cv2.imread("cattleFolder\WhatsApp Image 2023-08-24 at 15.07.35.jpg")

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, refernce_img.copy())["verified"]:# or DeepFace.verify(frame, refernce_img2.copy())["verified"]:
            face_match = True
        else:
            face_match = False
    except ValueError:
        pass

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 15 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()    


