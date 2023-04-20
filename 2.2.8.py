class TreeObj:

    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if isinstance(left, TreeObj) or left is None:
            self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if isinstance(right, TreeObj) or right is None:
            self.__right = right


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        cur_el = root
        while cur_el:
            next_el = cur_el.left if x[cur_el.indx] else cur_el.right
            if next_el is None:
                break
            cur_el = next_el
        return cur_el.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node is None:
            return obj
        if left:
            node.left = obj
        else:
            node.right = obj
        return obj

assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree, 'predict'), "в классе DecisionTree должны быть методы add_obj и predict"

assert type(TreeObj.left) == property and type(TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"