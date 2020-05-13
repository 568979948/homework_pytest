import pytest
import yaml
with open("datas/test.yml") as f:
    print(yaml.safe_load(f))
