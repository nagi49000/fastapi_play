from api.server import get_run_kwargs


def test_get_run_kwargs():
    a = get_run_kwargs([])
    assert a == {'host': '127.0.0.1',
                 'port': 8000,
                 'log_config': {'disable_existing_loggers': False,
                                'formatters': {'access': {'()': 'uvicorn.logging.AccessFormatter',
                                                          'fmt': '%(asctime)s %(levelname) '
                                                          '%(client_addr)s - '
                                                          '"%(request_line)s" '
                                                          '%(status_code)s'},
                                               'default': {'()': 'uvicorn.logging.DefaultFormatter',
                                                           'fmt': '%(asctime)s %(levelname)-8s '
                                                           '%(message)s'}
                                               },
                                'handlers': {'access': {'class': 'logging.StreamHandler',
                                                        'formatter': 'access',
                                                        'stream': 'ext://sys.stdout'},
                                             'default': {'class': 'logging.StreamHandler',
                                                         'formatter': 'default',
                                                         'stream': 'ext://sys.stdout'}
                                             },
                                'loggers': {'': {'handlers': ['default'], 'level': 10},
                                            'uvicorn.access': {'handlers': ['access'],
                                                               'level': 10,
                                                               'propagate': False},
                                            'uvicorn.error': {'level': 10}
                                            },
                                'version': 1}
                 }

    a = get_run_kwargs(['--host', '0.0.0.0',
                        '--port', '1234',
                        '--log-level', 'warning',
                        '--log-file', 'log.txt'])
    assert a == {'host': '0.0.0.0',
                 'port': 1234,
                 'log_config': {'disable_existing_loggers': False,
                                'formatters': {'access': {'()': 'uvicorn.logging.AccessFormatter',
                                                          'fmt': '%(asctime)s %(levelname) %(client_addr)s - "%(request_line)s" %(status_code)s'},
                                               'default': {'()': 'uvicorn.logging.DefaultFormatter',
                                                           'fmt': '%(asctime)s %(levelname)-8s %(message)s'}
                                               },
                                'handlers': {'access': {'class': 'logging.StreamHandler',
                                                        'formatter': 'access',
                                                        'stream': 'ext://sys.stdout'},
                                             'default': {'class': 'logging.StreamHandler',
                                                         'formatter': 'default',
                                                         'stream': 'ext://sys.stdout'}
                                             },
                                'loggers': {'': {'handlers': ['default'],
                                                 'level': 30},
                                            'uvicorn.access': {'handlers': ['access'],
                                                               'level': 30,
                                                               'propagate': False},
                                            'uvicorn.error': {'level': 30}
                                            },
                                'version': 1},
                 }
