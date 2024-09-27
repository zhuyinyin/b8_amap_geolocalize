# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    geoloc_provider_amap_key = fields.Char(
        string='amap API Key',
        config_parameter='amap_geolocalize.amap_api_key',
        help="Visit https://lbs.amap.com/api/webservice/create-project-and-key for more information."
    )
