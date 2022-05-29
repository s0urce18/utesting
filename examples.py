from utesting import Test, TestCase
# import asyncio # for async testing way

t = Test()

cases1 = [TestCase({"a": 100000}, 100000), TestCase({"a": 200000}, 200000), TestCase({"a": 200000}, 300000)]

@t.mark_test_unit(cases=cases1)
def func1(a):
    n = 0
    for i in range(0, a):
        n += 1
    return n

cases2 = [TestCase({"a": [1, 5, 2, 5]}, [1, 2, 5, 5]), TestCase({"a": [1, 7, 3, 7, 9, 0]}, [0, 1, 3, 7, 7, 9])]

@t.mark_test_unit(cases=cases2)
def func2(a):
    k = 0
    while k < len(a) - 1:
        k = 0
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                a[j] = a[j] + a[j+1]
                a[j+1] = a[j] - a[j+1]
                a[j] = a[j] - a[j+1]
            else:
                k += 1
    return a

@t.mark_test_unit(cases=[TestCase({"a": 1}, 1)], only_errors=True)
def func3(a):
    a = a / 0

@t.mark_test_unit(cases=[TestCase({"a": 100000}, 100000)], only_time=True)
def func4(a):
    result = 1
    for m in range(1, a + 1):
        result *= m
    return result

class A:

    c = 2

    def func5(self, a):
        return a / self.c

a = A()

t.add_test_unit(a.func5, [TestCase({"a": 1}, 0.5)])

cases5 = [TestCase({"a": 5}, 5), TestCase({"a": 15}, 15)]

@t.mark_test_unit(cases=cases5, asynchronous=True)
async def func6(a):
    if a <= 1: return a
    else: return await func6(a - 1) + await func6(a - 2)


t.test_all()
# asyncio.run(t.test_all_async()) # async testing way
"""
****************************************************************************************************
UNIT: func1
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': 100000}
    Correct answer: 100000
    Returned answer: 100000
    Result: PASSED
    Time: 11.001110076904297 ms
----------------------------------------------------------------------------------------------------
CASE 1:
    Agruments: {'a': 200000}
    Correct answer: 200000
    Returned answer: 200000
    Result: PASSED
    Time: 24.006128311157227 ms
----------------------------------------------------------------------------------------------------
CASE 2:
    Agruments: {'a': 200000}
    Correct answer: 300000
    Returned answer: 200000
    Result: FAILED
    Time: 23.003339767456055 ms
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func2
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': [1, 2, 5, 5]}
    Correct answer: [1, 2, 5, 5]
    Returned answer: [1, 2, 5, 5]
    Result: PASSED
    Time: 0.0 ms
----------------------------------------------------------------------------------------------------
CASE 1:
    Agruments: {'a': [0, 1, 3, 7, 7, 9]}
    Correct answer: [0, 1, 3, 7, 7, 9]
    Returned answer: [0, 1, 3, 7, 7, 9]
    Result: PASSED
    Time: 0.0 ms
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func3
----------------------------------------------------------------------------------------------------
CASE 0: ERROR ( division by zero )
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func4
----------------------------------------------------------------------------------------------------
CASE 0: TIME ( 2.3085319995880127 s )
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func5
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': 1}
    Correct answer: 0.5
    Returned answer: 0.5
    Result: PASSED
    Time: 0.0 ms
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func6
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': 5}
    Correct answer: 5
    Returned answer: 5
    Result: PASSED
    Time: 2.0003318786621094 ms
----------------------------------------------------------------------------------------------------
CASE 1:
    Agruments: {'a': 15}
    Correct answer: 15
    Returned answer: 610
    Result: FAILED
    Time: 9.19651985168457 ms
----------------------------------------------------------------------------------------------------
****************************************************************************************************
NOT ALL TESTS PASSED :(
****************************************************************************************************
"""