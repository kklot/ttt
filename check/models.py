from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    # def was_published_recently(self):
        # return self.pub_date >= timezone.now() - date


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# from django.contrib.auth.hashers import make_password

class DuocThu(models.Model):
    """docstring for DuocThu"""
    ten_ngan = models.CharField(max_length=9)
    ten_dai = models.CharField(max_length=200)
    ten_thuongmai = models.CharField(max_length=200)
    nhasanxuat = models.CharField(max_length=200)
    def __str__(self):
        return self.ten_dai

DANH_SACH_THUOC = [
    ('A', 'thuoc A'),
    ('B', 'thuoc B'),
    ('C', 'thuoc C'),
    ('D', 'thuoc D'),
    ('E', 'thuoc E'),
    ('F', 'thuoc F'),
    ('G', 'thuoc G'),
    ('H', 'thuoc H'),
    ('I', 'thuoc I'),
    ('J', 'thuoc J'),
    ('K', 'thuoc K'),
    ('L', 'thuoc L'),
    ('M', 'thuoc M'),
    ('N', 'thuoc N'),
    ('O', 'thuoc O'),
    ('P', 'thuoc P'),
    ('Q', 'thuoc Q'),
    ('R', 'thuoc R'),
    ('S', 'thuoc S'),
    ('T', 'thuoc T'),
    ('U', 'thuoc U'),
    ('V', 'thuoc V'),
    ('W', 'thuoc W'),
    ('X', 'thuoc X'),
    ('Y', 'thuoc Y'),
    ('Z', 'thuoc Z'),
]

from .kutils import gen_hash_tt
# import hashlib

# def gen_hash_tt(a, b):
#     return hashlib.sha256(str.encode(a+b)).hexdigest()

class Tuongtac(models.Model):
    """docstring for Tuongtac"""
    # DANH_SACH_THUOC2= DuocThu.objects.get()
    tt_thuoc_a = models.CharField(max_length=200, choices=DANH_SACH_THUOC)
    tt_thuoc_b = models.CharField(max_length=200, choices=DANH_SACH_THUOC)
    tt_hash = models.CharField(max_length=256, blank=True)
    tt_desc = models.TextField()
    tt_rank = models.IntegerField()
    tt_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tt_desc
    def save(self, *arg, **kwargs):
        self.tt_hash = gen_hash_tt(self.tt_thuoc_a, self.tt_thuoc_b)
        super(Tuongtac, self).save(*arg, **kwargs)
