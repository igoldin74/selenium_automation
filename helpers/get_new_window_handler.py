class GetWindowHandler(object):

    def __init__(self, original_windows):
        self.original_windows = original_windows

    def __call__(self, app):
        new_windows = set(app.window_handles)
        diff = list(set(new_windows) - set(self.original_windows))
        if len(diff) == 1:
            return diff[0]
        else:
            return False