from helpers import assert_norm_equality

import dmsh


def test(show=False):
    geo = dmsh.Translation(dmsh.Rectangle(-1.0, +2.0, -1.0, +1.0), [1.0, 1.0])
    X, cells = dmsh.generate(geo, 0.1, show=show)

    ref_norms = [1.7525000000000000e03, 5.5677284113304673e01, 3.0000000000000000e00]
    assert_norm_equality(X.flatten(), ref_norms, 1.0e-7)


if __name__ == "__main__":
    test(show=False)
