from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SteppedCarousel, CarouselStep

from .utils import split_words


@plugin_pool.register_plugin
class SteppedCarouselPlugin(CMSPluginBase):
  model = SteppedCarousel
  name = f"{split_words(SteppedCarousel)} Plugin"
  render_template = "steppedCarousel/stepped_carousel.html" 

  allow_children = True
  child_classes=["CarouselStepPlugin"]

@plugin_pool.register_plugin
class CarouselStepPlugin(CMSPluginBase):
  model = CarouselStep
  name = f"{split_words(SteppedCarousel)} Plugin"
  render_template = "steppedCarousel/carousel_step.html" 

  require_parent = True
  parent_classes=["SteppedCarouselPlugin"]
