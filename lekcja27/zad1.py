class BrowserHistory:
    def __init__(self):
        self.current_page = None
        self.back_stack = []
        self.history = []

    def go_to_page(self, page):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)
        self.current_page = page
        self.history.append(page)
        print(f"Przejście do: {self.current_page}")

    def go_back(self):
        if not self.back_stack:
            print("Brak wcześniejszych stron w historii.")
        else:
            self.current_page = self.back_stack.pop()
            print(f"Wrócono do: {self.current_page}")

    def print_history(self):
        print("Pełna historia przeglądania:")
        for page in self.history:
            print(f"- {page}")

bh = BrowserHistory()
bh.go_to_page("osu.ppy.sh/users/jakubic769")
bh.go_to_page("youtube.com")
bh.go_back()
bh.go_to_page("store.steampowered.com/app/Wiedmin_3_Dziki_Gon")
bh.print_history()
