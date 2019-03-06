import copy
import sys
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Fragments
 
def replace_atom(mol):
    res = []
    aro_idxs = [atom.GetIdx() for atom in mol.GetAromaticAtoms() if atom.GetDegree() < 3]
    for atm_num in [6, 7, 8, 16]:
        for idx in aro_idxs:
            cp_mol = copy.deepcopy(mol)
            cp_mol.GetAtomWithIdx(idx).SetAtomicNum(atm_num)
            p = Chem.MolFromSmarts("nnn")
            if cp_mol.HasSubstructMatch(p) != True:
                try:
                    smi = Chem.MolToSmiles(cp_mol)
                    smi.replace("[sH]", "s")
                    cp_mol = Chem.MolFromSmiles(smi)
                    Chem.SanitizeMol(cp_mol)
                    res.append(cp_mol)
                except:
                    pass
    return res
 
def recursive_replace(mols, check=set([]), thres=0.4):
    before_n = len(check)
    print(before_n)
    for mol in mols:
        replaced_mols = replace_atom(mol)
        for mol_conv in replaced_mols:
            aro_n = Fragments.fr_Ar_N(mol)
            aro_a = len(mol.GetAromaticAtoms())
            ratio = float(aro_n) / float(aro_a)
            if ratio < thres:
                smi = Chem.MolToSmiles(mol_conv)
                check.add(smi)
    after_n = len(check)
    print(before_n, after_n)
    if before_n < after_n:
        mols = [Chem.MolFromSmiles(mol) for mol in check]
        recursive_replace(mols, check=check)
    return [Chem.MolFromSmiles(smi) for smi in check]
