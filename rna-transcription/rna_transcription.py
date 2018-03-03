transcription = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand):
    """Transform DNA to RNA."""
    result = ''
    for nucleotide in dna_strand:
        rna = transcription.get(nucleotide)
        if not rna:
            return ''
        result += rna

    return result
