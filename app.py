from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def fizzbuzz():
    numbers = range(1, 101)
    fizzbuzz_list = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            fizzbuzz_list.append('Fizzbuzz')
        elif num % 3 == 0:
            fizzbuzz_list.append('Fizz')
        elif num % 5 == 0:
            fizzbuzz_list.append('Buzz')
        else:
            fizzbuzz_list.append(num)
    return render_template("fizzbuzz.html")