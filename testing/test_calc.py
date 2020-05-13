import pytest
import sys
sys.path.append("..")
from python.calc import Calc
import yaml

def steps():
    with open("datas/steps.yml") as f:
        return yaml.safe_load(f)

class TestCalc():

    @pytest.fixture()
    def test_new_calc(self):
        self.calc_ob=Calc()

    @pytest.mark.parametrize("a,b,add", yaml.safe_load(open("datas/add.yml")))
    def calc_add(self,test_new_calc,a,b,add):
        steps_=steps()
        for step in steps_:
            if 'add' == step:
                result=self.calc_ob.add(a,b)
                assert result==add
       # assert self.calc_ob.add(a,b)==sum

    @pytest.mark.parametrize("a,b,sub", yaml.safe_load(open("datas/sub.yml")))
    def calc_sub(self, test_new_calc, a, b, sub):
        steps_ = steps()
        for step in steps_:
            if 'sub' == step:
                result = self.calc_ob.sub(a, b)
                if isinstance(result, str):
                    print(result)
                    assert "Exception" in result;
                else:
                    assert '%.5f' % result == '%.5f' % sub

    # assert self.calc_ob.add(a,b)==sum
    @pytest.mark.parametrize("a,b,mul", yaml.safe_load(open("datas/mul.yml")))
    def calc_mul(self, test_new_calc, a, b, mul):
        calc_result = self.calc_ob.mul(a, b)

        if isinstance(calc_result, str):
            print(calc_result)
            assert "Exception" in calc_result;
        else:
            assert '%.5f' % calc_result == '%.5f' % mul

    # @pytest.mark.skip("div")
    @pytest.mark.parametrize("a,b,div", yaml.safe_load(open("datas/div.yml")))
    def calc_div(self,test_new_calc, a, b, div):

        steps_ = steps()
        for step in steps_:
            if 'div' == step:
                calc_result = self.calc_ob.div(a, b)
                if isinstance(calc_result,str):
                    print(calc_result)
                    assert "Exception" in calc_result;
                else:
                    assert '%.5f'%calc_result == '%.5f'%div




if __name__=='__main__':
    #pytest.main(['-s','-m','adddiv','-q','--alluredir=./allure_result'])
    pytest.main(['-v','-m','add'])