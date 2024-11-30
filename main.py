from runner import Runner
from configs import log

if __name__ == '__main__':
    log.info(__name__, 'Iniciando RPA')
    try:
        log.info(__name__, 'Iniciando processamento...')
        Runner().intranet_values()
        log.info(__name__, 'Processamento concluído.')
    except Exception as error:
        log.critical(__name__, f'Ocorreu um erro: {error.__str__()}')
        raise Exception(f'Ocorreu um erro: {error.__str__()}')