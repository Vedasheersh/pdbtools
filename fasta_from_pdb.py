def fasta_from_pdb(pdbfile):
    pdbf = open(pdbfile)

    letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
               'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
               'TYR':'Y','VAL':'V'}

    prev_res = None
    seq = {}
    for line in pdbf:
        if line.startswith('ATOM'):
            try:
                curr_res = int(line[23:26])
                curr_chain = line[21]
            except ValueError:
                continue
            if prev_res!=curr_res:
                #print(curr_res)
                prev_res = curr_res
                resname = line[17:20]
                if curr_chain in seq:
                    seq[curr_chain]+=letters[resname]
                else:
                    seq[curr_chain]=letters[resname]
    
    return seq
