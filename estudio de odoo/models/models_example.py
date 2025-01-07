from odoo import models,fields


class Course(models.Model):
    __name__='nombreEntidadBD'
    
    name= fields.Char(string= 'Name')
    student_qty = fields.Integer(string= 'Studen qty')
    grades_average = fields.Text(string= 'Description')
    is_active = fields.Boolean(string = 'Is Active')
    course_start = fields.Date(string= 'Course Start')
    course_End = fields.Date(string ='Course Ends')
    last_evaluation_date = fields.DateTime (string = 'Course last evaluation')

# _name es el nombre que llevara la tabla y el nombre del modelo en general
# existen diferentes tipos de datos para registrar en el orm de odoo
# integer = numeros, Text= texto, Char= caracteres
#Date = fecha 
#estos son datos simples que podria llevar un modelo
#
#