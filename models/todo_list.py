from odoo import api, models, fields

class OwlTodo(models.Model):
    _name = 'owl.todo.list'
    _description = 'OWL Todo List App'

    name = fields.Char(string='Task name')
    completed=fields.Boolean()
    color = fields.Char()
