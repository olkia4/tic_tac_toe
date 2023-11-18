import random

def format_point(x):
  if x == 1337:
    return " "
  if x == 1:
    return "X"
  return "0"

class Crosses_zeros():
  def __init__(self):
    self.table = [1337 for i in range(9)]
    self.player_now = 1

  def winner_positions(self):
    return [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]

  def do_action(self, action):
    self.table = action
    self.player_now = 1 - self.player_now

  def action_list(self):
    actions = []
    for i in range(9):
      if (self.table[i] == 1337):
        actions.append(self.table[:i] + [self.player_now] + self.table[i + 1:])
    return actions

  def playable(self):
    return self.check_winner() == "c"

  def check_winner(self):
    sum_now = 0
    for combination in self.winner_positions():
      for pos in combination:
        sum_now += self.table[pos]
      if sum_now == 0:
        return "0"
      if sum_now == 3:
        return "X"
      sum_now = 0
    if any(self.action_list()):
      return "c"
    return "-"


  def print_table(self):
    for i in range(9):
      print(format_point(self.table[i]), end=("\n" * 0**(2 - i % 3) + " " * (1 - 0**(2 - i % 3))))
    print()

  def table_to_string(self):
    a = "<code>"
    for i in range(5):
      for j in range(5):
        if (i % 2 == 1) and (j % 2 == 1):
          a += '+'
        elif (i % 2 == 1):
          a += '-'
        elif (j % 2 == 1):
          a += "|"
        else:
          a += format_point(self.table[(i // 2) * 3 + j // 2])
      a += '\n'
    a += "</code>"
    return a

