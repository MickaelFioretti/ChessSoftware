from abc import ABC, abstractmethod
import os


class BaseView(ABC):
    @abstractmethod
    def display(self) -> dict:
        pass

    def clear_shell(self):
        """Clear the shell"""
        os.system("cls" if os.name == "nt" else "clear")
