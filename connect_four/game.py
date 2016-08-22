class Game:
	WIDTH = 7
	HEIGHT = 6

	""" Initialization """
	def __init__(self):
		self.is_game_over = False
		self.current_player = 1
		# initialize 2D array board filled with 0
		self.board = [[0 for y in xrange(self.HEIGHT)] for x in xrange(self.WIDTH)]
		self.last_move = [-1, -1]
	
	""" Start new game of Connect 4"""
	def start(self):
		print 'Starting new game...'
		self.__init__()
		self.__print_board()
		while not self.is_game_over:
			col_num = raw_input('Player ' + str(self.current_player) + '\'s turn to move: ')
			#print 'You entered: ' + str(col_num)
			self.__add_to_col(int(col_num))
			self.__print_board()
			self.__check_game_over()
			self.__switch_players()

	""" Prints to console the current board """
	def __print_board(self):
		# y from 6 to 0
		for y in range(self.HEIGHT - 1, -1, -1):
			line = '||'
			# x from 0 to 7
			for x in range(self.WIDTH):
				line = line + ' ' + str(self.board[x][y]) + ' ||'
			print line
		print '-------------------------------------'		
		print '|| 0 || 1 || 2 || 3 || 4 || 5 || 6 ||'
		print '-------------------------------------'

	""" Adds the current_player's peice to the specified column number """
	def __add_to_col(self, col_num):
		for y in range(self.HEIGHT):
			if (self.board[col_num][y] == 0):
				self.board[col_num][y] = self.current_player
				self.last_move = [col_num, y]
				break
		else:
			print 'Error: Column is full!'
			
	""" Checks for 4 pieces in a row in any direction. Changes the
		is_game_over member variable to True if so.
	"""
	def __check_game_over(self):
		self.__check_vertical()
		self.__check_horizontal()
		self.__check_right_diagonal()
		self.__check_left_diagonal()
	
	def __check_vertical(self):
		values = ''
		x = self.last_move[0]
		for y in range(self.HEIGHT):
			values = values + str(self.board[x][y])
		self.__check_four_in_a_row(values)
		
	def __check_horizontal(self):
		values = ''
		y = self.last_move[1]
		for x in range(self.WIDTH):
			values = values + str(self.board[x][y])
		self.__check_four_in_a_row(values)
		
	''' Check four in a row in / direction '''
	def __check_right_diagonal(self):
		x = self.last_move[0]
		y = self.last_move[1]
		values = str(self.board[x][y])

		x = x - 1
		y = y - 1
		while x >= 0 and y >= 0:
			values = str(self.board[x][y]) + values
			x = x - 1
			y = y - 1

		x = self.last_move[0] + 1
		y = self.last_move[1] + 1
		while x < self.WIDTH and y < self.HEIGHT:
			values = values + str(self.board[x][y])
			x = x + 1
			y = y + 1

		self.__check_four_in_a_row(values)
		
	''' Check four in a row in \ direction '''
	def __check_left_diagonal(self):
		x = self.last_move[0]
		y = self.last_move[1]
		values = str(self.board[x][y])

		x = x - 1
		y = y + 1
		while x >= 0 and y < self.HEIGHT:
			values = str(self.board[x][y]) + values
			x = x - 1
			y = y + 1

		x = self.last_move[0] + 1
		y = self.last_move[1] - 1
		while x < self.WIDTH and y >= 0:
			values = values + str(self.board[x][y])
			x = x + 1
			y = y - 1

		self.__check_four_in_a_row(values)

	def __check_four_in_a_row(self, values_str):
		if values_str.find('1111') != -1:
			self.is_game_over = True
			print 'Player 1 wins!'
		elif values_str.find('2222') != -1:
			self.is_game_over = True
			print 'Player 2 wins!'

	""" Changes the current_player member variable fromo 1 to 2 and vise-versa """
	def __switch_players(self):
		if self.current_player == 1:
			self.current_player = 2
		else:
			self.current_player = 1


