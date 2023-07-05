# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class IsServeur(models.Model):
    _name = 'is.serveur'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = "Serveur"
    _order = 'name'

    name                = fields.Char(u"Nom du serveur"                , required=True, index=True)
    partner_id          = fields.Many2one('res.partner', u"Client"     , required=True)
    fournisseur_id      = fields.Many2one('res.partner', u"Fournisseur", required=True)
    adresse_ip          = fields.Char(u"Adresse IP", required=True)
    date_creation       = fields.Date(u"Date de création")
    date_fin            = fields.Date(u"Date fin abonnement")
    renouvellement_auto = fields.Selection([
            ('oui', u'Oui'),
            ('non', u'Non'),
        ], u"Renouvellement auto")
    service_id          = fields.Many2one('is.service', u"Service", required=True)
    mot_de_passe        = fields.Char(u"Mot de passe")
    systeme_id          = fields.Many2one('is.systeme', u"Système", required=True)
    type_vps_id         = fields.Many2one('is.type.vps', u"Type de VPS")
    commentaire         = fields.Text(u"Commentaire")
    grafana             = fields.Boolean(u"Grafana", default=False)
    sauvegarde          = fields.Boolean(u"Vérification sauvegarde", default=True)
    active              = fields.Boolean(u"Actif"  , default=True)


class IsSysteme(models.Model):
    _name = 'is.systeme'
    _description = "Système"
    _order = 'name'

    name = fields.Char(u"Système", required=True, index=True)


class IsTypeVPS(models.Model):
    _name = 'is.type.vps'
    _description = "Type de VPS"
    _order = 'name'

    name = fields.Char(u"Type de VPS", required=True, index=True)


class IsService(models.Model):
    _name = 'is.service'
    _description = "Service"
    _order = 'name'

    name = fields.Char(u"Service", required=True, index=True)
