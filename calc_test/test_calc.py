import pytest
#from calc_test.calc import Calc
import calc

class TestCalc():


    @pytest.fixture()
    def test_new_calc(self):
        self.calc_ob=calc.Calc()

    @pytest.mark.parametrize("a,b,sum", [(3,5,8),
                                         (12,-12,0),
                                         (999,0,999),
                                         (0.2,0.2,0.4),
                                         (-0.999,-0.001,-1),
                                         ('a','b','ab'),
                                         ("ccc","ddd","cccddd")])
    def test_sum(self,test_new_calc,a,b,sum):

        assert self.calc_ob.add(a,b)==sum

    @pytest.mark.parametrize("a,b,div", [(10, 5, 2),
                                         (10000,-20,-500),
                                         (-0.1,2,-0.05),
                                         (100,30,3.33333),
                                         (0,0,""),
                                         ('a', '2', ""),
                                         ('@','#','')])
    def test_div(self,test_new_calc, a, b, div):
        calc_result = self.calc_ob.div(a,b)

        if isinstance(calc_result,str):
            print(calc_result)
            assert "Exception" in calc_result;
        else:
            assert '%.5f'%calc_result == '%.5f'%div

if __name__=='__main__':
    pytest.main(['-v','test_calc.py::TestCalc::test_div'])