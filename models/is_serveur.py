# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class IsServeur(models.Model):
    _name = 'is.serveur'
    _description = "Serveur"
    _order = 'name'

    name                = fields.Char(u"Nom du serveur", required=True, index=True)
    partner_id          = fields.Many2one('res.partner', u"Client")
    adresse_ip          = fields.Char(u"Adresse IP")
    date_creation       = fields.Date(u"Date de création")
    date_fin            = fields.Date(u"Date fin abonnement")
    renouvellement_auto = fields.Selection([
            ('oui', u'Oui'),
            ('non', u'Non'),
        ], u"Renouvellement auto")
    mot_de_passe        = fields.Char(u"Mot de passe")
    systeme             = fields.Char(u"Système")
    type_vps            = fields.Char(u"Type de VPS")
    commentaire         = fields.Text(u"Commentaire")
    active              = fields.Boolean(u"Actif", default=True)

