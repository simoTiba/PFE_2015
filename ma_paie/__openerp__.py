{
    'name': 'Morocco-payroll',
    'category': 'Localization/Payroll',
    'author': 'TIBA Mohamed',
    "category" : "Localization",
    'version': '1.0',
    'depends': ['hr_payroll'],
    
	
    'description': """Moroccan Payroll Rules.
======================

   Gestion de la Paie Marocaine:    
    - Gestion des employés.
    - Gestion des contrats.
    - Configuration et paramètrage
            * Les rubriques de paie :primes,indemnités,avantages,déductions,...
            * Les rubriques cotisable ,imposable , soumise à la prime d'ancienneté  ...
            * Les cotisations : cotisations salariales et patronales CNSS,AMO...
            * Barème de la prime d'ancienneté,cotisations CNSS ...       
    - Calcul de paie selon les normes marocains : calcul automatique des heures supplémentaire,cotisations salariales et patronales,...
    - Gestion des congés  :Calcul automatique des congés non payés à partir du module hr_holidays
    - Comptabilisation de la paie :  configuration des comptes de credit et de débit
    - Reporting : les  bulletins de paie,journale de paie ,Ordres de virement ...
    """,
    'active': False,
	 'data': [
        'ma_paie_view.xml',
		'ma_paie_data.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,

}
