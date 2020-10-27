#!/usr/bin/python3
"""Request handlers for the uWeb3 project scaffold"""

import uweb3

class PageMaker(uweb3.DebuggingPageMaker):
  """Holds all the request handlers for the application"""

  def Index(self):
    """Returns the index template"""
    return self.parser.Parse('index.html')

  def Redirect(self):
    """Redirects to the homepage"""
    return uweb3.Redirect('/')

  def FourOhFour(self, path):
    """The request could not be fulfilled, this returns a 404."""
    self.req.response.httpcode = 404
    return self.parser.Parse('404.html', path=path)
