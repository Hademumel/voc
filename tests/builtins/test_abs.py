from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AbsTests(TranspileTestCase):
    def test_abs_not_implemented(self):
        self.assertCodeExecution("""
            class NotAbsLike:
                pass
            x = NotAbsLike()
            try:
                print(abs(x))
            except TypeError as err:
                print(err)
            """)

    def test_incorrect_abs_call_int(self):
        self.assertCodeExecution("""
            x = 1
            print(x.abs())
            """, exits_early=True)

    def test_incorrect_abs_call_float(self):
        self.assertCodeExecution("""
            x = 1.2
            print(x.abs())
            """, exits_early=True)

    def test_incorrect_abs_call_complex(self):
        self.assertCodeExecution("""
            x = 5j
            print(x.abs())
            """, exits_early=True)

    def test_incorrect_abs_call_bool(self):
        self.assertCodeExecution("""
            x = True
            print(x.abs())
            """, exits_early=True)

    def test_incorrect_abs_call_list(self):
        self.assertCodeExecution("""
            x = []
            print(x.abs())
            """, exits_early=True)


class BuiltinAbsFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["abs"]

    not_implemented = []
