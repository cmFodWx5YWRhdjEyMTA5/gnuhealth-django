from django.db import models

# Create your models here.

class gnuhealth_icu_glasgow(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  evaluation_date = models.DateField()
  glasgow = models.CharField()
  glasgow_eyes = models.CharField()
  glasgow_motor = models.CharField()
  glasgow_verbal = models.CharField()
  name = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_icu_chest_drainage(models.Model):
  id = models.IntegerField()
  air_leak = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  fluid_aspect = models.CharField()
  fluid_volume = models.CharField()
  location = models.CharField()
  name = models.CharField()
  oscillition = models.CharField()
  remarks = models.CharField()
  suction = models.CharField()
  suction_pressure = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_icu_apache2(models.Model):
  id = models.IntegerField()
  aado2 = models.CharField()
  age = models.IntegerField()
  apache_score = models.CharField()
  arf = models.CharField()
  chronic_condition = models.CharField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  fio2 = models.IntegerField()
  gcs = models.CharField()
  heart_rate = models.CharField()
  hematocrit = models.CharField()
  hospital_admission_type = models.CharField()
  mean_ap = models.CharField()
  name = models.CharField()
  paco2 = models.CharField()
  pao2 = models.CharField()
  ph = models.CharField()
  repository_rate = models.IntegerField()
  score_date = models.DateField()
  serum_creatinine = models.CharField()
  serum_potassium = models.CharField()
  serum_sodium = models.CharField()
  temperature = models.IntegerField()
  wbc = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
class gnuhealth_icu_ventilation(models.Model):
  id = models.IntegerField()
  create_date = models.DateField()
  create_uid = models.IntegerField()
  current_mv = models.CharField()
  ett_size = models.IntegerField()
  mv_end = models.CharField()
  mv_start = models.CharField()
  name = models.CharField()
  remarks = models.CharField()
  tracheostomy_size = models.IntegerField()
  ventilation = models.CharField()
  write_date = models.DateField()
  write_uid = models.IntegerField()
  
  
