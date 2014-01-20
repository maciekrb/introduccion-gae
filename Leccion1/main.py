# -*- coding: utf-8 -*-
"""
Punto de entrada principal a la aplicación

Extiende el RequestHandler standard de webapp2, un micro framework para
desarrollo de aplicaciones con Python sobre App Engine.
Documentación: http://webapp-improved.appspot.com/

"""

import webapp2


class MainPage(webapp2.RequestHandler):
  """
  Handler principal de la aplicación

  Define los métodos que atenderán las solicitudes
  que se hagan a la raiz del sitio ("/")
  """

  def get(self):
    """
    Atiende solicitudes con el método GET
    """
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hola Mundo: Solicitud GET %s' % self.request.GET)

  def post(self):
    """
    Atiende solicitudes con el método POST
    """
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hola Mundo: Solicitud POST %s' % self.request.POST)


app = webapp2.WSGIApplication([
    ('/', MainPage),  # Asigna MainPage como handler de la ruta "/"
], debug=True)
