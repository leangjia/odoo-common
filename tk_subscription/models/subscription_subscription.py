# -*- encoding: utf-8 -*-
##############################################################################
#
#    Author: Taktik S.A.
#    Copyright (c) 2015 Taktik S.A. (http://www.taktik.be)
#    All Rights Reserved
#
#    WARNING: This program as such is intended to be used by professional
#    programmers who take the whole responsibility of assessing all potential
#    consequences resulting from its eventual inadequacies and bugs.
#    End users who are looking for a ready-to-use solution with commercial
#    guarantees and support are strongly advised to contact a Free Software
#    Service Company.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from openerp import api, exceptions, fields, models, _


class SubscriptionSubscription(models.Model):
    _inherit = 'subscription.subscription'

    @property
    def ret_invoice_only(self):
        return self.invoice_only

    @api.onchange('partner_id')
    def partner_id_filter(self):
        if not self.ret_invoice_only:
            return

        return {'domain': {'invoice_id': [('partner_id', '=', self.partner_id.id)]}} if self.invoice_only else False

    invoice_id = fields.Many2one('account.invoice',
                                 string='Invoice')

    invoice_only = fields.Boolean(string='Invoice only ?',
                                  default=False,
                                  help="")
