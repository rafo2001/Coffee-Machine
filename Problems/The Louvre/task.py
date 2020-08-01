class Painting:
    museum = "the Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year
        print(f'"{title}" by {painter} ({str(year)}) hangs in {self.museum}.')


tit1 = input()
paint1 = input()
year1 = int(input())
new_paint = Painting(tit1, paint1, year1)


