from invoke import task, run

#elimina los archivos generados al pasar los test
@task 
def clean(ctx):
    print('Cleaning...')
    run ("rm -d -r tests/__pycache__")
    run ("rm -d -r src/__pycache__")
    run ("rm tests/.coverage")
    print ('Done!')

#instala las dependencias
@task
def install(ctx):
    print('Instalando...')
    run ('pip install -r requirements.txt')
    print ('Done!')

#ejecuta los test unitarios
@task
def test(ctx):
    with ctx.cd('tests'):
        ctx.run ('python -m unittest discover -s . -p "Test*.py"')

@task
def coverage(ctx):
    with ctx.cd('tests'):
        ctx.run ('coverage run -m unittest discover -s . -p "Test*.py"')  
        ctx.run ('coverage report')