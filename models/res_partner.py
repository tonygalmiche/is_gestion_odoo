# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_effectif              = fields.Integer("Effectif")
    is_activite              = fields.Char("Activité")
    is_dirigeant             = fields.Char("Dirigeant")
    is_contact               = fields.Char("Contact")
    is_derniere_intervention = fields.Text("Commentaire dernière intervention")
    is_siren                 = fields.Char("SIREN")
    is_forme_juridique       = fields.Char("Forme juridique")
    is_date_debut_activite   = fields.Date("Date de début d'activité")
    is_categorie             = fields.Char("Catégorie")
    is_dynacase_id           = fields.Integer("Id Dynacase")






