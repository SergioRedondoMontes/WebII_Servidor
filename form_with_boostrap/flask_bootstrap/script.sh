#echo "Activating Virtual Enviroment..."
#source python3boostrap/bin/activate

echo "Setting path to app.py ..."
export FLASK_APP=app.py

echo "Setting debug mode ..."
export FLASK_DEBUG=1

flask run
# Lanzar aplicación con threads
# flask run --with-threads

# nohup flask run -> ejecuta procceso sin padre, por lo que ningun proceso podría matarlo

# Mientras estamos en desarrollo
# Comando
# sudo nohup flask run --0.0.0.0 --port 80 &
# Explicacion
# sudo nohup flask run --0.0.0.0 (Cualquier direccion IP) --port 80 (Puerto 80) & (Segundo plano y devuelve control consola)

# Mientras estamos en produccion
# Comando
# crontab -e
# @reboot sh /home/usuario/*/scripts/script.sh


# Cosas a tener en cuenta
# python app.py si tiene un error no reiniciaria en caso de error
# flask run si tiene un error se reinicia automáticamente
