# Define constants
MIN_NUM_CODONS = 5
MIN_GC_CONTENT = 30
UNIQUE_NUC = 4
NUM_NUC_PER_CODON = 3

# Define main function
def main():
    # Print the intro of the program
    print('This program reports information about DNA\nnucleotide sequences that may encode proteins.')

    # Call the function to get a file
    get_file_data()

# Define the function to get a file
def get_file_data():
    # Get the file name from the user
    file_name = input('Input file name? ')

    # Propmt the output name
    output_name = input('Output file name? ')

    # Call the function to analyze file data
    analyze_file_data(file_name, output_name)

# Define the function to analyze file data
def analyze_file_data(data_file, output_name):

    # initialize the data dictionary
    data = {
        "data": [
            
        ]
    }

    # opent ht edata file
    with open(data_file) as d_file:
        # read every two lines of the file
        for line1, line2 in zip(d_file, d_file):

            # Get the region name
            region_name = line1.strip()

            # Get the nucleotide sequence
            nucleotide_sequence = line2.strip().replace('-','').upper()

            # analyze the nucleotide sequence
            nuc_a_count = nucleotide_sequence.count('A')
            nuc_c_count = nucleotide_sequence.count('C')
            nuc_g_count = nucleotide_sequence.count('G')
            nuc_t_count = nucleotide_sequence.count('T')
            
            # calc total mass
            total_mass = (nuc_a_count * 135.128) + (nuc_c_count * 111.103) + (nuc_g_count * 151.128) + (nuc_t_count * 125.107)

            # calc total mass % of each nucleotide
            nuc_a_mass = round(((nuc_a_count * 135.128) / total_mass) * 100, 1)
            nuc_c_mass = round(((nuc_c_count * 111.103) / total_mass) * 100, 1)
            nuc_g_mass = round(((nuc_g_count * 151.128) / total_mass) * 100, 1)
            nuc_t_mass = round(((nuc_t_count * 125.107) / total_mass) * 100, 1)

            # get codons list
            codons_list = []
            for i in range(0, len(nucleotide_sequence), NUM_NUC_PER_CODON):
                codons_list.append(nucleotide_sequence[i:i+NUM_NUC_PER_CODON])

            # Determin if the sequence is a protein
            is_protein = False
            if (codons_list[0] == 'ATG' and codons_list[-1] == 'TAA' or codons_list[-1] == 'TAG' or codons_list[-1] == 'TGA' and len(codons_list) >= MIN_NUM_CODONS and (nuc_c_mass + nuc_g_mass) >= MIN_GC_CONTENT):
                is_protein = True

            # append the data to the dictionary
            data['data'].append({ "regionName": region_name, "nucleotideSequence": nucleotide_sequence, "nucCounts": [nuc_a_count, nuc_c_count, nuc_g_count, nuc_t_count], "totalMass": [nuc_a_mass, nuc_c_mass, nuc_g_mass, nuc_t_mass], "codonsList": codons_list, "isProtein": is_protein })

    # Call the function to output the data
    output_data(output_name, data, len(data['data']) - 1)

# Define the output data function
def output_data(output_name, data, region_count):

    # Open the output file
    output_file = open(output_name, 'w')
    
    # loop for every region
    for i in range(region_count):

        # Get the regions values from the dict
        region_name = data['data'][i]['regionName']
        nucleotide_sequence = data['data'][i]['nucleotideSequence']
        nuc_counts = data['data'][i]['nucCounts']
        total_mass = data['data'][i]['totalMass']
        codons_list = data['data'][i]['codonsList']
        is_protein = data['data'][i]['isProtein']
        
        # Properly format the is_protein value
        if (is_protein):
            is_protein = 'YES'
        else:
            is_protein = 'NO'

        # Write the data to the output file
        output_file.write(f'Region Name: {region_name}\nNucleotides: {nucleotide_sequence}\nNuc. Counts: {nuc_counts}\nTotal Mass%: {total_mass}\nCodons List: {codons_list}\nIs Protein: {is_protein}\n\n')

# Call main function
main()