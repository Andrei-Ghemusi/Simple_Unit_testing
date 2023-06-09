from application.methods_to_be_tested import UnitTestClass


class TestReverse(UnitTestClass):
    def setup_method(self):
        print('Instructions executed at the beginning')
        self.change = UnitTestClass()

    def teardown_method(self):
        print('Instructions executed at the end')

    def test_square_digits_method(self):
        assert self.change.square_digits(9119) == 811181
