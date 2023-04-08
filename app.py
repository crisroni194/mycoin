@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar que el nombre de usuario no esté en uso
        if db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone() is not None:
            return 'El nombre de usuario ya está en uso'

        # Crear el nuevo usuario
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, generate_password_hash(password)))
        db.commit()

        # Redirigir al usuario a la página de inicio de sesión
        return redirect(url_for('login'))

    # Mostrar el formulario de registro
    return render_template('register.html')
