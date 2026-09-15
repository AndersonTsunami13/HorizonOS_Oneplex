"""
MDL_config.py
Sistema simples de configuração e ações para o HorizonOS.

Formato suportado no .cfg:
    Debug_Mode=True
    DevelopmentMode=1
    StatusBar=On
    FPS=60
    Name=HorizonOS

Também aceita comentários iniciados por # ou ;.

API principal:
    config = Config("system.cfg")
    config.register_action("EnableDeveloperConsole", func)
    config.run_action("EnableDeveloperConsole")
    config.get("Debug_Mode")
    config.set("Debug_Mode", False)
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any


class ConfigError(Exception):
    """Erro relacionado ao arquivo ou sistema de configuração."""


class Config:
    TRUE_VALUES = {"true", "on", "yes", "enabled"}
    FALSE_VALUES = {"false", "off", "no", "disabled"}

    def __init__(
        self,
        path: str | Path | None = None,
        defaults: Mapping[str, Any] | None = None,
        auto_load: bool = True,
    ) -> None:
        self.path = Path(path) if path is not None else None
        self.values: dict[str, Any] = dict(defaults or {})
        self.actions: dict[str, Callable[..., Any]] = {}

        if auto_load and self.path is not None:
            self.load_file()

    # ---------------------------------------------------------
    # Leitura / escrita
    # ---------------------------------------------------------

    def load_file(self) -> dict[str, Any]:
        """Lê o arquivo .cfg e retorna as configurações carregadas."""
        if self.path is None:
            raise ConfigError("Nenhum arquivo de configuração foi definido.")

        if not self.path.exists():
            raise ConfigError(f"Arquivo de configuração não encontrado: {self.path}")

        try:
            text = self.path.read_text(encoding="utf-8")
        except OSError as exc:
            raise ConfigError(f"Não foi possível ler {self.path}: {exc}") from exc

        self.values.update(self.parse(text))
        return self.values

    def save(self) -> None:
        """Salva as configurações atuais no arquivo .cfg."""
        if self.path is None:
            raise ConfigError("Nenhum arquivo de configuração foi definido.")

        lines: list[str] = []

        for key, value in self.values.items():
            lines.append(f"{key}={self._serialize(value)}")

        try:
            self.path.write_text(
                "\n".join(lines) + ("\n" if lines else ""),
                encoding="utf-8",
            )
        except OSError as exc:
            raise ConfigError(f"Não foi possível salvar {self.path}: {exc}") from exc

    @classmethod
    def parse(cls, text: str) -> dict[str, Any]:
        """Converte texto .cfg em um dicionário Python."""
        result: dict[str, Any] = {}

        for line_number, raw_line in enumerate(text.splitlines(), start=1):
            line = raw_line.strip()

            if not line or line.startswith("#") or line.startswith(";"):
                continue

            if "=" not in line:
                raise ConfigError(
                    f"Linha {line_number} inválida: esperava 'Chave=Valor'."
                )

            key, raw_value = line.split("=", 1)
            key = key.strip()
            raw_value = raw_value.strip()

            if not key:
                raise ConfigError(f"Linha {line_number}: chave vazia.")

            result[key] = cls._convert_value(raw_value)

        return result

    @classmethod
    def _convert_value(cls, value: str) -> Any:
        """Converte strings do .cfg para tipos Python."""
        lower = value.lower()

        if lower in cls.TRUE_VALUES:
            return True

        if lower in cls.FALSE_VALUES:
            return False

        # Inteiros
        try:
            return int(value)
        except ValueError:
            pass

        # Decimais
        try:
            return float(value)
        except ValueError:
            pass

        # Texto
        return value

    @staticmethod
    def _serialize(value: Any) -> str:
        """Converte valores Python para o formato do .cfg."""
        if isinstance(value, bool):
            return "True" if value else "False"

        return str(value)

    # ---------------------------------------------------------
    # Acesso às configurações
    # ---------------------------------------------------------

    def get(self, key: str, default: Any = None) -> Any:
        """Obtém uma configuração."""
        return self.values.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Altera ou cria uma configuração."""
        self.values[key] = value

    def has(self, key: str) -> bool:
        """Verifica se uma configuração existe."""
        return key in self.values

    def remove(self, key: str) -> Any:
        """Remove uma configuração e retorna o valor antigo."""
        return self.values.pop(key, None)

    def all(self) -> dict[str, Any]:
        """Retorna uma cópia das configurações."""
        return self.values.copy()

    # ---------------------------------------------------------
    # Sistema de ações
    # ---------------------------------------------------------

    def register_action(
        self,
        name: str,
        function: Callable[..., Any],
    ) -> None:
        """Registra uma função que pode ser chamada pelo nome."""
        if not callable(function):
            raise TypeError(f"A ação '{name}' precisa ser uma função chamável.")

        self.actions[name] = function

    def unregister_action(self, name: str) -> None:
        """Remove uma ação registrada."""
        self.actions.pop(name, None)

    def run_action(self, name: str, *args: Any, **kwargs: Any) -> Any:
        """Executa uma ação registrada."""
        if name not in self.actions:
            raise ConfigError(f"Ação não registrada: {name}")

        return self.actions[name](*args, **kwargs)

    def run_configured_action(
        self,
        key: str = "Startup_Action",
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Lê o nome de uma ação de uma configuração e a executa.

        Exemplo:
            Startup_Action=EnableDeveloperConsole
        """
        action_name = self.get(key)

        if not action_name:
            return None

        if not isinstance(action_name, str):
            raise ConfigError(
                f"A configuração '{key}' precisa conter o nome de uma ação."
            )

        return self.run_action(action_name, *args, **kwargs)
