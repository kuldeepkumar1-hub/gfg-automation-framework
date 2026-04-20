from utils.config_reader import load_config

def test_config():
    config = load_config()
    print(config)

    assert config["browser"] == "chrome"
    assert "base_url" in config