# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class IsAffaire(models.Model):
    _name = 'is.affaire'
    _description = "Affaire"
    _order = 'name desc'

    name               = fields.Char("Affaire", readonly=True, index=True)
    intitule           = fields.Char("Intitulé de l'affaire", required=True, index=True)
    partner_id         = fields.Many2one('res.partner', "Client", required=True, index=True, 
                            domain=[('customer','=',True),('is_company','=',True)])
    date_debut         = fields.Date("Date de début", default=fields.Date.today())
    date_fin           = fields.Date("Date de fin")
    ca_previsionnel    = fields.Float("CA prévisionnel", digits=(14,2))
    frais_previsionnel = fields.Float("Frais prévisionnel", digits=(14,2))
    commentaire        = fields.Text("Commentaire")
    state              = fields.Selection([
            ('devis'     , u'Devis'),
            ('abandonnee', u'Abandonnée'),
            ('active'    , u'Active'),
            ('soldee'    , u'Soldée'),
        ], u"État", index=True, default='active')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('is.affaire')
        res = super(IsAffaire, self).create(vals)
        return res


    @api.multi
    def name_get(self):
        result = []
        for obj in self:
            result.append((obj.id, '['+str(obj.name)+'] '+str(obj.intitule)+' ('+obj.partner_id.name+')'))
        return result


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        ids = []
        if name:
            ids = self._search(['|','|',('name', 'ilike', name),('intitule', 'ilike', name),('partner_id.name', 'ilike', name)] + args, limit=limit, access_rights_uid=name_get_uid)
        else:
            ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return self.browse(ids).name_get()


