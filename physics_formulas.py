# coding=utf-8

"""
This is a collection of all my physics formulas
"""


def nm_to_ev(lambda_):
    """
    Convert the wavelength in nm to eV

    Parameters
    ----------
    lambda_

    Returns
    -------
    voltage in eV
    """
    h = 6.2 * 10 ** -34  # (?)
    c = 299792458
    f = c / lambda_
    e = h * f * 100000000  # because of nm instead of m
    e2 = 1.0 * e / (10 ** -19)
    print(e2, "eV")
    return e2
