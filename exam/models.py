from django.db import models
import cv2
import datetime 

from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

# class Certificate(models.Model):
#     full_name = models.CharField(max_length=50)
#     language = models.CharField(max_length=50)
#     dt = datetime.datetime.now()

#     # for index,name in enumerate(list_names):
#     template = cv2.imread(r"C:\Users\HP\Downloads\White Minimalist Certificate.jpg")
#     # cv2.putText(template,name,(766,734),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,3,(0,0,255),2,cv2.LINE_AA)
#     cv2.putText(template,full_name,(766,734),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),2,cv2.LINE_AA)
#     cv2.putText(template,str(dt.date()),(250,1172),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),1,cv2.LINE_AA)
#     cv2.putText(template,language,(1238,786),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv2.LINE_AA)
#     cv2.imwrite(f'C:/Users/HP/Downloads/Cer/{full_name}.jpg',template)