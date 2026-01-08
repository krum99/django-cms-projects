from django.db import models
from cms.models.pluginmodel import CMSPlugin
from .utils import split_words

class SteppedCarousel(CMSPlugin):
  title = models.CharField(max_length=256)

  def __str__(self):
    return self.title or split_words(self.__class__)


class CarouselStep(CMSPlugin):
  title = models.CharField(max_length=256)
  text = models.TextField()

  def __str__(self):
    return self.title or split_words(self.__class__)