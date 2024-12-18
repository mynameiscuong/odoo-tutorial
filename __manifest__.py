# -*- coding: utf-8 -*-
{
    "name":"OWL tutorial",
    "version": "1.0",
    "summary":"OWL tutorial",
    "sequence":-1,
    "description":""""OWL Tutorial""",
    "category":"OWL" ,
    "depends":['base','website'],
    "data":[
        "security/ir.model.access.csv",
        "views/todo_list.xml"
    ],
    "demo":[],
    "installable":True,
    "application":True,
    "assets":{
        "web.assets_backend":[
            "owl/static/src/components/*/*.js",
            "owl/static/src/components/*/*.scss",
            "owl/static/src/components/*/*.xml",
            "owl/static/src/**/*",
        ],
    },
}