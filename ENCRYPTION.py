#------------- IMPORT ------------#
from os import system as c
import marshal
import base64
import zlib
try:
    from Cython.Build.BuildExecutable import build as execute
except:
    c('clear')
#---------------- LOGO -----------#
logo='''


╔═══╦═╗─╔╦═══╗
║╔══╣║╚╗║║╔═╗║
║╚══╣╔╗╚╝║║─╚╝
║╔══╣║╚╗║║║─╔╗
║╚══╣║─║║║╚═╝║
╚═══╩╝─╚═╩═══╝
╔═══╦╗──╔╦════╦╗─╔╦═══╦═╗─╔╗
║╔═╗║╚╗╔╝║╔╗╔╗║║─║║╔═╗║║╚╗║║
║╚═╝╠╗╚╝╔╩╝║║╚╣╚═╝║║─║║╔╗╚╝║
║╔══╝╚╗╔╝──║║─║╔═╗║║─║║║╚╗║║
║║────║║───║║─║║─║║╚═╝║║─║║║
╚╝────╚╝───╚╝─╚╝─╚╩═══╩╝─╚═╝
      Creador: Angel Del Villar                                      
                                             

'''
#--------------- CLEAR FUNCTION -------------#
def clear():
    c('clear')
    print(logo)
    print(40*'-')
    print(' Telegram: https://t.me/+7UenLEmurs9iNjJh ')
    print(' GITHUB  : https://github.com/Angel-iluminaty')
    print(40*'-')
#----------- MAIN FUNCTION ------------#
def main():
    clear()
    print(' [A] MARSHAL ENCRYPTION ')
    print(' [B] BASE64  ENCRYPTION ')
    print(' [C] ZLIB    ENCRYPTION ')
    print(' [E] EXIT TERMINAL ')
    print(40*'-')
    option=input(' [?] CHOICE MENU : ')
    if option in ['a','A']:
        marshal_enc()
    elif option in ['b','B']:
        base64_enc()
    elif option in ['c','C']:
        zlib_enc()
    elif option in ['d','D']:
        cython_executable()
    else:
        exit(' TOOL EXITED :/')
#----------- MARSHAL ENCRYPTION --------------#
def marshal_enc():
    clear()
    file=input(' INGRESE EL NOMBRE DEL ARCHIVO : ')
    filex=input(' INGRESE EL NOMBRE DEL ARCHIVO DE SALIDA : ')
    try:
        file_open=open(file,'r').read()
    except:
        exit(' ERROR DE ARCHIVO NO ENCONTRADO !!')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write(run_code)
    out_put.close()
    print(40*'-')
    print(' [✓✓] ENCRYPTION COMPLETA :/ ')
    print(' [✓✓] ARCHIVO DE SALIDA GUARDAR COMO : '+filex)
#---------- BASE64 ENCRYPTION ------------#
def base64_enc():
    clear()
    input_file=input(' INGRESE LA RUTA DEL ARCHIVO  : ')
    output_file=input(' INGRESE LA RUTA DEL ARCHIVO DE SALIDA : ')
    try:
        file_open=open(input_file,'r').read()
    except:
        exit(' ERROR DE ARCHIVO NO ENCONTRADO !!')
    compile=base64.b64encode(file_open.encode())
    run_code=f'import base64\nexec(base64.b64decode({compile}))'
    out_put=open(output_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC ARCHIVO GUARDAR COMO : '+output_file)
#---------------- ZLIB ENCRYPTION -----------------#
def zlib_enc():
    clear()
    src=input(' INGRESE LA RUTA DEL ARCHIVO  : ')
    save_file=input(' INGRESE LA RUTA DEL ARCHIVO DE SALIDA : ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(' ERROR DE ARCHIVO NO ENCONTRADO !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'import zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETA :/')
    print(' [✓✓] ENC ARCHIVO GUARDAR COMO : '+save_file)
#--------------- CYTHON EXECUTABLE -----------------#
def cython_executable():
    clear()
    file=input(' INGRESE LA RUTA DEL ARCHIVO : ')
    try:
        filex=open(file,'r').read()
    except:
        exit(' ERROR DE ARCHIVO NO ENCONTRADO :/')
    error=filex.replace('	','    ')
    solve=open(file,'w').write(error)
    execute(file)
    clear()
    print(' [✓✓] EJECUTABLE DE CYTHON COMPLETO :")')
    save=file[:-3]
    print(' [✓✓] ARCHIVO EJECUTABLE GUARDAR COMO : '+save)
#----------------- END --------------#
main()
