import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _


class ShowTime(models.Model):
    _name = "movie.show.time"
    _description = "Movie Show Timing"
    # _order = "sequence"
    _rec_name = "st_movie_name"

    st_movie_name = fields.Many2one('book.the.show', string="Select Movie")
    # st_start_time = fields.Float(string='Time')
    st_screen_type = fields.Many2many('screen.types', string='Screen Type')
    st_language = fields.Many2many('movie.language', string='Movie Languages')
    st_screen_number = fields.Selection(string='Screen Number',
                                        selection=[('1', 1), ('2', 2), ('3', 3),
                                                   ('4', 4)])
    st_start_time = fields.Selection(string='Show Timing',
                                     selection=[('morning_01', "09:00"), ('morning_02', "12:00"),
                                                ('afternoon_01', "15:00"),
                                                ('evening_01', "18:00"),
                                                ('night', "21:00")
                                                ])
    st_seat_type = fields.Selection([('standard', 'Standard'), ('vip', 'VIP'), ('premium', 'Premium')],
                                    string='Seat Type')
