import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class BookTheSHow(models.Model):
    _name = "book.the.show"
    _description = "book the show"
    # _order = "sequence"

    mv_name = fields.Char('Movie Name ', required=True)