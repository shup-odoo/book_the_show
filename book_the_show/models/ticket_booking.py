import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _


class TicketBooking(models.Model):
    _name = "ticket.booking"
    _description = "Ticket Booking for Movie"
    _rec_name = "tb_ticket_booking_movie"

    tb_ticket_booking_movie = fields.Many2one("movie.show.time", string="Select the show")
    tb_select_show = fields.Char(string="SHOW Name", related="tb_ticket_booking_movie.st_show_name",
                                      store=True)
    tb_select_screen_number = fields.Selection(string='Screen Number',
                                               related="tb_ticket_booking_movie.st_screen_number",
                                               store=True)
    tb_select_show_time = fields.Selection(string='Show Timing',
                                           related="tb_ticket_booking_movie.st_start_time",
                                           store=True)
    tb_seat_type = fields.Selection([('standard', 'Standard'), ('vip', 'VIP'), ('premium', 'Premium')],
                                    string='Seat Type')
    tb_seat_price = fields.Float(string='Seat Price', compute='_compute_seat_price')

    tb_number_of_seats = fields.Integer(string="How Many Seats ?")

    tb_total_price = fields.Float(string="Total Price", compute='_compute_total_price')

    _sql_constraints = [
        ('check_number_of_seats', 'CHECK(tb_number_of_seats <= 10)',
         "Sorry you don't book more then 10 tickets at a time ")]

    @api.depends('tb_seat_price')
    def _compute_seat_price(self):
        tb_seat_price = {
            'standard': 200.0,
            'vip': 300.0,
            'premium': 400.0
        }
        for ticket in self:
            ticket.tb_seat_price = tb_seat_price.get(ticket.tb_seat_type, 0.0)

    @api.depends('tb_number_of_seats', 'tb_seat_price')
    def _compute_total_price(self):
        # for area in self:
        self.tb_total_price = self.tb_number_of_seats * self.tb_seat_price
