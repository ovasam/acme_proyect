# SPECIAL MESSAGE # 
def adios():
    print('''
+++++++++++++++++++++++++++++
++ Por favor vuelva pronto ++
+++++++++++++++++++++++++++++
          ''')


def opcion_invalida():
    print('''
+++++++++++++++++++++++++++++++
+       OPCION INVALIDA       +
+      (use solo numeros)     +
+++++++++++++++++++++++++++++++
                  ''')

def fuera_de_rango():
    print('''
+++++++++++++++++++++++++++++++
+        FUERA DE RANGO       +
+            (1-7)            +
+++++++++++++++++++++++++++++++
                  ''')
    

def clave_incorrecta():
    print('''
+++++++++++ ERROR +++++++++++
+    Contraseña Incorrecta  +
+++++++++++++++++++++++++++++
          ''')
    
def no_opcion():
    print('''
+++++++++++++++++++++++++++++++++++++++++
+   OPCION NO IMPLEMENTADA. LO SIENTO   +
+++++++++++++++++++++++++++++++++++++++++
''')
    
def monto_invalido():
    print(""" 
+++++++++++++++++++++++++++++++++++++++++++++++++
+ Por favor indique un monto valido (mayor a 0) +
+++++++++++++++++++++++++++++++++++++++++++++++++        
         """)
    
def saldo_insuficiente():
    print("""
+++++++++++++++++++++++++++++++++++++++++++++++++
+ No dispones del saldo suficiente en tu cuenta +
+         Intenta con un monto menor            +
+++++++++++++++++++++++++++++++++++++++++++++++++        
                      """)
    
def retiro_realizado(arreglo, n_cuenta):
    print(f'''
+++++++++++++++++++++++++++++++
+      RETIRO COMPLETADO      +
+ Saldo > {arreglo[n_cuenta]['BILLETERA']}                +
++++++++++++++++++++++++++++++++
                      ''')
    
def cuenta_inexistente():
    print("""
+++++++++++++++++++++++++++++++++
+  Error: La cuenta no existe.  +
+++++++++++++++++++++++++++++++++
              """)