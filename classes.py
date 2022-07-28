from functools import cached_property


class DeletionProhibited(Exception):
    pass


class MyClass:
    counter = 1
    _prop = 0

    def __init__(self, instance_attr):
        self.prop = instance_attr
        self.__class__.counter += 1

    @property
    def prop(self):
        return self._prop

    @prop.setter
    def prop(self, x):
        if x > 0:
            self._prop = x
        else:
            raise AttributeError("prop attribute can not be less than 0")

    @prop.deleter
    def prop(self):
        raise DeletionProhibited

    @cached_property
    def cached_prop(self):
        return 10 * 20

    @staticmethod
    def my_static():
        return "This is static method"

    @classmethod
    def my_classmethod(cls, instance_attr, multiplier):
        return cls(instance_attr=instance_attr * multiplier)


class MyClass2(MyClass):

    def my_static(self):
        return "This is NOT a static method"


if __name__ == "__main__":
    instance1 = MyClass(100)
    print(f"{instance1.counter=}, {instance1.prop}")

    instance2 = MyClass(200)
    print(f"{instance2.counter=}, {instance2.prop}")

    instance3 = MyClass.my_classmethod(instance_attr=300, multiplier=20)
    print(f"{instance3.counter=}, {instance3.prop}")

    print(f"{MyClass.my_static()=}")

    instance4 = MyClass(-20)

    print(f"{MyClass2.my_static()=}")

    print(f"{MyClass2.mro()=}")