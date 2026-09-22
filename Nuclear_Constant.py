import json

Nuclear_Constants = {
    "u_kg": 1.66053906660e-27,
    "c": 299792458,
    "avogadro": 6.02214076e23,
    "e_charge":1.602176634e-19,
    "ev_joule":1.602176634e-19,
    "proton_mass_u": 1.00727646662,
    "neutron_mass_u": 1.00866491595,
    "electron_mass_u": 0.000548579909,
    "u_to_Mev": 931.49410242
}


data_atom = json.dumps(Nuclear_Constants, indent=2)

print (data_atom)
print (Nuclear_Constants["u_kg"])
print (Nuclear_Constants["c"])
print (Nuclear_Constants["avogadro"])
print (Nuclear_Constants["e_charge"])
print (Nuclear_Constants["ev_joule"])
print (Nuclear_Constants["proton_mass_u"])
print (Nuclear_Constants["neutron_mass_u"])
print (Nuclear_Constants["electron_mass_u"])
print (Nuclear_Constants["u_to_Mev"])
