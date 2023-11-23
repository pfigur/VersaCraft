#!/usr/bin/env python3

import typer
from typer import Typer, Argument, Context, Option, Exit
from typing_extensions import Annotated

import click
from pysend import py_controller

__VERSION = '0.0.1a0'
app = Typer()


def version(arg):
    if arg:
        print(f'VersaCraft V-{__VERSION}')
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def callback(
        ctx: Context,
        version: bool = Option(False,
                               '--version', '-v', '--v',
                               callback=version,
                               is_flag=True, is_eager=True,
                               case_sensitive=False)):
    if ctx.invoked_subcommand:
        return
    print(f'É necessário algum comando. Para maiores informações utilize: versa --help')


@app.command(short_help='Inicia projetos Python')
def python():
    py_controller.pergunta_env()


@app.command(name='outra-lang', help='Comando existe')
def outra(nome: str):
    pass


if __name__ == '__main__':
    app()
