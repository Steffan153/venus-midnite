#!/usr/bin/env python

# Name: 		config.py
# Purpose:	Configuration details Midnite Classic
# Date:		12-12-2024
# Version:	2.0
# Author:	Jan Bakuwel / YSolar NZ Ltd
# License:	GNU General Public License v3.0

VERSION	= "v2.0"

MIDNITE_IPS	= [
  ("192.168.1.223", "Midnite Classic Charge Controller 1"),
  ("192.168.1.170", "Midnite Classic Charge Controller 2"),
  ("192.168.1.226", "Midnite Classic Charge Controller 3"),
  ("192.168.1.113", "Midnite Classic Charge Controller 4"),
  ("192.168.1.220", "Midnite Classic Charge Controller 5"),
  ("192.168.1.190", "Midnite Classic Charge Controller 6"),
  ("192.168.1.218", "Midnite Classic Charge Controller 7"),
]


MIDNITE_INTERVAL	= 5


MIDNITE_VICTRON	= {
	0: 0,	# Midnite Resting:	Victron Off
	3: 4,	# Midnite Absorb:		Victron Absorption
	4: 3,	# Midnite BulkMPPT:	Victron Bulk
	5: 5,	# Midnite Float:		Victron Float
	6: 5,	# Midnite FloatMPPT:	Victron Float
	7: 7,	# Midnite Equalize:	Victron Equalize
	10:	3,	# HyperVOC:				Victron Bulk - I guess
	18:	7,	# EqualizeMPPT:		Victron Equalize
}
