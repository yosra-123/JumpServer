from django.utils.translation import ugettext as _
from tickets.models import ApplyLoginTicket
from .base import BaseHandler


class Handler(BaseHandler):
    ticket: ApplyLoginTicket

    def _construct_meta_body_of_open(self):
        apply_login_ip = self.ticket.apply_login_ip
        apply_login_city = self.ticket.apply_login_city
        apply_login_datetime = self.ticket.apply_login_datetime
        applied_body = '''
            {}: {}
            {}: {}
            {}: {}
        '''.format(
            _("Applied login IP"), apply_login_ip,
            _("Applied login city"), apply_login_city,
            _("Applied login datetime"), apply_login_datetime,
        )
        return applied_body
