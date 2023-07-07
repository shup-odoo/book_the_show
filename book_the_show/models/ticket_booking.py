import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _


class BookTheShow(models.Model):
    _name = "ticket.booking"
    _description = "Ticket Booking for Movie"
    # _rec_name = "mv_name"
    # _order = "sequence"

