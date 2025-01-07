from odoo import models,fields

class RestPartner(model.Model):
    _inherit = 'rest.partner'
    is_teacher = fields.Boolean(string= 'Is a teacher')
#   EL NETADATAO __REC__NAME AYUDA A ORDENAR LA VISTA DEL ORDEN ESTO CYANDO NO TIENE UN CAMPO NAME
  
    
#cuando se desea extender un modelo (para añadir campos en este caso)
# en el nombre del modelo se le tiene que ser reemplazado por
#_inherit el cual hace la indicacion que vamos a trabajar sobre un modelo hecho

# existen diferentes tipos de herencia
#1._ Herenciq convencional: cuando se tiene un _inherit y nombre actual de la classe
# esto hace que los valores predeterminados de donde se hereda pase al hijo
#2._ HERENCIA EXTENSION, al no tener un nombre perse o definido esto hace que el hijo reemplace al padre
#3._DELEGATION, Mas que ser una manera de herencia este es un tipo de 
#     _inherits = {
#        'delegation.screen': 'screen_id',
#        'delegation.keyboard': 'keyboard_id',
#    }
   
   
   