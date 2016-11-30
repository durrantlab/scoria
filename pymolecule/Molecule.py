from pymolecule import dumbpy as numpy
from FileIO import FileIO
from AtomsAndBonds import AtomsAndBonds
from Selections import Selections
from Manipulation import Manipulation
from Information import Information
from OtherMolecules import OtherMolecules
from Geometry import Geometry
import copy


class Molecule: # here's the actual Molecule class
    """
    Loads, saves, and manupulates molecuar models. The main pymolecule
    class. Contains alias functions for subclasses.

    Examples assume::

        >>> import pymolecule
        >>> PSF = "./test_file.psf"
        >>> DCD = "./test_file.dcd"
        >>> mol = pymolecule.Molecule()
        >>> mol.load_via_MDAnalysis(PSF, DCD)
    """

    def __init__ (self):
        """Initializes the variables of the Molecule class."""

        self.fileio = FileIO(self)
        self.atoms_and_bonds = AtomsAndBonds(self)
        self.selections = Selections(self)
        self.manipulation = Manipulation(self)
        self.information = Information(self)
        self.other_molecule = OtherMolecules(self)
        self.geometry = Geometry(self)

    # Information methods
    ### Aliases ###
    # Gets
    def get_coordinates(self, frame = 0):
        """
        Returns the set of coordinates from the specified frame.
        Alias function for Information.get_coordinates().

        :param int frame: The timestep from which the coordinates shoule be 
                        returned. If ommitted, it defaults to the first 
                        frame of the trajectory.
        
        :returns: The set of coordinates from the specified frame.
                    ::

                    [[x1, y1, z1], ... [xn, yn, zn]]

        :rtype: *numpy.array*

        ::

            >>> print mol.get_coordinates()
            [[ -30.85199928  -81.45800018  365.05499268]
             [ -31.99500084  -80.69300079  365.66900635]
             [ -32.0530014   -81.13200378  367.18200684]
             ..., 
             [ -27.54199982  -96.25099945  402.83700562]
             [ -23.54199982  -94.7539978   400.41900635]
             [ -22.86100006  -93.72499847  400.55300903]]
             
            >>> print mol.get_coordinates(2)
            [[ -28.88899994  -80.45700073  365.51699829]
             [ -30.20000076  -79.73699951  365.99700928]
             [ -30.90699959  -80.5510025   367.13000488]
             ..., 
             [ -26.0189991   -97.28099823  403.52600098]
             [ -23.2140007   -94.73999786  400.94699097]
             [ -22.52899933  -93.73300171  400.81399536]]
        """
        
        return self.information.get_coordinates(frame)

    def get_trajectory(self):
        """
        Returns the trajectory for the molecule.
        Alias function for Information.get_trajectory().
        
        :returns: The set of all coordinates.
                    ::
                
                        [[[x11, y11, z11], ... [x1n, y1n, z1n]],
                         ...,
                         [[xm1, ym1, zm1], ... [xmn, ymn, zmn]]] 

        :rtype: *numpy.array*

        ::

            >>> for coord in mol.get_trajectory():
            >>>     print coord
            >>>     print
            [[ -30.85199928  -81.45800018  365.05499268]
             [ -31.99500084  -80.69300079  365.66900635]
             [ -32.0530014   -81.13200378  367.18200684]
             ..., 
             [ -27.54199982  -96.25099945  402.83700562]
             [ -23.54199982  -94.7539978   400.41900635]
             [ -22.86100006  -93.72499847  400.55300903]]

            [[ -30.6779995   -81.32499695  365.73199463]
             [ -31.88100052  -80.38600159  366.0289917 ]
             [ -32.40399933  -80.62799835  367.45700073]
             ..., 
             [ -27.44400024  -96.71099854  402.64700317]
             [ -23.79199982  -94.58899689  400.63598633]
             [ -23.10700035  -93.56300354  400.79598999]]
             <more>
        """

        return self.information.get_trajectory()

    def get_filename(self):
        """
        Returns the filename that the molecule was originally loaded from.
        Alias function for Information.get_filename()
        
        :returns: The name of the file.

        :rtype: *str*

        ::

            >>> mol = pymolecule.Molecule()
            >>> mol.load_pdb_into("single_frame.pdb")
            >>> print mol.get_filename()
            single_frame.pdb
        """
        
        return self.information.get_filename()

    def get_remarks(self):
        """
        Returns the remarks from the file the molecule was loaded from.
        Alias function for Information.get_remarks()
        
        :returns: The remarks from the file an a list of strings.

        :rtype: *list*

        ::

            >>> mol = pymolecule.Molecule()
            >>> mol.load_pdb_into("single_frame.pdb")
            >>> print mol.get_remarks()
            [' This is a remark.']
        """
        
        return self.information.get_remarks()

    def get_atom_information(self):
    	"""
        Retreives the atomic information for the molecule.
        Alias function for Information.get_atom_information()

        :returns: A masked array containing the atom information.

        :rtype: *numpy.ma* 

        The contents of the array are as follows:

        ================ ===== ================= ==============================
        member name      dtype Full Type         Description
        ================ ===== ================= ==============================
        record_name      S6    six char string   What the atom belongs to
        serial           <i8   64-bit integer    The index of the atom
        name             S5    five char string  The atom name
        resname          S5    five char string  The residue name
        chainid          S1    one char string   The chain identifier
        resseq           <i8   64-bit integer    The Residue sequence number   
        occupancy        <f8   64-bit float      Occupancy of atom
        tempfactor       <f8   64-bit float      Tempature Factor
        element          S2    two char string   The element symbol
        charge           S3    three char string Charge on the atom
        name_stripped    S5    five char string  Atom name without space
        resname_stripped S5    five char string  Residue name without space
        chainid_stripped S1    one char string   Chain identifier without space
        element_stripped S2    two char string   Element symbol without space
        ================ ===== ================= ==============================
        |

        An example for printing the elemental symbols of the first five atoms::

            >>> atom_info = mol.get_atom_information()
            >>> print atom_info['element_stripped'][0:5]
            ['N' 'C' 'C' 'O' 'C']
        """

        return self.information.get_atom_information()

    def get_coordinates_undo_point(self):
        """
        NEEDS CLARIFICATION.
        Retreives a previously save set of coordinates to revert to.
        Alias function for Information.get_coordinates_undo_point()

        :returns: A set of coordinates from which to return to.

        :rtype: *numpy.array* or *None*
        """

        return self.information.get_coordinates_undo_point()

    def get_bonds(self):
        """
        Retreives the bonds beteween atoms as a n x n matrix.
        Alias function for Information.get_bonds()

        :returns: A binary n x n matrix, where bonds are represented by 1.

        :rtype: *numpy.array*

        An example for finding all atoms bonded with atom 153::

            >>> bonds = mol.get_bonds()
            >>> for i in xrange(0,len(bonds)):
            ...     if bonds[153][i] == 1:
            ...             print 153,"-",i
            153 - 152
            153 - 154
            153 - 155


        """
        
        return self.information.get_bonds()

    def get_hierarchy(self):
        """
        NEEDS CLARIFICATION.
        Alias function for Information.get_hierarchy()

        :returns: A dictionary?

        :rtype: *dict*
        """
        
        return self.information.get_hierarchy()

    def get_constants(self):
        """
        Returns a dictionary containing the constants assumed for the molecular model.
        Alias function for Information.get_constants()

        :returns: The constants assumed by the model.

        :rtype: *dict*

        ============================== =============== ===============================
        Dictionary Keys                Value Type      Contains
        ============================== =============== ===============================
        mass_dict                      dict{str:float} The mass of elements
        rna_residues                   list(str)       RNA residue names
        f8_fields                      list(str)       Atom Information floats
        vdw_dict                       dict{str:float} Van der Waals force of elements
        i8_fields                      list(str)       Atom Information integers
        protein_residues               list(str)       Protein residue names
        bond_length_dict               dict{str:float} Element-pair bond length 
        element_names_with_two_letters list(str)       Element symbols with 2 letters
        max_number_of_bonds_permitted  dict{str:int}   Max bonds per element
        dna_residues                   list(str)       DNA reside names
        ============================== =============== ===============================

        """
        
        return self.information.get_constants()

    def get_center_of_mass(self, selection = None):
        """
        Alias function for Information.get_center_of_mass()

        :param numpy.array selection: The indices of
                          the atoms to consider when calculating the center of mass. 
                          If ommitted, all atoms of the pymolecule.Molecule object 
                          will be considered.

        :param int frame: The timestep at which the geometric center 
                      should be calculated. If ommitted, it defaults to the first 
                      frame of the trajectory.
        
        :returns: The x, y, and z coordinates of the geometric center.

        :rtype: *numpy.array*

        ::

            >>> mol = pymolecule.Molecule()
            >>> mol.load_pdb_into("single_frame.pdb")
            >>> print mol.get_geometric_center()
            [ 33.09860848  19.1221197   16.0426808 ]
        """
        
        return self.information.get_center_of_mass(selection)

    def get_geometric_center(self, selection = None):
        """
        Determines the geometric center of the molecule.
        Alias function for Information.get_geometric_center()

        :param numpy.array selection: The indices of
                          the atoms to consider when calculating the geometric. 
                          If ommitted, all atoms of the pymolecule.Molecule object 
                          will be considered.

        :param int frame: The timestep at which the geometric center 
                      should be calculated. If ommitted, it defaults to the first 
                      frame of the trajectory.
        
        :returns: The x, y, and z coordinates of the geometric center.

        :rtype: *numpy.array*

        ::

            >>> mol = pymolecule.Molecule()
            >>> mol.load_pdb_into("single_frame.pdb")
            >>> print mol.get_geometric_center()
            [ 33.09860848  19.1221197   16.0426808 ]
        """

        return self.information.get_geometric_center(selection)

    def get_total_mass(self, selection = None):
        """Alias function for Information.get_total_mass()"""
        
        return self.information.get_total_mass(selection)

    def get_total_number_of_atoms(self, selection = None):
        """Alias function for Information.get_total_number_of_atoms()"""
        
        return self.information.get_total_number_of_atoms(selection)

    def get_total_number_of_heavy_atoms(self, selection = None):
        """Alias function for Information.get_total_number_of_heavy_atoms()"""
        
        return self.information.get_total_number_of_heavy_atoms(selection)

    def get_bounding_box(self, selection = None, padding = 0.0):
        """Alias function for Information.get_bounding_box()"""
        
        return self.information.get_bounding_box(selection, padding)

    def get_bounding_sphere(self, selection = None, padding = 0.0):
        """Alias function for Information.get_bounding_sphere()"""
        
        return self.information.get_bounding_sphere(selection, padding)

    # Set
    def set_filename(self, filename):
        """Alias function for Information.set_filename()"""
        
        self.information.set_filename(filename)

    def set_remarks(self, remarks):
        """Alias function for Information.set_remarks()"""
        
        self.information.set_remarks(remarks)

    def set_atom_information(self, atom_information):
        """Alias function for Information.set_atom_information()"""
        
        self.information.set_atom_information(atom_information)

    def set_coordinates(self, coordinates, frame = 0):
        """Alias function for Information.set_coordinates()"""
        
        self.information.set_coordinates(coordinates, frame)

    def set_trajectory(self, trajectory):
        """Alias function for Information.set_trajectory()"""

        self.information.set_trajectory(trajectory)

    def set_coordinates_undo_point(self, coordinates_undo_point):
        """Alias function for Information.set_coordinates_undo_point()"""
        
        self.information.set_coordinates_undo_point(coordinates_undo_point)

    def set_bonds(self, bonds):
        """Alias function for Information.set_bonds()"""
        
        self.information.set_bonds(bonds)

    def set_hierarchy(self, hierarchy):
        """Alias function for Information.set_hierarchy()"""
        
        self.information.set_hierarchy(hierarchy)

    # Information functions
    def assign_masses(self):
        """Alias function for Information.assign_masses()"""
        
        self.information.assign_masses()

    def assign_elements_from_atom_names(self, selection = None):
        """Alias function for Information.assign_elements_from_atom_names()"""
        
        self.information.assign_elements_from_atom_names(selection)

    def define_molecule_chain_residue_spherical_boundaries(self):
        """Alias function for Information.define_molecule_chain_residue_spherical_boundaries()"""
        
        self.information.define_molecule_chain_residue_spherical_boundaries()

    def serial_reindex(self):
        """Alias function for Information.serial_reindex()"""
        
        self.information.serial_reindex()

    def resseq_reindex(self):
        """Alias function for Information.resseq_reindex()"""
        
        self.information.resseq_reindex()
    
    def belongs_to_protein(self, atom_index):
        """Alias function for Information.belongs_to_protein()"""
        
        return self.information.belongs_to_protein(atom_index)

    def belongs_to_rna(self, atom_index):
        """Alias function for Information.belongs_to_rna()"""
        
        return self.information.belongs_to_rna(atom_index)

    def belongs_to_dna(self, atom_index):
        """Alias function for Information.belongs_to_dna()"""
        
        return self.information.belongs_to_dna(atom_index)

    def insert_trajectory_frame(self, index, coordinates):
        """Alias function for Information.insert_trajectory_frame()"""

        return self.information.insert_trajectory_frame(index, coordinates)
    
    def delete_trajectory_frame(self, index):
        """Alias function for Information.delete_trajectory_frame()"""

        return self.information.delete_trajectory_frame(index)

    def get_trajectory_frame_count(self):
        """Alias function for Information.get_trajectory_frame_count()"""

        return self.information.get_trajectory_frame_count()

    # File I/O class methods
    def load_pym_into(self, filename):
        """Alias function for FileIO.load_pym_into(filename)"""
        
        self.fileio.load_pym_into(filename)

    def load_pdb_into(self, filename, bonds_by_distance = True,
                      serial_reindex = True, resseq_reindex = False):
        """Alias function for FileIO.load_pdb_into("""

        self.fileio.load_pdb_into(
            filename, bonds_by_distance, serial_reindex, resseq_reindex
        )

    def load_pdb_into_using_file_object(self, file_obj,
                                        bonds_by_distance = True,
                                        serial_reindex = True,
                                        resseq_reindex = False):
        """Alias function for FileIO.load_pdb_into_using_file_object()"""

        self.fileio.load_pdb_into_using_file_object(
            file_obj, bonds_by_distance, serial_reindex, resseq_reindex
        )

    def load_pdbqt_into(self, filename, bonds_by_distance = False,
                      serial_reindex = True, resseq_reindex = False):
        """Alias function for FileIO.load_pdbqt_into()"""

        self.fileio.load_pdbqt_into(
            filename, bonds_by_distance, serial_reindex, resseq_reindex
        )

    def load_pdbqt_into_using_file_object(self, file_obj,
                                        bonds_by_distance = False,
                                        serial_reindex = True,
                                        resseq_reindex = False):
        """Alias function for FileIO.load_pdbqt_into_using_file_object()"""

        self.fileio.load_pdbqt_into_using_file_object(
            file_obj, bonds_by_distance, serial_reindex, resseq_reindex
        )

    def save_pym(self, filename, save_bonds = False, save_filename = False,
                 save_remarks = False, save_hierarchy = False,
                 save_coordinates_undo_point = False):
        """Alias function for FileIO.save_pym()"""

        self.fileio.save_pym(
            filename, save_bonds, save_filename, save_remarks,
            save_hierarchy, save_coordinates_undo_point
        )

    def save_pdb(self, filename = "", serial_reindex = True,
                 resseq_reindex = False, return_text = False):
        """Alias function for FileIO.save_pdb()"""

        return self.fileio.save_pdb(
            filename, serial_reindex, resseq_reindex, return_text
        )

    def load_via_MDAnalysis(self, *args):
        """Alias function for FileIO.load_via_MDAnalysis()"""

        self.fileio.load_via_MDAnalysis(*args)

    # Atoms and Bonds class methods
    def get_number_of_bond_partners_of_element(self, atom_index, the_element):
        """Alias function for AtomsAndBonds.get_number_of_bond_partners_of_element()"""

        return self.atoms_and_bonds.get_number_of_bond_partners_of_element(
            atom_index, the_element
        )

    def get_index_of_first_bond_partner_of_element(self, atom_index,
                                                   the_element):
        """Alias function for AtomsAndBonds.get_index_of_first_bond_partner_of_element()"""

        return self.atoms_and_bonds.get_index_of_first_bond_partner_of_element(
            atom_index, the_element
        )

    def create_bonds_by_distance(self, remove_old_bond_data = True,
                                 delete_excessive_bonds = True):
        """Alias function for AtomsAndBonds.create_bonds_by_distance()"""

        self.atoms_and_bonds.create_bonds_by_distance(
            remove_old_bond_data, delete_excessive_bonds
        )

    def delete_bond(self, index1, index2):
        """Alias function for AtomsAndBonds.delete_bond()"""
        
        self.atoms_and_bonds.delete_bond(index1, index2)

    def add_bond(self, index1, index2, order = 1):
        """Alias function for AtomsAndBonds.add_bond()"""
        
        self.atoms_and_bonds.add_bond(index1, index2, order)

    def delete_atom(self, index):
        """Alias function for AtomsAndBonds.delete_atom()"""
        
        self.atoms_and_bonds.delete_atom(index)

    def add_atom(self, record_name = "ATOM", serial = 1, name = "X",
                 resname = "XXX", chainid = "X", resseq = 1, occupancy = 0.0,
                 tempfactor = 0.0, charge = '', element = "X",
                 coordinates = numpy.array([0.0, 0.0, 0.0]), autoindex = True):
        """Alias function for AtomsAndBonds.add_atom()"""

        self.atoms_and_bonds.add_atom(
            record_name, serial, name, resname, chainid, resseq, occupancy,
            tempfactor, charge, element, coordinates, autoindex
        )

    # Selections class
    def get_molecule_from_selection(self, selection, serial_reindex = True,
                                    resseq_reindex = False):
        """Alias function for Selections.get_molecule_from_selection()"""

        return self.selections.get_molecule_from_selection(
            selection, serial_reindex, resseq_reindex
        )

    def select_atoms(self, selection_criteria):
        """Alias function for Selections.select_atoms()"""
        
        return self.selections.select_atoms(selection_criteria)

    def select_atoms_in_bounding_box(self, bounding_box):
        """Alias function for Selections.select_atoms_in_bounding_box()"""
        
        return self.selections.select_atoms_in_bounding_box(bounding_box)

    def select_branch(self, root_atom_index, directionality_atom_index):
        """Alias function for Selections.select_branch()"""
        
        return self.selections.select_branch(
            root_atom_index, directionality_atom_index
        )

    def select_all_atoms_bound_to_selection(self, selections):
        """Alias function for Selections.select_all_atoms_bound_to_selection()"""
        
        return self.selections.select_all_atoms_bound_to_selection(selections)

    def select_atoms_from_same_molecule(self, selection):
        """Alias function for Selections.select_atoms_from_same_molecule()"""
        
        return self.selections.select_atoms_from_same_molecule(selection)

    def selections_of_constituent_molecules(self):
        """Alias function for Selections.selections_of_constituent_molecules()"""
        
        return self.selections.selections_of_constituent_molecules()

    def select_atoms_near_other_selection(self, selection, cutoff):
        """Alias function for Selections.select_atoms_near_other_selection()"""
        
        return self.selections.select_atoms_near_other_selection(
            selection, cutoff
        )

    def select_atoms_in_same_residue(self, selection):
        """Alias function for Selections.select_atoms_in_same_residue()"""
        
        return self.selections.select_atoms_in_same_residue(selection)

    def invert_selection(self, selection):
        """Alias function for Selections.invert_selection()"""
        
        return self.selections.invert_selection(selection)

    def select_all(self):
        """Alias function for Selections.select_all()"""
        
        return self.selections.select_all()

    def select_close_atoms_from_different_molecules(self, other_mol, cutoff,
                                                    pairwise_comparison = True,
                                                    terminate_early = False):
        """Alias function for Selections.select_close_atoms_from_different_molecules()"""

        return self.selections.select_close_atoms_from_different_molecules(
            other_mol, cutoff, pairwise_comparison, terminate_early
        )

    def selections_of_chains(self):
        """Alias function for Selections.selections_of_chains()"""
        
        return self.selections.selections_of_chains()

    def selections_of_residues(self):
        """Alias function for Selections.selections_of_residues()"""
        
        return self.selections.selections_of_residues()

    # Manipulation class
    def set_atom_location(self, atom_index, new_location):
        """Alias function for Manipulation.set_atom_location()"""
        
        return self.manipulation.set_atom_location(atom_index, new_location)

    def coordinate_undo(self):
        """Alias function for Manipulation.coordinate_undo()"""
        
        self.manipulation.coordinate_undo()

    def translate_molecule(self, delta):
        """Alias function for Manipulation.translate_molecule()"""
        
        self.manipulation.translate_molecule(delta)

    def rotate_molecule_around_a_line_between_points(self, line_point1,
                                                     line_point2, rotate):
        """Alias function for Manipulation.rotate_molecule_around_a_line_between_points()"""

        self.manipulation.rotate_molecule_around_a_line_between_points(
            line_point1, line_point2, rotate
        )

    def rotate_molecule_around_a_line_between_atoms(self, line_point1_index,
                                                    line_point2_index, rotate):
        """Alias function for Manipulation.rotate_molecule_around_a_line_between_atoms()"""

        self.manipulation.rotate_molecule_around_a_line_between_atoms(
            line_point1_index, line_point2_index, rotate
        )

    def rotate_molecule_around_pivot_point(self, pivot, thetax,
                                           thetay, thetaz):
        """Alias function for Manipulation.rotate_molecule_around_pivot_point()"""

        self.manipulation.rotate_molecule_around_pivot_point(
            pivot, thetax, thetay, thetaz
        )

    def rotate_molecule_around_pivot_atom(self, pivot_index, thetax,
                                          thetay, thetaz):
        """Alias function for Manipulation.rotate_molecule_around_pivot_atom()"""

        self.manipulation.rotate_molecule_around_pivot_atom(
            pivot_index, thetax, thetay, thetaz
        )

    # Geometry class
    def get_angle_between_three_points(self, pt1, pt2, pt3):
        """Alias function for Geometry.get_angle_between_three_points()"""
        
        return self.geometry.get_angle_between_three_points(pt1, pt2, pt3)

    def get_dihedral_angle(self, pt1, pt2, pt3, pt4):
        """Alias function for Geometry.get_dihedral_angle()"""
        
        return self.geometry.get_dihedral_angle(pt1, pt2, pt3, pt4)

    def get_planarity_deviation(self, pt1, pt2, pt3, pt4):
        """Alias function for Geometry.get_planarity_deviation()"""
        
        return self.geometry.get_planarity_deviation(pt1, pt2, pt3, pt4)

    def is_planar(self, pt1, pt2, pt3, pt4, planarity_cutoff = 0.2):
        """Alias function for Geometry.is_planar()"""
        
        return self.geometry.is_planar(pt1, pt2, pt3, pt4, planarity_cutoff)

    # Other molecule class
    def get_other_molecule_aligned_to_this(self, other_mol, tethers):
        """Alias function for OtherMolecules.get_other_molecule_aligned_to_this()"""

        # Add Weight Matrix
        return self.other_molecule.get_other_molecule_aligned_to_this(
            other_mol, tethers
        )

    def get_distance_to_another_molecule(self, other_molecule,
                                         pairwise_comparison = True):
        """Alias function for OtherMolecules.get_distance_to_another_molecule()"""

        return self.other_molecule.get_distance_to_another_molecule(
            other_molecule, pairwise_comparison
        )

    def get_rmsd_equivalent_atoms_specified(self, other_mol, tethers):
        """Alias function for OtherMolecules.get_rmsd_equivalent_atoms_specified()"""

        return self.other_molecule.get_rmsd_equivalent_atoms_specified(
            other_mol, tethers
        )

    def get_rmsd_order_dependent(self, other_mol):
        """Alias function for OtherMolecules.get_rmsd_order_dependent()"""
        
        return self.other_molecule.get_rmsd_order_dependent(other_mol)

    def get_rmsd_heuristic(self, other_mol):
        """Alias function for OtherMolecules.get_rmsd_heuristic()"""
        
        return self.other_molecule.get_rmsd_heuristic(other_mol)

    def steric_clash_with_another_molecule(self, other_mol, cutoff,
                                           pairwise_comparison = True):
        """Alias function for OtherMolecules.steric_clash_with_another_molecule()"""

        return self.other_molecule.steric_clash_with_another_molecule(
            other_mol, cutoff, pairwise_comparison
        )

    def merge_with_another_molecule(self, other_molecule):
        """Alias function for OtherMolecules.merge_with_another_molecule()"""
        
        return self.other_molecule.merge_with_another_molecule(other_molecule)

    ######## Supporting functions ########

    def numpy_structured_array_remove_field(self, narray, field_names):
        """Removes a specific field name from a structured numpy array.

            Args::
                narray -- A structured numpy array.
                field_names -- A list of strings, where each string is one of
                    the field names of narray.

            Returns:
                A structured numpy array identical to narray, but with the
                    field names in field_names removed.

        """

        # surprised this doesn't come with numpy

        # now remove the coordinates from the atom_information object to save
        # memory
        names = list(narray.dtype.names)
        for f in field_names:
            names.remove(f)
        
        return narray[names]

    def __is_number(self, s):
        """Determines whether or not a string represents a number.

            Args::
                s -- A string (e.g., "5.4").

            Returns:
                A boolean, whether or not the string can be represented by a
                    float.

        """

        try:
            float(s)
            return True
        except ValueError:
            return False

    def copy(self):
        """Returns an exact copy (pymolecule.Molecule) of this Molecule object.
        Undo points are NOT copied.

            Returns:
                A pymolecule.Molecule, containing to the same atomic
                    information as this pymolecule.Molecule object.

        """

        new_molecule = Molecule()
        new_molecule.set_filename(self.get_filename()[:])
        new_molecule.set_remarks(self.get_remarks()[:])
        new_molecule.set_atom_information(self.get_atom_information().copy())
        new_molecule.set_coordinates(self.get_coordinates().copy())

        if not self.get_bonds() is None:
            new_molecule.set_bonds(self.get_bonds().copy())
        else:
            new_molecule.set_bonds(None)

        new_molecule.set_hierarchy(copy.deepcopy(self.get_hierarchy()))

        return new_molecule
