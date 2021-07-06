import time
import os
import logging
import psutil


class FirstTestCase(object):
    tc_id = 1
    name = 'FirstTestCase'

    def __prep(self):
        epoch = int(time.time())
        if epoch % 2 == 0:
            logging.info('Подготовка завершена. Началось выполнение. ' + str(epoch))
            return True
        else:
            logging.warning('Выполнение не началось. ' + str(epoch))
            return False

    def __run(self):
        # Не Desktop в целях приватности.
        home_dir = "C:\\Users\\{user}\\Desktop\\Home".format(user=os.getlogin())
        files = os.listdir(home_dir)
        if len(files) == 0:
            logging.info('Файлы не обнаружены.')
        else:
            print(files)
        logging.info('Выполнение завершилось.')

    def __clean_up(self):
        logging.info('Выход из тест-кейса.')

    @classmethod
    def execute(cls):
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s', 
            filename='main.log', encoding='utf-8', level=logging.DEBUG)

        logging.debug('tc_id = ' + str(cls.tc_id) + ', name = ' + cls.name)
        ready = cls.__prep(cls)
        
        if ready:
            cls.__run(cls)
            cls.__clean_up(cls)



class SecondTestCase(object):
    tc_id = 2
    name = 'SecondTestCase'

    def __prep(self):
        ram = psutil.virtual_memory()
        if ram.total >= ((2 ** 10) ** 3):
            logging.info('Подготовка завершена. Началось выполнение.')
            return True 
        else:
            logging.warning('Выполнение не началось.')
            return False

    def __run(self):
        with open('test_file', 'wb') as f:
            f.write(os.urandom((2 ** 10) ** 2))

        logging.info('Выполнение завершилось.')

    def __clean_up(self):
        os.remove('test_file')
        logging.info('Выход из тест-кейса.')

    @classmethod
    def execute(cls):
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s', 
            filename='main.log', encoding='utf-8', level=logging.DEBUG)

        logging.debug('tc_id = ' + str(cls.tc_id) + ', name = ' + cls.name)
        ready = cls.__prep(cls)
        
        if ready:
            cls.__run(cls)
            cls.__clean_up(cls)


FirstTestCase.execute()
SecondTestCase.execute()