class Base:
  def __init__(self, name) -> None:
    self.__name = name

  @property
  def name(self):
    return self.__name

  def __repr__(self) -> str:
    return f'Base(name={self.name})'
