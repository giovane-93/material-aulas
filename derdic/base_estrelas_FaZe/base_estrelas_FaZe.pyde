coresC = (
          (111, 15, 124),
          (102, 100, 47),
          (47, 102, 99),
          (103, 47, 68),
          (232, 228, 16),
          (255, 255, 255),
          )

estrelas = []  # lista de objetos

def setup():
    """ Define área de desenho e popula lista de estrelas """
    # fullScreen()
    size(400, 700)  # área de desenho (width, height)
    meia_largura, meia_altura = width / 2., height / 2. # floats
    for _ in range(6):
        e = Estrela(meia_largura, meia_altura)
        estrelas.append(e)

def draw():
    colorMode(RGB)
    if keyPressed:
        cor1 = color(* coresC[0])
        cor2 = color(* coresC[1])
        cor3 = color(* coresC[2])
    else:
        cor1 = color(* coresC[3])
        cor2 = color(* coresC[4])
        cor3 = color(* coresC[5])
    colorMode(HSB)
    paleta = (color(hue(cor1),255,255),
              color(hue(cor2),255,255),
              color(0,255,255),
              color(hue(cor1),255,255),
              color(hue(cor2),255,255),
              color(hue(cor3),0,255),
              )    
    """ Limpa a tela, desenha e atualiza estrelas """
    background(0)  # atualização do desenho, fundo preto
    for i, estrela in enumerate(estrelas):
        estrela.desenha(paleta[i]) #10 if mouseX > 200 else 30)
        estrela.anda()

class Estrela():
    """ Classe Estrela, cor sorteada, tamanho sorteado por default """

    def __init__(self, px, py, ptamanho=None):
        self.x = px
        self.y = py
        if ptamanho:
            self.tamanho = ptamanho
        else:
            self.tamanho = random(50, 200)
        self.vx = random(-2,2)
        self.vy = random(-2,-4)
        sorteio = random(128)
        self.cor = color(128 + sorteio,  # R
                         0,  # G
                         128 + sorteio,  # B
                         200)  # alpha

    def desenha(self,cor, pontas=10, raio1=50, raio2=100):
        """ Desenha polígono em torno das coordenadas do objeto """
        noStroke()
        fill(cor)
        pushMatrix()
        translate(self.x, self.y)
        rotate(radians(frameCount))
        estrela(0, 0, pontas, mouseY, raio2)
        popMatrix()
    
    
    def anda(self):
        """ atualiza a posição do objeto e devolve do lado oposto se sair """
        self.x += self.vx
        self.y += self.vy
        metade = self.tamanho / 2
        if self.x > width + metade:
            self.vx = -self.vx
        if self.y > height + metade:
            self.vy = -self.vy
        if self.x < -metade:
            self.vx = -self.vx
        if self.y < -metade:
            self.vy = -self.vy
            
            
def estrela(cx, cy, pontas, raio1, raio2):    
    pontos = pontas * 2
    parte = 360. / pontos
    beginShape() # comece a forma!
    for p in range(pontos): # para cada p
        angulo = radians(p * parte) # calcula angulo
        if p % 2 == 0: # se for par
            raio = raio1
        else: # senão, se for impar
            raio = raio2
        x = cx + raio * sin(angulo)
        y = cy + raio * cos(angulo)
        vertex(x, y) # vertex é um ponto
    endShape(CLOSE) # termina forma