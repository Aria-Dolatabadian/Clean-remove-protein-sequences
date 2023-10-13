def read_fasta(fasta_file):
    sequences = {}
    current_seq = ""
    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_seq = line
                sequences[current_seq] = ""
            else:
                sequences[current_seq] += line
    return sequences

def write_fasta(sequences, output_file):
    with open(output_file, "w") as file:
        for header, sequence in sequences.items():
            file.write(header + "\n")
            file.write(sequence + "\n")

def remove_asterisks(sequences):
    cleaned_sequences = {}
    for header, sequence in sequences.items():
        cleaned_sequence = sequence.replace("*", "")
        cleaned_sequences[header] = cleaned_sequence
    return cleaned_sequences

input_fasta = "protein seq.fasta"
output_fasta = "clean protein seq.fasta"

sequences = read_fasta(input_fasta)
cleaned_sequences = remove_asterisks(sequences)
write_fasta(cleaned_sequences, output_fasta)
