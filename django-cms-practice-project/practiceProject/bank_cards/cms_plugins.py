from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import MasterCardInfo, MasterCardsContainer
from django.utils.translation import gettext as _


@plugin_pool.register_plugin
class MasterCardInfoPlugin(CMSPluginBase):
  model = MasterCardInfo
  name = _("Master Card Info")

  render_template = "bank_cards/info_card.html"

  require_parent = True
  parent_classes = ["MasterCardsContainerPlugin"]

  def render(self, context, instance, placeholder):
      context["card"] = instance
      return context



@plugin_pool.register_plugin
class MasterCardsContainerPlugin(CMSPluginBase):
  model = MasterCardsContainer
  name = _("Master Cards Container")

  allow_children = True
  child_classes = ["MasterCardInfoPlugin"]

  render_template = "bank_cards/info_cards_container.html"

  def render (self, context, instance, placeholder):
    # it’s recommended to always populate the context with default 
    # values by calling the render method of the super class
    context = super().render(context, instance, placeholder)
    cards = instance.child_plugin_instances or []
    print(cards)
    active = next((c for c in cards if getattr(c, "is_default", False)), None)

    if active is None and cards:
      active = cards[0]

    print(active.title)
    
    context["cards"] = cards
    context["active_card"] = active

    return context
