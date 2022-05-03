import os
import face_recognition

directory = "/home/mahesh/projects/final_year_project/static/uploads"


# print(directory)

# for filename in os.scandir(directory):
#     if filename.is_file():
#         print(filename.path)

        

# for filename in os.listdir(directory):
#     if filename.endswith(".png") or filename.endswith(".py"): 
#          # print(os.path.join(directory, filename))
#         continue
#     else:
#         continue        




user_image = face_recognition.load_image_file( "/home/mahesh/projects/final_year_project/static/uploads/unknown.jpeg" )

biden_encoding = face_recognition.face_encodings(user_image)[0]


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".jpg"):
        if os.path.isfile(f):
            db_image = face_recognition.load_image_file(f)
            unknown_encoding = face_recognition.face_encodings(db_image)[0]
            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            if results[0]:
                print(filename)
            else:
                print("image not matched")    