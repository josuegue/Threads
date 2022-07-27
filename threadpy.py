import threading
import time 
import logging

class ExampleThreads:

    def fucntionThreads(self,arg: str):
        """_summary_: Imprime iteraciones de una lista y el nombre del hilo, con su identificador.

        Args:
            arg (str): una palabra para poder iterar sobre ella, o puede ser una lista.
        """
        try:
            for i in arg:
                time.sleep(2)
                print(f'Letra: {i} --- Hilo: {threading.current_thread().name}',
                f'--- identificador: {threading.current_thread().ident}', end='\n')
        except threading.excepthook() as ex:
            print(f'Thread failed: {ex}')


    def runThreads(self):

        hilo1 = threading.Thread(target=self.fucntionThreads, args=('hola',))
        hilo2 = threading.Thread(target=self.fucntionThreads, args=('adios..',))
        hilo1.start()
        hilo2.start()

def run():
    th = ExampleThreads()
    th.runThreads()

if __name__=='__main__':
    run()