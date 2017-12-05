from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp

class hr_contract(osv.osv):
    _inherit = 'hr.contract'

    _columns = {
        'salhor': fields.float('Salaire/Heures', digits_compute=dp.get_precision('Payroll'),required=True ),
        'nationalite': fields.char('Nationalite', size=64),
        'niveau': fields.char('Niveau', size=64),
        'indemnites': fields.float('Les Indemnites', digits_compute=dp.get_precision('Payroll')),
        'remuneration': fields.float('Les Rémunérations', digits_compute=dp.get_precision('Payroll')),
        'attendence': fields.boolean('Compute from attendance', readonly=False),

    }
hr_contract()


class res_company(osv.osv):
    _inherit = 'res.company'

    _columns = {
        'plafond_secu': fields.float('Plafond de la Securite Sociale', digits_compute=dp.get_precision('Payroll')),
        'nombre_employes': fields.integer('Nombre d\'employes'),
        'cotisation_prevoyance': fields.float('Cotisation Patronale Prevoyance', digits_compute=dp.get_precision('Payroll')),
        'org_ss': fields.char('Organisme de securite sociale', size=64),
        'conv_coll': fields.char('Convention collective', size=64),
    }

res_company()



class hr_payslip(osv.osv):
    _inherit = 'hr.payslip'

    _columns = {
        'payment_mode': fields.char('Mode de paiement', size=64),
    }
hr_payslip()

    
    
    
class hr_employee(osv.osv):
    _inherit = 'hr.employee'
	
	
    _columns = {
		'matricule_cnss':fields.integer('Matricule CNSS', size=10),
        'matricule_cimr':fields.integer('Matricule CIMR', size=10),
		'matriculation':fields.integer('Matricule'),
        'adresse_pro': fields.char('Adresse profesionnel', size=64),
        'adresse_elc': fields.char('Adresse electronique', size=64),


	}
hr_employee()

		
		
		
		
		
		
		
		
		
		
	
