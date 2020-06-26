class GRS80:
    a_axis = 6378137
    e2 = 0.00669438002290
    f = 1 / 298.25722210
    b_axis = a_axis - a_axis * f
    e2p = round((a_axis ** 2 - b_axis ** 2) / b_axis ** 2, 13)
    e4 = e2 ** 2
    e6 = e2 ** 3
    A0 = 1 - e2 / 4 - 3 * e4 / 64 - 5 * e6 / 256
    A2 = 3 / 8 * (e2 + e4 / 4 + 15 * e6 / 128)
    A4 = 15 / 256 * (e4 + 3 * e6 / 4)
    A6 = 35 * e6 / 3072


class WGS84:
    a_axis = 6378137
    e2 = 0.00669437999014
    f = 1 / 298.257223563
    b_axis = a_axis - a_axis * f
    e2p = round((a_axis ** 2 - b_axis ** 2) / b_axis ** 2, 13)

    e4 = e2 ** 2
    e6 = e2 ** 3
    A0 = 1 - e2 / 4 - 3 * e4 / 64 - 5 * e6 / 256
    A2 = 3 / 8 * (e2 + e4 / 4 + 15 * e6 / 128)
    A4 = 15 / 256 * (e4 + 3 * e6 / 4)
    A6 = 35 * e6 / 3072
