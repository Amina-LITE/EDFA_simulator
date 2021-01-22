OpticalComponent = [
['connector'   ,   'ConnectorIn' ,   'in'         ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split1'      ,   '3'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['iso'         ,   'Iso1'        ,   'double'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM2'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ],
['edf'         ,   'EDF1'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ], 
['splice'      ,   ''            ,   'smf-smf'    ],
['iso'         ,   'Iso2'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM3'        ,   '980nm'      ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split2'      ,   '5'          ], #IPD ATM
['splice'      ,   ''            ,   'smf-smf'    ],
['voa'         ,   'VOA1'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split3'      ,   '2'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM4'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ],
['edf'         ,   'EDF2'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ], 
['splice'      ,   ''            ,   'smf-smf'    ],
['iso'         ,   'Iso3'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM5'        ,   '980nm'      ],
['splice'      ,   ''            ,   'smf-smf'    ],
['gff'         ,   'GFF1'        ,   'TFF'        ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM6'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ],
['edf'         ,   'EDF3'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ], 
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split4'      ,   '2'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM7'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ],
['edf'         ,   'EDF4'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ], 
['splice'      ,   ''            ,   'smf-smf'    ],
['iso'         ,   'Iso4'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM8'        ,   '980nm'      ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split5'      ,   '3'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['voa'         ,   'VOA2'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split6'      ,   '2'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split7'      ,   '10'         ],#this is a wdm filter 
['splice'      ,   ''            ,   'smf-smf'    ],
['connector'   ,   'ConnectorOut',   'out'        ]
]

OpticalSource =    [
['source',   'SignalIn' ,   'uniform'         ]
]


Pump1 =    [
['source' ,   'pump1' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['split' ,   'PumpSplit1'      ,   '30'   ,'1'    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM1'  ,   '980nm'    , '1'  ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM2'  ,   '980nm'    , '2'  ]
]

Pump2 =    [
['source' ,   'pump2' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM6'  ,   '980nm'    , '2'  ]
]

Pump3 =    [
['source' ,   'pump2' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM7'  ,   '980nm'    , '2'  ]
]



OpticalPump = [Pump1, Pump2, Pump3]

#['Probe Type' , 'Direction', 'Probe Name' ,  'Port1_Component_Name' ,  'Port2_Component_Name'], ASSUMES COMPONENT NAME IS UNIQUE> NEED TO CHECK. 
OpticalProbe =    [
['Gain'   ,   'Forward'    ,  'AmplifierGain' ,  'SignalIn' ,  'WDM5'     ], 
['Gain'   ,   'Forward'    ,  'Coil1Gain'     ,  'SignalIn'        ,   'WDM6'            ],
['PDSig'     ,   'Forward'    ,  'InputPD'       ,  'Split1'    ,   ''                ],
['PDASE'     ,   'Forward'    ,  'InputPDASE'       ,  'Split5'    ,   ''                ],
['NF'     ,   'Forward'    ,  'TotalNoiseFigure'       ,  'WDM1'    ,   'EDF1'                ]
]