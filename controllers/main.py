from odoo import http
from odoo.http import request

class CustomPageController(http.Controller):

    @http.route('/custom_page', auth='public', website=True)
    def custom_page(self, **kwargs):
        # Lấy dữ liệu từ model 'custom.model'
        records = request.env['custom.model'].sudo().search([])
        return request.render('custom_web.custom_page_template', {
            'records': records
        })