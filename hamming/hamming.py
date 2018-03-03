def distance(dna_strand1, dna_strand2):
    """Calculate hamming distance between two DNA strands."""
    if len(dna_strand1) != len(dna_strand2):
        raise ValueError
    counter = 0
    for i in range(len(dna_strand1)):
        if dna_strand1[i] != dna_strand2[i]:
            counter += 1

    return counter
