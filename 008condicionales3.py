usuario_logueado = True
usuario_admin = False
if usuario_logueado and usuario_admin: # or
    print('administrador')
elif usuario_logueado:
    print('acceeso al sistema') 
else:
    print('debes iniciar secion') 
