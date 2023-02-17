import ui


class View(ui.View):
  def __init__(self):
    self.bg_color = 1

  def draw(self):
    margin = 16
    sq = 320
    width = sq
    height = sq

    for x in range(width):
      rect = ui.Path.rect(x + margin, margin, 1, height)
      p = x / sq
      ui.set_color(p)
      rect.fill()


if __name__ == '__main__':
  view = View()
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

