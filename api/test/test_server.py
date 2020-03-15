from api.server import get_run_kwargs


def test_get_run_kwargs():
    a = get_run_kwargs([])
    assert a == {'host': '127.0.0.1', 'log_level': 'debug', 'port': 8000}

    a = get_run_kwargs(['--host', '0.0.0.0',
                        '--port', '1234',
                        '--log-level', 'warning',
                        '--log-file', 'log.txt'])
    assert a == {'host': '0.0.0.0', 'log_level': 'warning', 'port': 1234}
