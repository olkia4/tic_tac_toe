import random
from game import *

class Agent007():
  def __init__(self, game, gamma=0.5, rand=0.1, player=1):
    self.game = game
    self.gamma = gamma
    self.rand = rand
    self.player = player
    self.V_P = dict()

  def value(self, state):
    return self.V_P.get(tuple(state), 0.0)

  def best_action_now(self, game, func):
    good_actions = []
    tmp = self.value(game.action_list()[0])
    for action in game.action_list():
      tmp = func(tmp, self.value(action))
    for action in game.action_list():
      if self.value(action) == tmp:
        good_actions.append(action)
    return good_actions


  def learn(self, count_of_games):
    for i in range(count_of_games):
      now_game = self.game()
      tmp, action = self.best_actions(now_game)
      while now_game.playable():
        action = self.action_with_learn(now_game, action)

  def select_action(self, game):
    if self.player == game.player_now:
      return random.choice(self.best_action_now(game, max))
    return random.choice(self.best_action_now(game, min))

  def best_actions(self, game):
    best_action = self.select_action(game)
    selected_action = best_action
    if random.random() < self.rand:
      selected_action = random.choice(game.action_list())
    return best_action, selected_action


  def reward(self, game):
    if game.check_winner() == format_point(self.player): #если выиграли
      return 1
    elif game.check_winner() == '-' or game.check_winner() == "c": #если ничья
      return 0
    else: #если проиграли
      return -1


  def action_with_learn(self, game, action):
    game.do_action(action)
    r = self.reward(game) #получили какой-то реворд
    random_next_action = 0 #вознагрождение от след состояния пока 0
    next_state = 0 #след действие еще не выбрали
    best_next_action = 0
    if game.playable():
      best_next_action, random_next_action = self.best_actions(game) #дописать функцию, где будет еще рандом(иначе зациклимся)
      next_state = self.value(best_next_action) #берем САМОЕ лучшее состояние
    self.V_P[tuple(action)] = self.value(action) + self.gamma * (r + self.gamma * next_state)
    #V(s) = Е(R_{t} + gamma*G_{t})  /// где G_{t} = reward + gamma*G_{t+1}
    #(V(s) = pi(a|s) + p(r, s'|s, a)[r + gamma*v(s')])
    return random_next_action #возвращаем рандомное действие


  def game_now(self, to_print=False):
    now_game = self.game()
    while now_game.playable():
      now_game.do_action(self.select_action(now_game))
      if to_print:
        now_game.print_table()
    winner = now_game.check_winner()
    if to_print:
      if winner == "0":
        print("Выиграли нолики")
      elif winner == "X":
        print("Выиграли крестики")
      else:
        print("Ничья! Давайте жить дружно!!!")
    return now_game.check_winner()

  def select_action_for_interactive_game(self, game, player):
      if player == 1:
        return random.choice(self.best_action_now(game, max))
      return random.choice(self.best_action_now(game, min))
