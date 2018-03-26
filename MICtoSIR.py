#!/usr/bin/env python
'''This is used to transfer from MIC value to SIR.
Author: Sam Zhu
'''

#Dictionary of MIC (According to M100-S28 Enterobacteriaceae)
#Not include MA(Cefamandole), CFP(Cefoperazone), SPX(Sparfloxacin), PFX/PEF(Pefloxacin), SPZ(Cefoperazone/Sulbactam), CFC/CTC(Cefotaxime/Clavulanic acid)

SIR16_32_64 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'S', '32':'I', '64':'R', '128':'R', '256':'R', '512':'R'} 
SIR4_8_16 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'I', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SIR16_3264_128 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'S', '32':'I', '64':'I', '128':'R', '256':'R', '512':'R'} 
SR8_16 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SR1_2 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'R', '4':'R', '8':'R', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SIR1_2_4 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'I', '4':'R', '8':'R', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SIR8_16_32 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'I', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SIR025_05 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'R', '1':'R', '2':'R', '4':'R', '8':'R', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SIR2_4_8 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'I', '4':'R', '8':'R', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SR16_32 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'S', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SR2_4 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'R', '8':'R', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SIR8_16_32 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'I', '32':'S', '64':'R', '128':'R', '256':'R', '512':'R'} 
SIR16_3264_128 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'S', '32':'I', '64':'I', '128':'R', '256':'R', '512':'R'} 
SIR05_1_2 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'I', '2':'R', '4':'R', '8':'R', '16':'R', '32':'R', '64':'R', '128':'R', '256':'R', '512':'R'}
SIR32_64_128 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'S', '32':'S', '64':'I', '128':'R', '256':'R', '512':'R'} 
SIR64_128_256 = {'0.015':'S', '0.03':'S', '0.06':'S', '0.06':'S', '0.12':'S', '0.25':'S', '0.5':'S', '1':'S', '2':'S', '4':'S', '8':'S', '16':'S', '32':'S', '64':'S', '128':'I', '256':'R', '512':'R'} 

	# AN for Amikacin 
AN = SIR16_32_64
	# G for Gentamicin 
G = SIR4_8_16
	# PIP for Piperacillin 
PIP = SIR16_3264_128
	# NN for Tobramycin 
NN = SIR4_8_16
	# TM for Trimethoprim 
TM = SR8_16
	# TGC for Tigecycline (According to EUCAST v8.0, only suitable for E.coli) (S,R:1,2)
TGC = SR1_2
	# IMP for Imipenem
IMP = SIR1_2_4
	# CTX for Cefotaxime
CTX = SIR1_2_4
	# CAZ for Ceftazidime
CAZ = SIR4_8_16
	# CFT for Cefotaxime
CFT = SIR1_2_4
	# CXM for Cefuroxime (parenteral)
CXM = SIR8_16_32
	# A for Ampicillin
A = SR8_16
	# MFX for Moxifloxacin (According to EUCAST v8.0) 
MFX = SIR025_05
	# LVX for Levofloxacin
LVX = SIR2_4_8
    # CFX,CIP for Ciprofloxacin
CFX = SIR1_2_4
CIP = SIR1_2_4
    # NOR for Norfloxacin
NOR = SIR4_8_16
    # FLX for Fleroxacin
FLX = SIR2_4_8
    # NA for Nalidixic Acid
NA = SR16_32
    # MER for Meropenem
MER = SIR1_2_4
    # CHL for Chloramphenicol 
CHL = SIR8_16_32
    # CPE for Cefepime (In CLSI is S,SDD,R:2,4-8,18, we include SDD to R)
CPE = SR2_4
    # CBT for Ceftibuten
CBT = SIR8_16_32
    # CPD for Cefpodoxime
CPD = SIR2_4_8
    # U for Ampicillin-Sulbactam (Using Ampicillin, actually is 8/4, 16/8, 32/16) 
U = SIR8_16_32
    # PTZ for Piperacillin-Tazobactam (Using Piperacillin, actually is 16/2, 32/2-64/2, 128/2)
PTZ = SIR16_3264_128
    # ETP for Ertapenem
ETP = SIR05_1_2
    # CL for Colistin (According to EUCAST v8.0) 
CL = SR2_4
    # NIT for Nitrofurantoin
NIT = SIR32_64_128
    # FOS for Fosfomycin
FOS = SIR64_128_256
    
    
    
import argparse


def parse_args():
    parser = argparse.ArgumentParser('Transfer from MIC value to SIR')
 
    parser.add_argument('-i', dest='input', type=str, required=True, help='name of input MIC txt file')
    
    return parser.parse_args()

args = parse_args()

filename = args.input
fr=open(filename, 'r')




fw=open('SIR.txt','w')
head = fr.readline()
head = head.rstrip()
head_list = head.split("\t")
fw.write(head)
fw.write('\n')
for line in fr:
    line=line.rstrip()
    list_line=line.split("\t")
    pos = 1
    while pos < len(list_line):
        mic_dict=head_list[pos]
        list_line[pos]=eval(mic_dict).get(list_line[pos])
        pos+=1
    new_line=("\t").join(list_line)
    fw.write(new_line)
    fw.write('\n')

fr.close()
fw.close()

print('Task finished, results in out.txt')
