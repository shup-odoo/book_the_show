import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _


class BookTheShow(models.Model):
    _name = "ticket.booking"
    _description = "Ticket Booking for Movie"
    # _rec_name = "mv_name"
    # _order = "sequence"
    tb_select_movie = fields.Many2one('book.the.show', string="Select Movie")
    tb_seat_type = fields.Selection([('standard', 'Standard'), ('vip', 'VIP'), ('premium', 'Premium')],
                                    string='Seat Type')
    tb_seat_price = fields.Float(string='Seat Price', compute='_compute_seat_price')

    @api.depends('st_seat_type')
    def _compute_seat_price(self):
        seat_prices = {
            'standard': 200.0,
            'vip': 300.0,
            'premium': 400.0
        }
        for ticket in self:
            ticket.seat_price = seat_prices.get(ticket.seat_type, 0.0)
