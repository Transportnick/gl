import unittest


def add_element(bus):
    bus=[2, 2, 0, 9, 2, 0, 0]
    bus.append(1)
    return bus


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_illia_kripaka_fi_94_2(self):
        self.assertEqual(2*[1, 3, 5], [1, 3, 5, 1, 3, 5])

    def test_illya_melnick_fi94(self):
        lista=[2, 2, 0, 9, 2, 0, 0]
        self.assertEqual(add_element(lista),[2, 2, 0, 9, 2, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
