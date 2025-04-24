from django.db import models

# Create your models here.

# Schema:Lead
# fields:first_name,last_name,email,
        #phone,dob,gender,qualifiaction,
        # course,passout_year,course_mode,source,
        #status,follow_up_date
       


class Lead(models.Model):

    first_name=models.CharField(max_length=200)

    last_name=models.CharField(max_length=200)

    email=models.CharField(max_length=200,unique=True)

    phone=models.CharField(max_length=15,unique=True)

    dob=models.CharField(max_length=18)#[](){1,2,3}{k:v}

    GENDER_OPTIONS=(
        ("male","male"),
        ("female","female")

    )

    gender=models.CharField(max_length=200,choices=GENDER_OPTIONS,default="male")

    qualification=models.CharField(max_length=200)

    COURSE_OPTIONS=(
        ("django","django"),
        ("testing","testing"),
        ("datascience","datascience"),
        ("machine learning","machine learning"),
        ("java spring","java spring"),
        ("asp.net","asp.net"),
        ("flutter","flutter")
    )

    course=models.CharField(max_length=200,choices=COURSE_OPTIONS,default="django")

    passout_year=models.CharField(max_length=200)

    COURSE_MODE_OPTIONS=(
        ("online","online"),
        ("offline","offline"),
        ("hybrid","hybrid")
    )

    course_mode=models.CharField(max_length=200,choices=COURSE_MODE_OPTIONS,default="offline")

    SOURCE_OPTIONS=(
        ("website","website"),
        ("socialmedia","socialmedia"),
        ("referral","referral"),
        ("walkin","walkin"),
        ("education fair","education fair"),
        ("adv","adv")
    )

    source=models.CharField(max_length=200,choices=SOURCE_OPTIONS,default="website")

    STATUS_OPTIONS=(
        ("new","new"),
        ("qualified","qualified"),
        ("unqualified","unqualified"),
        ("proceed to admission","proceed to admission")
     
    )
    status=models.CharField(max_length=200,choices=STATUS_OPTIONS,default="new")


    follow_up_date=models.CharField(max_length=200)

    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.first_name+self.last_name