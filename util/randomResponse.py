import numpy as np
from setting import Settings

setts = Settings()


def computePRR(bf_bits):
    if setts.pro_f == 0.0:
        return bf_bits

    for i in range(len(bf_bits)):
        should_use_noise = np.random.rand() < setts.pro_f
        if should_use_noise:
            if np.random.rand() < 0.5:
                bf_bits[i] = 1
            else:
                bf_bits[i] = 0


def computeIRR(prr_bits):
    if setts.pro_q == 1 and setts.pro_p == 0:
        return prr_bits

    for i in range(len(prr_bits)):
        bool_bit = prr_bits[i]
        if bool_bit == 1:
            probability = setts.pro_q
        else:
            probability = setts.pro_p
        res_bit = np.random.rand() < probability
        if res_bit:
            prr_bits[i] = 1
        else:
            prr_bits[i] = 0
