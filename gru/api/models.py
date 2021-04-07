# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumni(models.Model):
    alumni_id = models.AutoField(primary_key=True)
    name = models.TextField()
    graduation_year = models.IntegerField()
    achievement_description = models.TextField(blank=True, null=True)
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumni'
        ordering = ['name']

    def __str__(self):
        return self.name


class AlumniHas(models.Model):
    alumni_id = models.AutoField(primary_key=True)
    degree_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'alumni_has'


class Award(models.Model):
    sport = models.TextField()
    name = models.TextField()
    award_name = models.TextField()
    year_awarded = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'award'


class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'


class Course(models.Model):
    course_code = models.AutoField(primary_key=True)
    course_number = models.FloatField()
    course_name = models.TextField(blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class CourseTeaching(models.Model):
    course_code = models.AutoField(primary_key=True)
    course_number = models.FloatField()
    prof_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_teaching'


class Degree(models.Model):
    name = models.TextField()
    field = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'degree'


class EntryRequirement(models.Model):
    major_code = models.AutoField(primary_key=True)
    class_name = models.TextField()
    grade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'entry_requirement'


class EquivalentClass(models.Model):
    major_code = models.AutoField(primary_key=True)
    class_name = models.TextField()
    name = models.TextField()
    grade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equivalent_class'


class ExtraCurricularProgram(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'extra_curricular_program'


class ExtracurricularOfferings(models.Model):
    uni_name = models.TextField()
    excurricular_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'extracurricular_offerings'


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculty'


class FieldOfStudy(models.Model):
    prof_id = models.AutoField(primary_key=True)
    field_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'field_of_study'


class GruUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.TextField()
    name = models.TextField(blank=True, null=True)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'gru_user'


class Major(models.Model):
    major_code = models.AutoField(primary_key=True)
    major_name = models.TextField()
    no_of_years = models.IntegerField()
    degree_name = models.TextField(blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major'


class Preference(models.Model):
    pref_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'preference'


class PreferenceContain(models.Model):
    pref_id = models.AutoField(primary_key=True)
    uni_name = models.TextField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'preference_contain'


class PreferredUni(models.Model):
    pref_id = models.AutoField(primary_key=True)
    preferred_uni_name = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'preferred_uni'


class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    rating = models.FloatField(blank=True, null=True)
    name = models.TextField()
    uni_name = models.TextField(blank=True, null=True)
    faculty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'


class Provides(models.Model):
    uni_name = models.TextField(blank=True, null=True)
    degree_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provides'


class Ranking(models.Model):
    uni_code = models.AutoField(primary_key=True)
    best_program = models.TextField(blank=True, null=True)
    rank = models.IntegerField()
    prev_year_rank = models.IntegerField(blank=True, null=True)
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ranking'


class Sport(models.Model):
    sport = models.TextField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'sport'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    position = models.TextField()
    name = models.TextField()
    uni_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class University(models.Model):
    name = models.TextField()
    location = models.TextField()
    description = models.TextField()
    impact_on_industry = models.TextField(blank=True, null=True)
    finances = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university'
