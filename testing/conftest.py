import pytest, sys
"""
方法定义在conftest.py中，就可以默认去执行
此例子是按照测试用例的方法名给各测试用例自动添加mark
然后通过pytest -m add这样的方式来执行名字中有add(test_add)的用例
"""
def pytest_collection_modifyitems(session,config,items):
    # print(items)
    # print(type(items))
    # items.reverse()

    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
