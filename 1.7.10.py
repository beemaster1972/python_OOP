class Application:

    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    applications = dict()

    def add_application(self, app):
        self.applications[app.name] = app

    def remove_application(self, app):
        del self.applications[app.name]

    def block_application(self, app):
        self.applications[app.name].blocked = True

    def total_apps(self):
        return len(self.applications)


store = AppStore()
app_youtube = Application("Youtube")
app_sber = Application("SberOnline")
store.add_application(app_youtube)
store.add_application(app_sber)
print(store.total_apps())
store.remove_application(app_youtube)
print(store.total_apps())