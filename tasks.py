import invoke
import livereload
import os
import shutil

server = livereload.Server()

def dir(path):
    return os.path.abspath(os.path.join(os.getcwd(), path))

@invoke.task
def clean(ctx):
    if os.path.exists('./build'):
        shutil.rmtree('./build')


@invoke.task(pre=[clean])
def build(ctx):
    invoke.run('sphinx-build -c . ./src ./build', pty=True)


@invoke.task(pre=[build])
def serve(ctx):
    server.watch(dir('./src/'), lambda: build(ctx))

    server.serve(
        root='./build',
        host='localhost',
        liveport=35729,
        port=8080
    )
