import importlib
import os

class PluginSystem:
    def __init__(self, plugin_dir='plugins'):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith('.py'):
                plugin_name = filename[:-3]
                module = importlib.import_module(f"plugins.{plugin_name}")
                self.plugins[plugin_name] = module

    def execute_plugin(self, plugin_name, *args):
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].execute(*args)
        else:
            raise ValueError(f"Plugin {plugin_name} not found")

