## Describe amplifier
##############################################################
##############################################################
## Describe Component Layer 
""" How does it work?
OpticalComponent =    [

 1st entry:    ['Component Family' , 'Component Name', 'Component Type'],
 2nd entry:    ['Component Family' , 'Component Name', 'Component Type'],
    .
    .
    .
  last entry:  ['Component Family' , 'Component Name', 'Component Type']
No comma for last entry
]
"""
OpticalComponent =    [
['connector',   'ConnectorIn' ,   'in'         ],
['splice'   ,   ''            ,   'smf-smf'    ],
['split'    ,   'Split1'      ,   '2'          ],
['splice'   ,   ''            ,   'smf-smf'    ],
['iso'      ,   'Iso1'        ,   'double'     ],
['splice'   ,   ''            ,   'smf-smf'    ],
['wdm'      ,   'WDM1'        ,   '980nm'      ],
['splice'   ,   ''            ,   'spec-spec'  ],
['splice'   ,   ''            ,   'spec-edf'   ], 
['edf'      ,   'EDF1'        ,   ''           ],
['splice'   ,   ''            ,   'smf-edf'    ],
['splice'   ,   ''            ,   'smf-smf'    ],
['gff'      ,   'GFF1'        ,   'TFF'        ],
['splice'   ,   ''            ,   'smf-smf'    ],
['iso'      ,   'Iso2'        ,   'single'     ],
['splice'   ,   ''            ,   'smf-smf'    ],
['split'    ,   'Split2'      ,   '2'          ],
['splice'   ,   ''            ,   'smf-smf'    ],
['connector',   'ConnectorOut',   'out'        ]
# last entry NO comma
]
##############################################################
##############################################################
## Describe Switch Layer
""" How does it work?
SwitchComponent =    [

 1st entry:    ['Component Family' , 'Component Name', 'Component Type'],
 2nd entry:    ['Component Family' , 'Component Name', 'Component Type'],
    .
    .
    .
  last entry:  ['Component Family' , 'Component Name', 'Component Type']
No comma for last entry
]
"""
SwitchComponent =    {
'SWITCH1' : [
['iso'      ,   'Iso3'        ,   'double'     ],
['splice'   ,   ''            ,   'smf-smf'    ],
['wdm'      ,   'WDM2'        ,   '980nm'      ],
['splice'   ,   ''            ,   'spec-spec'  ],
['splice'   ,   ''            ,   'spec-edf'   ], 
['edf'      ,   'EDF2'        ,   ''           ],
['splice'   ,   ''            ,   'smf-edf'    ],
['splice'   ,   ''            ,   'smf-smf'    ],
['gff'      ,   'GFF2'        ,   'TFF'        ],
['splice'   ,   ''            ,   'smf-smf'    ],
['iso'      ,   'Iso4'        ,   'single'     ],
['splice'   ,   ''            ,   'smf-smf'    ],
['split'    ,   'Split3'      ,   '2'          ],
['splice'   ,   ''            ,   'smf-smf'    ]
], 
'SWITCH2' : [
['iso'      ,   'Iso3'        ,   'double'     ],
['splice'   ,   ''            ,   'smf-smf'    ],
['wdm'      ,   'WDM2'        ,   '980nm'      ],
['splice'   ,   ''            ,   'spec-spec'  ],
['splice'   ,   ''            ,   'spec-edf'   ], 
['edf'      ,   'EDF2'        ,   ''           ],
['splice'   ,   ''            ,   'smf-edf'    ],
['splice'   ,   ''            ,   'smf-smf'    ],
['gff'      ,   'GFF2'        ,   'TFF'        ],
['splice'   ,   ''            ,   'smf-smf'    ],
['iso'      ,   'Iso4'        ,   'single'     ],
['splice'   ,   ''            ,   'smf-smf'    ],
['split'    ,   'Split3'      ,   '2'          ],
['splice'   ,   ''            ,   'smf-smf'    ]
# last entry NO comma
]
}

##############################################################
##############################################################
## Describe Source Layer 
""" How does it work?
OpticalSource =    [

 1st entry:    ['Component Family' , 'Component Name', 'Component Type'],
 2nd entry:    ['Component Family' , 'Component Name', 'Component Type'],
    .
    .
    .
  last entry:  ['Component Family' , 'Component Name', 'Component Type']
No comma for last entry
]
"""
OpticalSource =    [
['source',   'SignalIn' ,   'uniform'         ]
# last entry NO comma
]
##############################################################
##############################################################
## Describe Pump Layer: describe path of each pump to corresponding EDF 
""" How does it work?
OpticalPump =    [

 1st entry:    ['Component Family' , 'Component Name', 'Component Type' , 'Connected to which component and port'],
 2nd entry:    ['Component Family' , 'Component Name', 'Component Type' , 'Connected to which component and port'],
    .
    .
    .
  last entry:  ['Component Family' , 'Component Name', 'Component Type' , 'Connected to which port']
No comma for last entry
]
"""
OpticalPump =    [
['source' ,   'pump1' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'wdm1'  ,   '980nm'    , '2'  ]
# last entry NO comma
]

##############################################################
##############################################################
## Describe Probe Layer: describe probes 
""" How does it work?
OpticalProbe =    [

 1st entry:    ['Probe Type' , 'Direction', 'Probe Name' , 'Component/Port 1' , 'Component/Port 2'],
 2nd entry:    ['Probe Type' , 'Direction', 'Probe Name' , 'Component/Port 1' , 'Component/Port 2'],
    .
    .
    .
  last entry:  ['Probe Type' , 'Direction', 'Probe Name' , 'Component/Port 1' , 'Component/Port 2']
No comma for last entry
]
"""
OpticalProbe =    [
['PD'     ,   'Forward'    ,  'InputPD'       ,  'Split1/2'   ,   ''                        ],
['PD'     ,   'Forward'    ,  'OutputPD'      ,  'Split2/2'   ,   ''                        ],
['Gain'   ,   'Forward'    ,  'AmplifierGain' ,  'SignalIn/1' ,   'ConnectorOut/1'          ],
['NF'     ,   'Forward'    ,  'AmplifierNF'   ,  'SignalIn/1' ,   'ConnectorOut/1'          ],
['Gain'   ,   'Forward'    ,  'Coil1Gain'     ,  'WDM1/1'     ,   'EDF1/1'                  ]
# last entry NO comma
]

##############################################################
##############################################################
## Test
#print(OpticalComponent[1][0])
#print(OpticalSource[0][0])
#print(OpticalPump[2][0])
#print(OpticalProbe[2][0])