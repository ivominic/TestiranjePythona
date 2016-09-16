import turtle

lista = ['red', 'green', 'blue', 'black']

def crtajFiguru(brojTjemena, duzinaLinije):
    for tjeme in range(brojTjemena):
        turtle.forward(duzinaLinije)
        turtle.right(360 / brojTjemena)
        turtle.color(lista[tjeme % len(lista)])
        for i in range(brojTjemena):
            turtle.forward(duzinaLinije / 2)
            turtle.right(360 / brojTjemena)
    return


crtajFiguru(13,100)