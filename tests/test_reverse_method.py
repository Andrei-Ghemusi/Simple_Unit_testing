from application.methods_to_be_tested import UnitTestClass


class TestReverse(UnitTestClass):
    def setup_method(self):
        print('Instructions executed at the beginning')
        self.change = UnitTestClass()

    def teardown_method(self):
        print('Instructions executed at the end')

    def test_reverse(self):
        assert self.change.reverse_this(123456) == 654321
        assert self.change.reverse_this('Abraham') == 'maharbA'