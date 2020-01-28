# kamaka.py
# helper module to store common functions

from qiskit import *

import numpy as np

def real_matrix(mx: list) -> np.array:
    return np.array([[x.real for x in row] for row in mx])

def norm_matrix(mx: list, norm: float) -> np.array:
    return np.array([[(x / norm) for x in row] for row in mx])

def cleanup_matrix(mx: list, norm: float) -> np.array:
    cleaned = norm_matrix(real_matrix(mx), norm)
    cleaned = [[int(x) for x in row] for row in cleaned]
    cleaned = str(cleaned).replace('\n', '').replace('   ', '  ').replace(']', ']\n')
    return np.array(cleaned)

# def cleanup_matrix(mx: list, norm: float) -> np.array:
#     cleaned = np.array([[int(x.real / norm) for x in row] for row in mx])
#     cleaned = str(cleaned).replace('\n', '').replace('   ', '  ').replace(']', ']\n')
#     return np.array(cleaned)
#
def trim_matrix(mx: list, dim: int) -> np.array:
    """ Takes an nxn matrix and returns a reduced matrix of dimension dim x dim
    corresponding to the upper-left square of the original matrix"""
    trimmed = [[x for idx, x in enumerate(row) if idx < dim] for index, row in enumerate(mx) if index < dim]
    return np.array(trimmed)

def refresh(size: int, reg_name='q', circ_name='qc') -> (QuantumRegister, QuantumCircuit):
    reg = QuantumRegister(size, name=reg_name)
    circ = QuantumCircuit(reg, name=circ_name)
    
    return reg, circ

def saved_bs():
    qr = QuantumRegister(2, 'qr')
    c = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(qr, c)
    
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.measure(qr, c)
    
    return qc.to_instruction()

def bv_oracle(state: int):
    from math import ceil, log2

    qr, qc = refresh(ceil(log2(state)) + 1)
    for i in range(len(qr) - 1):
        if state & (1 << i):
            qc.cx(qr[i], qr[len(qr) - 1])
    return qc.to_instruction()

def bv_oracleA():
    state = 11
    qr, qc = refresh(5)
    for i in range(4):
        if state & (1 << i):
            qc.cx(qr[i], qr[4])
    return qc.to_instruction()

def bv_oracleB():
    state = 14
    qr, qc = refresh(5)
    for i in range(4):
        if state & (1 << i):
            qc.cx(qr[i], qr[4])
    return qc.to_instruction()

def bv_oracleC():
    state = 9
    qr, qc = refresh(5)
    for i in range(4):
        if state & (1 << i):
            qc.cx(qr[i], qr[4])
    return qc.to_instruction()
