class GRS80:
    a_axis = 6378137
    e2 = 0.00669438002290
    f = 1 / 298.25722210
    b_axis = a_axis - a_axis * f
    e2p = round((a_axis ** 2 - b_axis ** 2) / b_axis ** 2, 13)