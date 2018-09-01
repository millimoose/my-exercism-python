_complements = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand):
    return str.join("", (_complements[nucl] for nucl in dna_strand))
