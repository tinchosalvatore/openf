import install
import uninstall

def update():
    print(">>> Iniciando actualización de openf...")
    
    print("\n>>> Paso 1: Eliminando versión anterior...")
    uninstall.uninstall()
    
    print("\n>>> Paso 2: Instalando nueva versión...")
    install.install()
    
    print("\n>>> Actualización completada con éxito.")

if __name__ == "__main__":
    update()
