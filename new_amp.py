OpticalComponent = [
['connector'   ,   'ConnectorIn' ,   'in'         ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split1'      ,   '2'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split2'      ,   '2'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['iso'         ,   'Iso1'        ,   'double'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM1'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ], 
['edf'         ,   'EDF1'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM2'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['iso'         ,   'Iso2'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split3'      ,   '2'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['voa'         ,   'VOA'         ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split4'      ,   '2'          ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM3'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ], 
['edf'         ,   'EDF2'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM4'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['iso'         ,   'Iso3'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['switchstart' ,   'SWITCH1'     ,   'start'       ],
['splice'      ,   ''            ,   'smf-smf'    ],
['gff'         ,   'GFF2'        ,   'TFF'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM7'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ], 
['edf'         ,   'EDF4'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ],
['splice'      ,   ''            ,   'smf-smf'    ],
['iso'         ,   'Iso5'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['split'       ,   'Split5'      ,   '2'          ],
['connector'   ,   'ConnectorOut',   'out'        ]
]

OpticalSource =    [
['source',   'SignalIn' ,   'uniform'         ]
]

SwitchComponent =    {
'SWITCH1' : [
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM5'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['splice'      ,   ''            ,   'spec-edf'   ], 
['edf'         ,   'EDF3'        ,   ''           ],
['splice'      ,   ''            ,   'smf-edf'    ],
['splice'      ,   ''            ,   'smf-smf'    ],
['wdm'         ,   'WDM6'        ,   '980nm'      ],
['splice'      ,   ''            ,   'spec-spec'  ],
['iso'         ,   'Iso4'        ,   'single'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
['splice'      ,   ''            ,   'smf-smf'    ],
['gff'         ,   'GFF1'        ,   'TFF'     ],
['splice'      ,   ''            ,   'smf-smf'    ],
]
}

Pump1 =    [
['source' ,   'pump1' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM1'  ,   '980nm'    , '2'  ]
]

Pump2 =    [
['source' ,   'pump2' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['split' ,   'PumpSplit1'      ,   '50'   ,'1'    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM3'  ,   '980nm'    , '2'  ]
]

Pump3 =    [
['source' ,   'pump2' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['split' ,   'PumpSplit1'      ,   '50'   ,'1'    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM7'  ,   '980nm'    , '2'  ]
]

Pump4 =    [
['source' ,   'pump1' ,   ''    ,''    ],
['splice' ,   ''      ,   'spec-spec'   ,''    ],
['wdm'    ,   'WDM5'  ,   '980nm'    , '2'  ]
]

OpticalPump = [Pump1, Pump2, Pump3, Pump4]