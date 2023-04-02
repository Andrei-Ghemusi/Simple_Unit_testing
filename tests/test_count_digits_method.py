from application.methods_to_be_tested import UnitTestClass


class TestReverse(UnitTestClass):
    def setup_method(self):
        print('Instructions executed at the beginning')
        self.change = UnitTestClass()

    def teardown_method(self):
        print('Instructions executed at the end')

    def test_count_digits_method(self):
        lista = [1,2,2,2,5,6,7,0,6,7]
        assert self.change.count_digits(lista) == {0: 1, 1: 1, 2: 3, 3: 0, 4: 0, 5: 1, 6: 2, 7: 2, 8: 0, 9: 0}