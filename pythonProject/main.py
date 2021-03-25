
import pyrebase

firebaseConfig = {"apiKey": "AIzaSyCfuQ46q09FozGesUxT3ZakA_7XhGrnrUM",
  "authDomain": "fir-course-56a13.firebaseapp.com",
  "projectId": "fir-course-56a13",
  "storageBucket": "fir-course-56a13.appspot.com",
  "messagingSenderId": "447378702514",
  "appId": "1:447378702514:web:f15e3623cec16a1d3949ab",
  "databaseURL": "https://fir-course-56a13-default-rtdb.firebaseio.com/"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

# auth = firebase.auth()
#
# #SignIn
# email = input("Enter your email.")
# password = input("Enter your password")
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print('hmm thk ase')
# except:
#     print('fuck off')
#
#
# #SignUp
# email = input("Email den")
# password = input("password lekhen ekta")
# confirmpass=input("Abar lekhen password")
# if password==confirmpass:
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         print("Success")
#     except:
#         print("Email ase already eda")

#Storage
# storage = firebase.storage()
# # filename=input("Enter filename you want to upload")
# cloudfilename=input("enter name of the file on the cloud")
#
# # storage.child(cloudfilename).put(filename)
#
# #download
# print(storage.child(cloudfilename).get_url(None))
# storage.child(cloudfilename).download("","xmennn.txt")

#Database
db = firebase.database()
# data = {'age':40,'address':'dhaka','employed':True}
# db.push(data)
# db.child("People").push(data)

#db.child("people").child("-MVIRPe7QGX69B6d1Fby").update({'age':51})
# elapsedtime=db.child("People").child("Abdomen_1").get()
# abdomen=db.child("People").child("Abdomen_1").get()
# print(elapsedtime)


# for person in people.each():
#     print(person.val())
#     print(person.key())
#     if person.val()['address'] == "dhaka":
#        db.child("People").child(person.key()).update({'employed': True})

#Delete
# db.child("people").remove();

#Read

# list1 = []
# people=db.child("People").child(2).child("Abdomen_1").get()
# #print(people.val())

elapsedtime = []
abdomenlist = []

ECG1 = db.child("ECG1").get()

for ecg in ECG1.each():

    ecgkey = ecg.key()

    x = db.child("ECG1").child(ecgkey).child("Elapsed time").get()
    y = db.child("ECG1").child(ecgkey).child("Abdomen_1").get()

    elapsedtime.append(x.val())
    abdomenlist.append(y.val())

print(x,y)


    #print(y.val())
    #list1.append(y.val())

#print(list1)











