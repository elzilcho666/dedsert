import random, sys, time
class playing_field:
  _players = {}
  def __init__(self):
    self.min_x = 0
    self.max_x = 100
    self.min_y = 0
    self.max_y = 100
  def sendplayerpos(self):
    return self._players
  def getx(self, player):
    return self._players[player]['x']
  def gety(self, player):
    return self._players[player]['y']
  def movex(self, player, x):
    if(x == 1):
      if(self._players[player]['x'] + 1 <= self.max_x):
        tempx = self._players[player]['x']
        tempx += 1
        self._players[player]['x'] = tempx
    if(x == -1):
      if(self._players[player]['x'] - 1 >= self.min_x):
        tempx = self._players[player]['x']
        tempx -= 1
        self._players[player]['x'] = tempx
  def movey(self, player, y):
    if(y == 1):
      if(self._players[player]['y'] + 1 <= self.max_y):
        tempy = self._players[player]['y']
        tempy += 1
        self._players[player]['y'] = tempy
    if(y == -1):
      if(self._players[player]['y'] - 1 >= self.min_y):
        tempy = self._players[player]['y']
        tempy = tempy - 1
        self._players[player]['y'] = tempy
  def change_player_pos(self, name):
    random.seed()
    self._players[player] = {'x':random.randrange(100),'y':random.randrange(100)}
  def addPlayer(self, player):
    random.seed()
    self._players[player] = {'x':random.randrange(100),'y':random.randrange(100)}
  def removePlayer(self, player):
    del self._players[player]
pitch = playing_field()
players = {}
sinbin = {}
removed_player = {}
class Player():
  def __init__(self, name):
    self.yellow_cards = 0
    self.name = name
    self._x = pitch.getx(self.name)
    self._y = pitch.gety(self.name)
  def sinbinned(self):
    self.countsincesin = 0
  def sayname(self):
    pass
  def moveup(self):
    pitch.movex(self.name, 1)
    self._x = pitch.getx(self.name)
    self.saypos()
    theRef.checkLegalMove(self.name)
  def movedown(self):
    pitch.movex(self.name, -1)
    self._x = pitch.getx(self.name)
    self.saypos()
    theRef.checkLegalMove(self.name)
  def moveright(self):
    pitch.movey(self.name, 1)
    self._y = pitch.gety(self.name)
    self.saypos()
    theRef.checkLegalMove(self.name)
  def moveleft(self):
    pitch.movey(self.name, -1)
    self._y = pitch.gety(self.name)
    self.saypos()
    theRef.checkLegalMove(self.name)
  def move(self):
    options = {'up': self.moveup, 'down': self.movedown, 'left': self.moveleft, 'right': self.moveright}
    random.seed()
    options[random.choice(options.keys())]()
  def saypos(self):
    pass
    print '[%s] My pos is x:%s, y:%s' % (self.name, self._x, self._y)
  def asktoplay(self):
    self.countsincesin += 1
    if self.countsincesin == 10:
      theRef.asktoplay(self.name)
class Ref():
  def __init__(self):
    self.players_yellowcards = {}
  def asktoplay(self, player):
    del sinbin[player]
    pitch.addPlayer(player)
  def checkLegalMove(self, player):
    self.pos = pitch.sendplayerpos()
    try:
      for otherplayer in self.pos:
        if(player != otherplayer):
          if self.pos[otherplayer]['x'] - self.pos[player]['x'] in range(0,2):
            if self.pos[otherplayer]['y'] - self.pos[player]['y'] in range(0,2):
              self.bookPlayer(player, otherplayer)
            if self.pos[otherplayer]['y'] + self.pos[player]['y'] in range(-2,0):
              self.bookPlayer(player, otherplayer)
          if self.pos[otherplayer]['x'] + self.pos[player]['x'] in range(-2,0):
            if self.pos[otherplayer]['y'] - self.pos[player]['y'] in range(0,2):
              self.bookPlayer(player, otherplayer)
            if self.pos[otherplayer]['y'] + self.pos[player]['y'] in range(-2,0):
              self.bookPlayer(player, otherplayer)
    except:
      pass
  def bookPlayer(self, player, otherplayer):
    print 'booking %s for being at %s, %s to close to %s in pos %s, %s' % (player, self.pos[player]['x'], self.pos[player]['y'], otherplayer, self.pos[otherplayer]['x'], self.pos[otherplayer]['y'])
    pitch.change_player_pos(player)
    if player not in self.players_yellowcards:
      self.players_yellowcards[player] = 1
    else:
      self.players_yellowcards[player] += 1
    if(self.players_yellowcards[player] == 2):
      sinbin[player] = players[player]
      players[player].sinbinned()
      pitch.removePlayer(player)
    if self.players_yellowcards[player] > 2:
      removed_player[player] = players[player]
      pitch.removePlayer(player)
      print '%s has been taken off the pitch for muliple violations' % (player)
realtime = False
if(len(sys.argv) > 1):
  if(sys.argv[1] == 'realtime'):
    realtime = True

names = ['Adam', 'John', 'Samantha', 'Jenny',  'Josh', 'Cian', 'Herbert', 'Naomi', 'Evan', 'Arthur']
for name in names:
  pitch.addPlayer(name)
  players[name] = Player(name)
theRef = Ref()
moves = 0
while(len(players)>1):
  moves += 1
  print 'Move %s:' % (moves)
  print '------------------------------'
  if len(removed_player)>= 1:
    for player in removed_player:
       players.pop(player, None)
       sinbin.pop(player, None)
  for player in players:
    if player not in sinbin:
      players[player].move()
    else:
      players[player].asktoplay()
  if realtime == True:
    time.sleep(1)

print 'THE WINNER IS: %s, the game took %s moves to complete' % (players.keys()[0], moves)