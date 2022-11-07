import tkinter as tk
import tkinter.dnd


# reStructuredText Docstring example.
def dnd_accept(self, source, event):
    """
    Decide what object will accept the drop.

    The returned object will become the new target for the drop operation.

    :param source: The object being dragged.
    :param event: The tk event that resulted in this call.
                  Usually a motion event.
    :return: The object that will accept a drop - this widget.
    """
    print("dnd_accept. Called on {}. source is {}, event type is {}".format(self, source, event.type))
    return self


# Google Docstring example.
def on_dnd_start(event):
    """Starts a drag and drop (dnd) operation.

    This is usually invoked by a mouse event binding on a
    widget that can be dragged.

    For example, `tile.bind('<ButtonPress>', on_dnd_start)`

    Args:
        event: The tk event that resulted in this call.
    Returns:
        The object to be dragged.  Here, it's the widget
        that was clicked to call this function.
    """
    tk.dnd.dnd_start(event.widget, event)
