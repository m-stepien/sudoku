
from flask import Flask, render_template, jsonify, request
import sudo
app = Flask(__name__)
@app.route("/")
def start():
	return render_template('index.html')
@app.route("/rozwiaz")
def rozwiaz():
	return render_template('rozwiaz.html')
@app.route("/solve_json",methods=['POST'])
def solve_json():
	sudoku=sudo.Sudoku()
	data = request.get_json()
	sudoku.create_from_list(data)
	sudoku.backtrack()
	solution = sudoku.get_values_location()
	return jsonify(solution)
@app.route("/game", methods=['GET', 'POST'])
def game(n_blank=43):
	if request.method == "POST":

		data=request.get_json()
		n_blank=data
	sudoku = sudo.Sudoku()
	sudoku.create_unbound_place(0)
	sudoku.create_unbound_place(4)
	sudoku.backtrack()
	sudoku.set_to_blank(n_blank)
	data=sudoku.get_values_location()

	data_json = jsonify(data)
	return data_json
@app.route("/check", methods=['POST'])
def check():
	if request.method == "POST":
		data=request.get_json()
		defult_sudoku = data[0]
		solution = data[1]
		sudoku_solution = sudo.Sudoku()
		sudoku_good = sudo.Sudoku()
		sudoku_good.create_from_list(defult_sudoku)
		sudoku_good.backtrack()
		sudoku_solution.create_from_list(defult_sudoku)
		sudoku_solution.create_from_list(solution)
		wrong = sudoku_solution.is_equeal(sudoku_good)
		return jsonify(wrong)
	return "<p>ok</p>"
	# solved_sudoku = Sudoku()
	# for element in user_solution:
	# 	solved_sudoku[element[0]][element[1]][element[2]] = element[3]
	# correct_solution = Sudoku()
	# for element in sudoku_to_solve:
	# 	correct_solution[element[0]][element[1]][element[2]] = element[3]
	# correct_solution.backtrack()
	# wrong_place_data = mis_index
	# return jsonify(wrong_place_data)

def is_same(sd1, sd2):
	mis_index = []
	for i in range(0,9):
		for j in range(0,3):
			for k in range(0,3):
				if sd1[i][j][k]!=sd2[i][j][k]:
					mis_index.append((i,j,k))
	return mis_index