from flask import Flask, request, render_template
import math

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def trig():
    angle = float(request.form.get('angle', 0))
    function = request.form.get('function', '')
    unit = request.form.get('unit', '')
    precision = int(request.form.get('precision', 0))
    if unit == 'radians':
        angle = round(angle/3.14*180, 3)
    if function == 'Sin':
        sin_val = math.sin(math.radians(angle))
        sin_val = round(sin_val, precision)
        return render_template('trig.html', sin_val=sin_val, angle=angle, function=function)
    elif function == 'Cos':
        cos_val = math.cos(math.radians(angle))
        cos_val = round(cos_val, precision)
        return render_template('trig.html', cos_val=cos_val, angle=angle, function=function)
    elif function == 'Tg':
        tg_val = math.tan(math.radians(angle))
        tg_val = round(tg_val, precision)
        return render_template('trig.html', tg_val=tg_val, angle=angle, function=function)
    elif function == 'Ctg':
        ctg_val = 1/math.tan(math.radians(angle))
        ctg_val = round(ctg_val, precision)
        return render_template('trig.html', ctg_val=ctg_val, angle=angle, function=function)
    else:
        return render_template('trig.html')


if __name__ == "__main__":
    app.run(debug=True)