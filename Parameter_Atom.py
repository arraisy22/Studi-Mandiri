import json
with open("Parameter_atom.json", "r") as file:
    atoms_list = json.load(file)

target_mass = int(input("Masukkan nomor massa isotop yang ingin dicari: "))

found_atom = None
found_isotope = None

for atom in atoms_list:
    for isotope in atom["isotopes"]:
        if isotope["mass_number"] == target_mass:
            found_atom = atom
            found_isotope = isotope
            break

if found_atom:
    print(f"--- Atom Ditemukan ---")
    print(f"Nama Atom        : {found_atom['name']} ({found_atom['symbol']})")
    print(f"Nomor Atom       : {found_atom['atomic_number']}")
    print(f"Massa Isotop (u) : {found_isotope['atomic_mass_u']}")
    print(f"Kelimpahan Alami : {found_isotope['natural_abundance_percent']}%")
    print(f"Status Kestabilan: {'Stabil' if found_isotope['stable'] else 'Tidak Stabil (Radioaktif)'}")
else:
    print("Isotop tidak ditemukan.")
    