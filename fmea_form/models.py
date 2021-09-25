from django.db import models

occurance_choices=(
    (10,"More than once per day"),
    (9,"Once every 3-4 days"),
    (8,"Once Every week"),
    (7,"Once every month"),
    (6,"Once every 3 months"),
    (5,"Once every 6 months"),
    (4,"Once every 9 months"),
    (3,"Twice a year"),
    (2,"Once a Year"),
    (1,"Once every 1 - 3 years"), 
)

class FmeaRegister(models.Model):
    process = models.CharField(max_length=200)
    preparedBy = models.CharField(max_length=200)
    responsible= models.CharField(max_length=200)
    date = models.DateField()
    revisedDate=models.DateField()

    def __str__(self):
        return self.process
    


class FmeaProcess(models.Model):
    fmeaRegister= models.ForeignKey(FmeaRegister, on_delete=models.CASCADE)
    processStep= models.CharField(max_length=300)
    processType=models.CharField(max_length=300,null=True)
    potentialFaliureMode= models.CharField(max_length=300)
    potentialFailureEffect= models.CharField(max_length=300)
    severity = models.IntegerField(default=0)
    potentialCause= models.CharField(max_length=300)
    occurence = models.IntegerField(choices=occurance_choices,default=0)
    currentControls= models.CharField(max_length=300)
    detection = models.IntegerField(default=0)
    #rpn = models.IntegerField(default=0)
    actionRecommended= models.CharField(max_length=300)
    responsiblePerson= models.CharField(max_length=200)
    actionTaken= models.CharField(max_length=300)

    def __str__(self):
        return self.processStep
    
    @property
    def rpn(self):
        return self.severity*self.occurence*self.detection

