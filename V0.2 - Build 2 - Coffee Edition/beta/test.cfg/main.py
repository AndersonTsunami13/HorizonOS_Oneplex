from MDL_config import Config


def enable_developer_console():
    print("[DEV] Developer Console ativada!")


def disable_status_bar():
    print("[SYSTEM] Status Bar desativada!")


config = Config("system.cfg")

config.register_action(
    "EnableDeveloperConsole",
    enable_developer_console
)

config.register_action(
    "DisableStatusBar",
    disable_status_bar
)


print("Configurações:")
print(config.all())

if config.get("Debug_Mode"):
    print("Modo debug ativo!")


config.run_configured_action()
