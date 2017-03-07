# Graphical Data Broker Browsers

## What is this?

This is GUI for browsing runs that are stored in the databroker. It is intended
as read-only browser, not a full-fledged data analysis framework. There is
limited support for interactivity and data export.

Features:
* Fast, rich search (backed by MongoDB queries)
* Fully customizable textual summaries and figures that can be made specifically
  relevant to certain kinds of experiments or results.
* Interactive figures (backed by matplotlib)
* Export to CSV and Excel

Currently, there is only one browser, implemented using Qt. Browsers for the
web, Jupyter, and PDF are planned.

## Getting Started

You need a databroker with some data in it. A quick way to obtain one is to
download the [tutorial](https://github.com/NSLS-II/tutorial):

```
git clone https://github.com/NSLS-II/tutorial
ipython
%run tutorial/startup.py  # defines a db and subscribed it to a RunEngine RE
%run -i tutorial/generate_data.py  # executes some plans using RE, generating data in db
```

And now set up a ``BrowserWindow`` instance. See example.py in this repo to get
started.
