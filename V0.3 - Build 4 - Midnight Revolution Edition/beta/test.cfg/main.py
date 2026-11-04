from MDL_config import Config

def test_agmt(x):
    print(f"Running test_agmt with argument: {x}")

config = Config("system.cfg")
config.run_action(test_agmt, 1155)
