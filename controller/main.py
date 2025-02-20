import json

from odoo import http
from odoo.http import request


class ModelName(http.Controller):

    @http.route(['/api/APiRoute/<int:Var>'], type="http", auth="public", website=True, method=['POST'],
                csrf=False)
    def example(self, Var):
        values = {}

        data = request.env['test.model'].sudo().search([("id", "=", int(Var))])

        if data:
            values['success'] = True
            values['return'] = "Something"
        else:
            values['success'] = False
            values['error_code'] = 1
            values['error_data'] = 'No data found!'

        return json.dumps(values)
