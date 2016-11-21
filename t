Creating directory to store temporary files.
FileIO Functions
    load_pdb_into_using_file_object()

Error: Cannot calculate bonds by distance. Install this
       recommended dependency: NUMPY

    save_pdb()
    save_pym()

Error: Cannot save pym files. Install this recommended
       dependency: NUMPY

    load_pdbqt_into_using_file_object()
    load_pdbqt_into()
    load_pym_into()

Error: Cannot load pym files. Install this recommended
       dependency: NUMPY

    load_pdb_into()

Error: Cannot calculate bonds by distance. Install this
       recommended dependency: NUMPY

Information Functions
    get_filename()
        Filename: ./pymolecule_tests_tmp/file_io_test.pdb
    get_remarks()
        [' This is a remark.']
    assign_elements_from_atom_names()
    assign_masses()
    get_center_of_mass()
        [33.0643089093136, 19.13574708872268, 16.05629867850806]
    get_atom_information()
        {'tempfactor': 12.04, 'chainid': 'A', 'record_name': 'ATOM  ', 'name': '  N  ', 'resname_stripped': 'GLN', 'occupancy': 1.0, 'element': ' N', 'resseq': 1, 'charge': '  \n', 'mass': 14.0067, 'element_stripped': 'N', 'resname': ' GLN ', 'name_stripped': 'N', 'chainid_stripped': 'A', 'serial': 1}
    get_coordinates()
        [42.237, 16.8, 35.823]
    get_bonds()

Error: Cannot test get_bonds(). Install this recommended
       dependency: NUMPY

    get_geometric_center()
        [33.09860847880298, 19.122119700748147, 16.042680798004994]
    get_total_number_of_atoms()
        401
    get_total_number_of_heavy_atoms()
        401
    get_total_mass()
        5289.173
    get_bounding_box()
        [array([14.309, 2.141, -0.939]), array([50.363, 34.611, 47.515])]
    get_bounding_sphere()

Error: Cannot calculate a sphere that bounds a set of atoms.
       Install this recommended dependency: NUMPY

        None
    get_constants()
        {'mass_dict': {'BE': 9.0122, 'ZN': 65.38, 'FE': 55.845, 'BR': 79.904, 'HG': 200.59, 'NA': 22.9897, 'CL': 35.453, 'LI': 6.941, 'PB': 207.2, 'RH': 102.9055, 'CA': 40.078, 'C': 12.0107, 'B': 10.811, 'CO': 58.9332, 'AG': 107.8682, 'F': 18.9984032, 'I': 126.90447, 'H': 1.00794, 'K': 39.0983, 'AL': 26.9815, 'O': 15.9994, 'N': 14.0067, 'P': 30.973762, 'S': 32.065, 'AU': 196.9655, 'CU': 63.9332, 'MG': 24.305, 'MO': 95.94, 'MN': 54.938, 'AS': 74.9216, 'BI': 208.9804}, 'rna_residues': ['A', 'C', 'G', 'U', 'RA', 'RA3', 'RA5', 'RAN', 'RC', 'RC3', 'RC4', 'RC5', 'RCN', 'RG', 'RG3', 'RG5', 'RGN', 'RU', 'RU3', 'RU5', 'RUN'], 'f8_fields': ['x', 'y', 'z', 'occupancy', 'tempfactor'], 'vdw_dict': {'ZN': 1.39, 'FE': 2.0, 'BR': 1.85, 'NA': 2.27, 'CL': 1.75, 'LI': 1.82, 'PB': 2.02, 'RH': 2.0, 'K': 2.75, 'C': 1.7, 'B': 2.0, 'CO': 2.0, 'AG': 1.72, 'F': 1.47, 'I': 1.98, 'H': 1.2, 'CA': 2.0, 'AL': 2.0, 'O': 1.52, 'N': 1.55, 'P': 1.8, 'AS': 1.85, 'AU': 1.66, 'CU': 1.4, 'MG': 1.73, 'MO': 2.0, 'MN': 2.0, 'S': 1.8, 'BI': 2.0}, 'i8_fields': ['serial', 'resseq'], 'protein_residues': ['ALA', 'ARG', 'ASH', 'ASN', 'ASP', 'CYM', 'CYS', 'CYX', 'GLN', 'GLH', 'GLU', 'GLY', 'HID', 'HIE', 'HIP', 'HIS', 'ILE', 'LEU', 'LYN', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL', 'MSE', 'TPO', 'PTR', 'SEP', 'CALA', 'CARG', 'CASN', 'CASP', 'CCYS', 'CCYX', 'CGLN', 'CGLU', 'CGLY', 'CHID', 'CHIE', 'CHIP', 'CHIS', 'CILE', 'CLEU', 'CLYS', 'CMET', 'CPHE', 'CPRO', 'CSER', 'CTHR', 'CTRP', 'CTYR', 'CVAL', 'NALA', 'NARG', 'NASN', 'NASP', 'NCYS', 'NCYX', 'NGLN', 'NGLU', 'NGLY', 'NHID', 'NHIE', 'NHIP', 'NHIS', 'NILE', 'NLEU', 'NLYS', 'NMET', 'NPHE', 'NPRO', 'NSER', 'NTHR', 'NTRP', 'NTYR', 'NVAL'], 'bond_length_dict': {'C-CL': 1.79, 'CL-SI': 2.072, 'C-O': 1.413, 'C-N': 1.469, 'C-I': 2.162, 'C-H': 1.059, 'C-F': 1.399, 'C-C': 1.53, 'C-SI': 1.888, 'C-X': 1.53, 'C-S': 1.819, 'C-P': 1.841, 'O-C': 1.413, 'H-X': 1.059, 'SI-BR': 2.284, 'O-H': 0.967, 'O-O': 1.469, 'O-N': 1.463, 'H-S': 1.35, 'O-S': 1.577, 'X-BR': 1.91, 'H-N': 1.009, 'H-O': 0.967, 'H-H': 0.74, 'X-SI': 1.888, 'O-X': 1.413, 'C-BR': 1.91, 'H-C': 1.059, 'F-X': 1.399, 'S-X': 1.819, 'S-S': 2.048, 'F-S': 1.64, 'F-P': 1.495, 'S-P': 1.954, 'F-N': 1.406, 'S-N': 1.633, 'S-I': 2.687, 'S-H': 1.35, 'S-F': 1.64, 'S-C': 1.819, 'F-C': 1.399, 'F-SI': 1.636, 'N-SI': 1.743, 'S-O': 1.577, 'S-BR': 2.321, 'SI-S': 2.145, 'I-C': 2.162, 'SI-P': 2.264, 'X-H': 1.059, 'X-I': 2.162, 'X-F': 1.399, 'SI-X': 1.888, 'X-C': 1.53, 'SI-C': 1.888, 'I-P': 2.49, 'I-S': 2.687, 'X-X': 1.53, 'SI-F': 1.636, 'I-X': 2.162, 'SI-O': 1.631, 'SI-N': 1.743, 'X-S': 1.819, 'N-BR': 1.843, 'I-N': 2.2, 'BR-S': 2.321, 'BR-P': 2.366, 'BR-SI': 2.284, 'BR-X': 1.91, 'BR-C': 1.91, 'BR-N': 1.843, 'S-SI': 2.145, 'N-CL': 1.743, 'X-N': 1.469, 'X-O': 1.413, 'S-CL': 2.283, 'P-S': 1.954, 'X-CL': 1.79, 'P-F': 1.495, 'SI-CL': 2.072, 'P-C': 1.841, 'P-N': 1.73, 'P-O': 1.662, 'P-I': 2.49, 'CL-C': 1.79, 'P-BR': 2.366, 'CL-N': 1.743, 'CL-S': 2.283, 'CL-P': 2.008, 'P-CL': 2.008, 'CL-X': 1.79, 'P-SI': 2.264, 'N-S': 1.633, 'N-P': 1.73, 'N-X': 1.469, 'N-F': 1.406, 'N-C': 1.469, 'N-N': 1.425, 'N-O': 1.463, 'N-H': 1.009, 'N-I': 2.2, 'SI-SI': 2.359, 'O-P': 1.662, 'O-SI': 1.631}, 'element_names_with_two_letters': ['BR', 'CL', 'BI', 'AS', 'AG', 'LI', 'MG', 'RH', 'ZN', 'MN'], 'max_number_of_bonds_permitted': {'C': 4, 'F': 1, 'I': 1, 'H': 1, 'O': 2, 'N': 4, 'P': 5, 'S': 6, 'BR': 1, 'Cl': 1, 'CL': 1}, 'dna_residues': ['A', 'C', 'G', 'T', 'DA', 'DA3', 'DA5', 'DAN', 'DC', 'DC3', 'DC4', 'DC5', 'DCN', 'DG', 'DG3', 'DG5', 'DGN', 'DT', 'DT3', 'DT5', 'DTN']}
    belongs_to_protein()
        True
    belongs_to_dna()
        False
    belongs_to_rna()
        False
    set_filename()
        test_name.pdb
    set_remarks()
        Test remark.
    set_coordinates()
        [999.999, 16.8, 35.823]
    set_atom_information()
        {'tempfactor': 12.04, 'chainid': 'A', 'record_name': 'ATOM  ', 'name': '  N  ', 'resname_stripped': 'GLN', 'occupancy': 1.0, 'element': ' N', 'resseq': 1, 'charge': '  \n', 'mass': 14.0067, 'element_stripped': 'N', 'resname': ' TST ', 'name_stripped': 'N', 'chainid_stripped': 'A', 'serial': 1}
    set_bonds()

Error: Cannot test set_bonds(). Install this recommended
       dependency: NUMPY

    serial_reindex()
    resseq_reindex()
    set_coordinates_undo_point()
    define_molecule_chain_residue_spherical_boundaries()

Error: Cannot calculate the spherical boundaries around
       molecules, chains, and residues. Install this
       recommended dependency: NUMPY

    get_hierarchy()

Error: Cannot test the get_hierarchy() function. Install
       this recommended dependency: NUMPY

    set_hierarchy()

Error: Cannot test the set_hierarchy() function. Install
       this recommended dependency: NUMPY

Selection Functions

Error: Cannot calculate bonds by distance. Install this
       recommended dependency: NUMPY

    select_all()
        Atoms in selection: 401
    select_atoms()
        Atoms in selection: 14
    invert_selection()
        Atoms in selection: 387
    select_all_atoms_bound_to_selection()

Error: Cannot test select_all_atoms_bound_to_selection().
       Install this recommended dependency: NUMPY

    select_atoms_near_other_selection()

Error: Cannot test select_atoms_near_other_selection().
       Install this recommended dependency: NUMPY

    select_atoms_in_same_residue()
        Atoms in selection: 1
    select_atoms_from_same_molecule()

Error: Cannot test select_atoms_from_same_molecule().
       Install this recommended dependency: NUMPY

    select_atoms_in_bounding_box()

Error: Cannot test select_atoms_in_bounding_box(). Install
       this recommended dependency: NUMPY

    select_branch()

Error: Cannot test select_branch(). Install this recommended
       dependency: NUMPY

    selections_of_constituent_molecules()

Error: Cannot test select_branch(). Install this recommended
       dependency: NUMPY

    selections_of_chains()

Error: Cannot test selections_of_chains(). Install this
       recommended dependency: NUMPY

    selections_of_residues()

Error: Cannot test selections_of_residues(). Install this
       recommended dependency: NUMPY

    select_close_atoms_from_different_molecules()

Error: Cannot test
       select_close_atoms_from_different_molecules().
       Install this recommended dependency: NUMPY

    get_molecule_from_selection()
        Atoms in selection: 5
Manipulation Functions
    set_coordinates_undo_point()
    translate_molecule()

Error: Cannot create a hierarchical organization of the
       molecule. Install this recommended dependency: NUMPY

    set_atom_location()

Error: Cannot create a hierarchical organization of the
       molecule. Install this recommended dependency: NUMPY

    rotate_molecule_around_a_line_between_points()

Error: Cannot create a hierarchical organization of the
       molecule. Install this recommended dependency: NUMPY

    rotate_molecule_around_a_line_between_atoms()

Error: Cannot create a hierarchical organization of the
       molecule. Install this recommended dependency: NUMPY


Error: Cannot create a hierarchical organization of the
       molecule. Install this recommended dependency: NUMPY

    rotate_molecule_around_pivot_point()

Error: Cannot test rotate_molecule_around_pivot_point().
       Missing the dot-product function. Install this
       recommended dependency: NUMPY

    rotate_molecule_around_pivot_atom()

Error: Cannot test rotate_molecule_around_pivot_atom().
       Missing the dot-product function. Install this
       recommended dependency: NUMPY

    coordinate_undo()
OtherMolecules Functions

Error: Cannot calculate bonds by distance. Install this
       recommended dependency: NUMPY


Error: Cannot calculate bonds by distance. Install this
       recommended dependency: NUMPY


Error: Cannot create a hierarchical organization of the
       molecule. Install this recommended dependency: NUMPY

    steric_clash_with_another_molecule()

Error: Cannot calculate the steric clashes with another
       molecule. Install this recommended dependency: NUMPY

        None

Error: Cannot calculate the steric clashes with another
       molecule. Install this recommended dependency: NUMPY

        None
    get_distance_to_another_molecule()

Error: Cannot calculate the distance to another molecule.
       Install this recommended dependency: NUMPY

        None

Error: Cannot calculate the distance to another molecule.
       Install this recommended dependency: NUMPY

        None
    get_rmsd_order_dependent()
        17.3205080757
    get_rmsd_heuristic()

Error: Cannot calculate an RMSD using a heuristical
       algorithm. Install this recommended dependency: NUMPY

        None
    get_rmsd_equivalent_atoms_specified()
        16.4684045068
    merge_with_another_molecule()
WHAT IS numpy.lib.recfunctions.stack_arrays?

Error: Cannot create a hierarchical organization of the
       molecule. Install this recommended dependency: NUMPY

    get_other_molecule_aligned_to_this()

Error: Cannot test get_other_molecule_aligned_to_this().
       Missing the dot-product function. Install this
       recommended dependency: NUMPY

AtomsAndBonds Functions
    add_atom()

Error: Cannot add atoms. Install this recommended
       dependency: NUMPY


Error: Cannot add atoms. Install this recommended
       dependency: NUMPY


Error: Cannot add atoms. Install this recommended
       dependency: NUMPY


Error: Cannot add atoms. Install this recommended
       dependency: NUMPY


Error: Cannot add atoms. Install this recommended
       dependency: NUMPY

    delete_atom()

Error: Cannot delete atoms. Install this recommended
       dependency: NUMPY

    add_bond()

Error: Cannot add bonds. Install this recommended
       dependency: NUMPY

    delete_bond()

Error: Cannot delete bonds. Install this recommended
       dependency: NUMPY

    create_bonds_by_distance()

Error: Cannot calculate bonds by distance. Install this
       recommended dependency: NUMPY

    get_number_of_bond_partners_of_element()

Error: Cannot count the number of bond partners of a given
       element. Install this recommended dependency: NUMPY

        None
    get_index_of_first_bond_partner_of_element()

Error: Cannot get the index of a bond partner of element X.
       Install this recommended dependency: NUMPY

        None
Geometry Functions
    get_angle_between_three_points()

Error: Cannot calculate the angle between three points.
       Missing the dot-product function. Install this
       recommended dependency: NUMPY

        None
    get_dihedral_angle()

Error: Cannot calculate the angle between three points.
       Missing the cross-product function. Install this
       recommended dependency: NUMPY

        None
    is_planar()
        True
    get_planarity_deviation()
        0.0
