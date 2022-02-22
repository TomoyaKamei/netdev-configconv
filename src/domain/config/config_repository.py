from abc import ABC, abstractmethod

from config import Config

import re
import os


class ConfigRepository(ABC):
    def __init__(self, config_sample_file: str, config: Config, output_config_file: str):
        self.config_sample_file: str    = config_sample_file
        self.config: Config             = config
        self.output_config_file: str    = output_config_file

    @property
    def config_sample_file(self) -> str:
        return self._config_sample_file

    @config_sample_file.setter
    def config_sample_file(self, value: str) -> None:
        if not os.path.exists(value):
            raise ValueError(f"The 'config_sample_file' property(value: {value}) of the ConfigRepository doesn't exist in your directories")
        else:
            self._config_sample_file = value

    @property
    def config(self) -> Config:
        return self._config

    @config.setter
    def config(self, value: Config) -> None:
        self._config = value

    @property
    def output_config_file(self) -> str:
        return self._output_config_file

    @output_config_file.setter
    def output_config_file(self, value: str) -> None:
        if not os.path.exists(value):
            raise ValueError(
                f"The 'output_config_file' property(value: {value}) of the ConfigRepository doesn't exist in your directories")
        else:
            self._output_config_file = value


    @abstractmethod
    def write(self) -> None:
        raise NotImplementedError("The 'write_config' method of the ConfigRepository must be implemented.")

    @staticmethod
    def inspect_marker(line: str) -> bool:
        return True if re.search(r"%{2}\w+%{2}", line) else False