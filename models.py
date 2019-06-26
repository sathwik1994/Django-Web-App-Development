from django.db import models

# Create your models here.






#create Appuser table
class Appuser(models.Model):
	#uid = models.IntegerField(primary_key=True,editable=False)
	username = models.CharField(max_length = 100)
	email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
	password = models.CharField(max_length=100)

#create Video table
class Video(models.Model):
	#vid = models.IntegerField(primary_key=True,default="", editable=False)
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length=70, null=True, blank=True, unique=True)
	created_ts = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length = 30)
	user_id = models.ForeignKey(Appuser, on_delete=models.CASCADE)
	duration = models.IntegerField()


#create Videolike table
class Videolike(models.Model):
	user_id = models.ForeignKey(Appuser, on_delete=models.CASCADE)
	video_id = models.ForeignKey(Video, on_delete=models.CASCADE)


#create Useradminrelation table
class Useradminrelation(models.Model):
	user_id = models.ForeignKey(Appuser, on_delete=models.CASCADE)



#create Comment table
class Comment(models.Model):
	comment = models.CharField(max_length = 100)
	user_id = models.ForeignKey(Appuser, on_delete=models.CASCADE)
	video_id = models.ForeignKey(Video, on_delete=models.CASCADE)


#create Videoviews table
class Videoviews(models.Model):
	video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
	views = models.IntegerField()

#create Schedule table
class Schedule(models.Model):
	start_ts = models.DateTimeField(auto_now_add=False)
	end_ts = models.DateTimeField(auto_now_add=False)
	video_id = models.ForeignKey(Video, on_delete=models.CASCADE)

#Create Tag table
class Tag(models.Model):
	name = models.CharField(max_length = 100)
		
#Create Videotagrelation table
class Videotagrelation(models.Model):
	user_id = models.ForeignKey(Appuser, on_delete=models.CASCADE)
	tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

#create History table
class History(models.Model):
	user_id = models.ForeignKey(Appuser, on_delete=models.CASCADE)
	schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)

