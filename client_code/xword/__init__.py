from ._anvil_designer import xwordTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class xword(xwordTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def check_word_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
  
 


