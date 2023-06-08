from unittest import main, TestCase

from MagicMethods.get_item import *


class SparseTableTest(TestCase):

    def test_rows_cols(self):
        st = SparseTable()
        st.add_data(2, 5, Cell(25))
        st.add_data(1, 1, Cell(11))

        self.assertEqual((st.rows, st.cols), (3, 6), "неверные значения атрибутов rows и cols")

    def test_value_error(self):
        st = SparseTable()
        st.add_data(2, 5, Cell(25))
        st.add_data(1, 1, Cell(11))
        with self.assertRaises(ValueError):
            v = st[3, 2]

    def test_setting(self):
        st = SparseTable()
        st.add_data(2, 5, Cell(25))
        st.add_data(1, 1, Cell(11))
        st[3, 2] = 100
        self.assertEqual(100, st[3, 2], "неверно отработал оператор присваивания нового значения в ячейку таблицы")


if __name__ == '__main__':
    main()
