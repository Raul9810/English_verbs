from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=25)
    meaning = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=50)

class Verb(models.Model):
    verb = models.ForeignKey(Word, on_delete = models.CASCADE)

class Adjective(models.Model):
    adjective = models.ForeignKey(Word, on_delete = models.CASCADE)

class Phrasal(models.Model):
    phrasal = models.ForeignKey(Word, on_delete = models.CASCADE)

class Noun(models.Model):
    noun = models.ForeignKey(Word, on_delete = models.CASCADE)

class Adverb(models.Model):
    adverb = models.ForeignKey(Word, on_delete = models.CASCADE)

class Expresion(models.Model):
    expresion = models.ForeignKey(Word, on_delete = models.CASCADE)