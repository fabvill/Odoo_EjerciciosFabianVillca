{
    "name": "Modulo Prueba FVT",
    "summary": "Módulo de prueba para Odoo",
    "version": "17.0.0.0.0",
    "license": "OEEL-1",
    "author": "Fabian Villca Toribio",
    "category": "Uncategorized",
    "depends": ["crm"],  
    "data": [ "security/res_groups.xml",
               "security/ir.model.access.csv"],
        "demo":[
          "demo/demo.xml"  
        ],
        "installable": True,
        "application": True,
        "auto_install": False,  
}
