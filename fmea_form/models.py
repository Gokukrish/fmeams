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

severity_choices= [(i,i) for i in range(11)]


status=(
    (1,"Completed"),
    (0,"Incomplete")
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
    processType=models.CharField(max_length=1024,null=True)
    fmeaRegister= models.ForeignKey(FmeaRegister, on_delete=models.CASCADE)
    processStep= models.CharField(max_length=1024)
    potentialFaliureMode= models.CharField(max_length=1024)
    potentialFailureEffect= models.CharField(max_length=1024)
    severity = models.IntegerField(choices=severity_choices,default=0)
    potentialCause= models.CharField(max_length=1024)
    occurence = models.IntegerField(choices=occurance_choices,default=0)
    currentControls= models.CharField(max_length=1024)
    detection = models.IntegerField(choices=severity_choices,default=0)
    #rpn = models.IntegerField(default=0)
    actionRecommended= models.CharField(max_length=1024)
    responsiblePerson= models.CharField(max_length=200)
    actionTaken= models.CharField(max_length=1024)
    reference = models.CharField(max_length=1024,default=None)
    status=models.BooleanField(choices=status,default=0)
    finalSeverity=models.IntegerField(default=0)
    finalOccurence=models.IntegerField(default=0)
    finalDetection=models.IntegerField(default=0)

    def __str__(self):
        return self.processStep
    
    @property
    def rpn(self):
        return self.severity*self.occurence*self.detection
    
    @property
    def finalRPN(self):
        return self.finalSeverity*self.finalOccurence*self.finalDetection

    @property
    def riskLevel(self):
        return self.severity*self.detection