import scoria
import numpy as np

class Contact():
    """
    A class for managing molecule subsections and calculating where they
    make contact.
    """

    def __init__(self, molecule):
        """
        Initializes the Contact object.

        :param scoria.molecule molecule: A molecule from which to calculate
        contact points.
        """

        self.__molecule = molecule
        self.__serials1 = None
        self.__serials2 = None

        self.__subsection_1 = None
        self.__subsection_2 = None

        self.__contacts = None
        self.__contact_count = [np.array([]), np.array([])]

    def set_subsections(self, resids_1, resids_2):
        """
        Given two sets on indexes, creates the subsection molecules.

        :param list resids_1: A list of indexes of the atoms to include in subsection one.

        :param list resids_2: a list of indexes of the atoms to include in subsection two.
        """

        self.__serials1 = self.__molecule.select_atoms({'resseq':resids_1}) 
        self.__serials2 = self.__molecule.select_atoms({'resseq':resids_2}) 

        self.__subsection_1 = self.__get_molecule_from_serials(self.__serials1)
        self.__subsection_2 = self.__get_molecule_from_serials(self.__serials2)

        self.__clean_contact_counts()

    def __clean_contact_counts(self):
        """
        Reinitalizes the __contact_counts to full 0.0 dictionaries.
        """
        if (self.__serials1 is None) or (self.__serials2 is None):
            return

        """
        Should be faster with numpy arrays...
        for index in xrange(0, len(self.__serials1)):
            self.__contact_count[0][index] = float(0.0)

        for index in xrange(0, len(self.__serials2)):
            self.__contact_count[1][index] = float(0.0)
        """

        self.__contact_count[0] = np.zeros(self.__subsection_1.get_total_number_of_atoms())
        self.__contact_count[1] = np.zeros(self.__subsection_2.get_total_number_of_atoms())


    def __get_molecule_from_serials(self, serial_list):
        """
        Creates a subsection molecule from a given list of serials.

        :param list serial_list: A list of atom serial numbers.
        """

        criteria = {'serial':serial_list}
        #import pdb; pdb.set_trace()
        selection = self.__molecule.select_atoms(criteria)
        return self.__molecule.get_molecule_from_selection(selection, False)


    def calculate_contact(self):
        """
        Given the two subsections, steps through the trajectory and counts
        the number of contacts between the two subsections.
        """

        trajectory_length = self.__molecule.get_trajectory_frame_count()

        for frame in xrange(0, trajectory_length):
            self.__subsection_1.set_default_trajectory_frame(frame)
            self.__subsection_2.set_default_trajectory_frame(frame)
            self.__contacts = self.__subsection_1.select_close_atoms_from_different_molecules(self.__subsection_2, 3)

            for i, atoms in enumerate(self.__contacts):
                for atom in atoms:
                    self.__contact_count[i][atom] += 1.0

        self.__normalize_counts()
        self.__save_contacts_to_occupancy()

    def __normalize_counts(self):
        """
        Normalizes the counts between 0.0 - 1.0 by dividing against the
        global maximum.
        """

        """
        Will be faster using numpy...
        max_value = max(max(self.__contact_count[0].values()),
                        max(self.__contact_count[1].values()))

        for count in self.__contact_count:
            for key in count.keys():
                count[key] = float(count[key]) / max_value
        """

        max_value = max(self.__contact_count[0].max(), self.__contact_count[1].max())
        
        self.__contact_count[0] = self.__contact_count[0] / max_value
        self.__contact_count[1] = self.__contact_count[1] / max_value

    def __save_contacts_to_occupancy(self):
        """
        Inserts normalized count data into the subsection's occupancy field.
        """

        atom_information = [self.__subsection_1.get_atom_information(),
                            self.__subsection_2.get_atom_information()]

        """
        numpy will be faster...
        for i, atom_info in enumerate(atom_information):
            for key in self.__contact_count[i].keys():
                atom_info['occupancy'][int(key)] = self.__contact_count[i][key]
        """

        atom_information[0]["occupancy"] = self.__contact_count[0]
        atom_information[1]["occupancy"] = self.__contact_count[1]

        # print len(atom_information[0]["occupancy"])
        # print len()
        # print len(atom_information[1]["occupancy"])
        # print len(self.__contact_count[1])

        # print atom_information[0]["occupancy"]
        # print self.__serials1
        # print self.__contact_count[0]

        # import pdb; pdb.set_trace()

        self.__subsection_1.set_atom_information(atom_information[0])
        self.__subsection_2.set_atom_information(atom_information[1])

    def print_subcomponents(self, section_one_name, section_two_name):
        """
        Prints the subcomponents to two PDB files.

        :param str section_one_name: Filename for the first component
        :param str section_two_name: Filename for the second componenet
        """

        self.__subsection_1.save_pdb(section_one_name, False)
        self.__subsection_2.save_pdb(section_two_name, False)
