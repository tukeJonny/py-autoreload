#-*- coding: utf-8 -*-

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

def isdir(event):
    """
    ハンドリングしているイベントがディレクトリへの操作によるものか否か
    """
    if event.is_directory:
        return True
    else:
        return False

class Watcher(FileSystemEventHandler):
    """
    指定されたディレクトリ以下を監視する
    """

    def on_created(self, event):
        """
        何かが作成された
        """
        if isdir(event): return

    def on_modified(self, event):
        """
        何かが変更された
        作成時もon_createdの次に呼ばれてしまう
        """
        if isdir(event): return

    def ondeleted(self, event):
        """
        何かが削除された
        """
        if isdir(event): return

def start_watcher(path, recursive=True):
    """
    watcherのエントリーポイント
    """
    while True:
        watcher = Watcher()

        observer = Observer()
        observer.schedule(watcher, path, recursive=recursive)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        obsewrver.join()
