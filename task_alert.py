# -*- coding: utf-8 -*-
# Copyright 2015 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from odoo import models, fields, api
from datetime import date, datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

_logger = logging.getLogger(__name__)

class task_alert(models.Model):
    _description = 'Task Alerts'
    _name = 'task.alert'
    _rec_name = 'task_name'

    active = fields.Boolean(string='Active', default=True)
    project_id = fields.Many2one('project.project', string="Project", required=True)
    days_delta = fields.Integer(
        string="Interval in days",
        help="The amount of days before the date in the field to send out the alert.",
        required=True
    )
    date_field_id = fields.Many2one(
        'ir.model.fields', string="Date field",
        domain=[('ttype', 'in', ('date', 'datetime'))], required=True
    )
    task_name = fields.Char(
        string="Task Name",
        required=True,
        help="The use of placeholders is allowed format like %(fieldname)s is used. Example: %(name)s %(description)s"
    )
    last_run = fields.Datetime("Last run", default=datetime.now())
    user_id = fields.Many2one("res.users", string="Assigned to")
    task_description = fields.Char(
        string="Task Description",
        help="The use of placeholders is allowed format like %(fieldname)s is used. Example: %(name)s %(description)s"
    )
    
    
