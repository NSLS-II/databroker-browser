# We assume this is being run in a namespace (e.g. an IPython profile startup
# script) where an instance of databroker.Broker named `db` is already defined.


from databroker_browser.qt import BrowserWindow, CrossSection, StackViewer
from bluesky.callbacks.best_effort import BestEffortCallback


search_result = lambda h: "{start[plan_name]} ['{start[uid]:.6}']".format(**h)
text_summary = lambda h: "This is a {start[plan_name]}.".format(**h)


def fig_dispatch(header, factory):
    bec = BestEffortCallback(fig_factory=factory, table_enabled=False)
    db.process(header, bec)


def browse():
    return BrowserWindow(db, fig_dispatch, text_summary, search_result)
