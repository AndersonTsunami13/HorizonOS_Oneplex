# ThreadingManager.py

import threading

threads = {}

def thread_create(name, target):
    if name in threads:
        raise Exception("Essa thread ja existe.")

    stop_event = threading.Event()

    def runner():
        target(stop_event)

    thread = threading.Thread(target=runner, daemon=True)

    thread.start()

    threads[name] = {"thread": thread, "event": stop_event}

def thread_stop(name):
    if name not in threads:
        return

    threads[name]["event"].set()

def thread_remove(name):
    if name in threads:
        del threads[name]

def threads_list():
    print("\n ========== THREADS ========== ")

    for name, data in threads.items():
        status = "RUNNING" if data["thread"].is_alive() else "STOPPED"

    print(f"[{status}] {name}")

