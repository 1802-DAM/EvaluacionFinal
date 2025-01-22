from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET' , 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_por_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_descuento = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - total_descuento

        return render_template('ejercicio1.html', nombre=nombre,
                           total_sin_descuento=total_sin_descuento,
                           total_descuento=total_descuento,
                           total_a_pagar=total_a_pagar,
                            mostrar_resultado=True)


    return render_template('ejercicio1.html')


usuarios_registrados = {
            "juan": "admin",
            "pepe": "user"
        }



@app.route('/ejercicio2', methods=['GET' , 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

       
        if usuario in usuarios_registrados:

            if usuarios_registrados[usuario] == contrasena:

                if usuario == "juan":
                    mensaje = "Bienvenido administrador juan"
                else:
                    mensaje = "Bienvenido usuario pepe"
            else:
                mensaje = "Contraseña incorrecta"
        else:
            mensaje = "Usuario no encontrado"

        return render_template('ejercicio2.html', mensaje=mensaje)
    else:
        return render_template('ejercicio2.html')





if __name__ == '__main__':
    app.run(debug=True)