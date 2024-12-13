from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    result = None
    conversion_type = None

    if request.method == 'POST':
        number = request.form.get('number')
        conversion_type = request.form.get('conversion_type')

        if conversion_type == 'decimal_to_binary':
            result = bin(int(number))[2:]  # Convert to binary
        elif conversion_type == 'binary_to_decimal':
            result = int(number, 2)  # Convert binary to decimal
        elif conversion_type == 'decimal_to_octal':
            result = oct(int(number))[2:]  # Convert to octal
        elif conversion_type == 'octal_to_decimal':
            result = int(number, 8)  # Convert octal to decimal
        elif conversion_type == 'decimal_to_hex':
            result = hex(int(number))[2:].upper()  # Convert to hexadecimal
        elif conversion_type == 'hex_to_decimal':
            result = int(number, 16)  # Convert hexadecimal to decimal
        elif conversion_type == 'binary_to_octal':
            result = oct(int(number, 2))[2:]  # Convert binary to octal
        elif conversion_type == 'octal_to_binary':
            result = bin(int(number, 8))[2:]  # Convert octal to binary
        elif conversion_type == 'binary_to_hex':
            result = hex(int(number, 2))[2:].upper()  # Convert binary to hexadecimal
        elif conversion_type == 'hex_to_binary':
            result = bin(int(number, 16))[2:]  # Convert hexadecimal to binary
        elif conversion_type == 'octal_to_hex':
            result = hex(int(number, 8))[2:].upper()  # Convert octal to hexadecimal
        elif conversion_type == 'hex_to_octal':
            result = oct(int(number, 16))[2:]  # Convert hexadecimal to octal

    return render_template("front.html", result=result, conversion_type=conversion_type)

if __name__ == '__main__':
    app.run(debug=True)