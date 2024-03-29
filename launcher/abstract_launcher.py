from abc import ABC, abstractmethod
import os

class LauncherBase(ABC):
    
    @abstractmethod
    def input_data(self):
        """
        Recebe os dados de entrada.
        
        """
        pass

    @abstractmethod
    def check_data(self):
        """
        Verifica os Dados Presentes
        """
        pass
    
