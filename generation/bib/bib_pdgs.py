# MARS particle ID definitions for creating MCParticles
# FORMAT: {<MARS ID>: pdgId}
MARS_PIDS = {
    1:  2212,
    2:  2112,
    3:  211,
    4:  -211,
    5:  321,
    6:  -321,
    7:  -13,
    8:  13,
    9:  22,
    10: 11,
    11: -11,
    12: -2212,
    13: 111,
    14: 1000010020,
    15: 1000010030,
    16: 1000020030,
    17: 1000020040,
    18: 14,
    19: -14,
    20: 12,
    21: -12,
    22: 130,
    23: 310,
    24: 311,
    25: -311,
    26: 3122,
    27: -3122,
    28: 3222,
    29: 3212,
    30: 3112,
    31: -2112,
    32: 3322,
    33: 3312,
    34: 3334,
    35: 5112,
    36: 5212,
    37: 5222,
    38: -3322,
    39: -5132,
    40: -5332,
}

FLUKA_PIDS = {
   -6: 1000020040,
   -5: 1000020030,
   -4: 1000010030,
   -3: 1000010020,
    1: 2212,
    2: -2212,
    3: 11,
    4: -11,
    5: 12,
    6: -12,
    7: 22,
    8: 2112,
    9: -2112,
    10: -13,
    11: 13,
    12: 130,
    13: 211,
    14: -211,
    15: 321,
    16: -321,
    17: 3122,
    18: -3122,
    19: 310,
    20: 3112,
    21: 3222,
    22: 3212,
    23: 111,
    24: 311,
    25: -311,
    27: 14,
    28: -14,
    31: -3222,
    32: -3212,
    33: -3112,
    34: 3322,
    35: -3322,
    36: 3312,
    37: -3312,
    38: 3334,
    39: -3334,
    41: -15,
    42: 15,
    43: 16,
    44: -16,
    45: 411,
    46: -411,
    47: 421,
    48: -421,
    49: 431,
    50: -431,
    51: 4122,
    52: 4232,
    53: 4112,
    54: 4322,
    55: 4312,
    56: 4332,
    57: -4122,
    58: -4232,
    59: -4132,
    60: -4322,
    61: -4312,
    62: -4332,
}


# Particle properties for pdgId
# FORMAT: {pdgId: charge, mass [GeV]}
PDG_PROPS = {
    5:          (-1/3, 4.18),
    2212:       ( 1,  0.938272 ),
    2112:       ( 0,  0.939565 ),
    211:        ( 1,  0.13957 ),
    -211:       (-1,  0.13957 ),
    321:        ( 1,  0.493677 ),
    -321:       (-1,  0.493677 ),
    -13:        ( 1,  0.105658 ),
    13:         (-1,  0.105658 ),
    22:         ( 0,  0 ),
    11:         (-1,  0.000510999 ),
    -11:        ( 1,  0.000510999 ),
    -2212:      (-1,  0.938272 ),
    111:        ( 0,  0.134977 ),
    1000010020: ( 1,  1.87561 ),
    1000010030: ( 1,  2.80892 ),
    1000020030: ( 2,  2.80839 ),
    1000020040: ( 2,  3.72738 ),
    14:         ( 0,  0 ),
    -14:        ( 0,  0 ),
    12:         ( 0,  0 ),
    -12:        ( 0,  0 ),
    130:        ( 0,  0.497614 ),
    310:        ( 0,  0.497614 ),
    311:        ( 0,  0.497614 ),
    -311:       ( 0,  0.497614 ),
    3122:       ( 0,  1.11568 ),
    -3122:      ( 0,  1.11568 ),
    3222:       ( 1,  1.18937 ),
    3212:       ( 0,  1.19264 ),
    3112:       (-1,  1.19745 ),
    -2112:      ( 0,  0.939565 ),
    3322:       ( 0,  1.31486 ),
    3312:       (-1,  1.32171 ),
    3334:       (-1,  1.67245 ),
    5112:       (-1,  5.8155 ),
    5212:       ( 0,  5.8078 ),
    5222:       ( 1,  5.8113 ),
    -3322:      ( 0,  1.31486 ),
    -5132:      ( 1,  5.7945 ),
    -5332:      ( 1,  6.0461 ),
}
