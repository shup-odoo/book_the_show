import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ShowTime(models.Model):
    _name = "movie.show.time"
    _description = "Movie Show timing"
    # _order = "sequence"

    st_name = fields.Char('Movie Name ', required=True)
    st_start_time = fields.Float(string='Time')
    st_end_time = fields.Float(string='Time')
    # st_screen_number = fields.Integer(string="Screen NUmber")
    # st_screen_type = fields.Many2one('screen.types', string='Screen Type')
    # st_language = fields.Many2one('movie.language', string='Movie Languages')
