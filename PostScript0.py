import os

def	nrange(a,boite, np):
	pas = (b - a) / np
	return ( a + i * pas for i in range(np + 1))
	
def preambule(nomFichier,boite, zoom, delta):
	c = [x * zoom * delta for x in boite]
	s_debut = ("%!PS-Adobe-2.0 EPSF-2.0\n"
			"%%BoundingBox: {0[0]:.1f} {0[1]:.1f} {0[2]:.1f} {0[3]:.1f}\n"
			"{1} {1} scale\n").format(c, zoom)
	with open(nomFichier + ".esp", 'w') as f:
		f.write(s_debut)

def fin(nomFichier):
	s_fin = "\nshowpage\n"
	with open(nomFichier + ".esp", 'a') as f:
		f.write(s_fin)

def ajouteCourbe(nomFichier, liste, boite, zoom, epaisseurTrait, rgb):
	with open(nomFichier + ".esp", 'a') as f:
		f.write("\nnewpath\n")
		for i, point in enumerate(liste):
			if i == 0:
				f.write("	{0[0]: .4f}	{0[1]: .4f}	".format(point))
				f.write("moveto\n")
			elif (boite[0] <= point[0] <= boite[2]
				and boite[1] <= point[1] <= boite[3] ):
				f.write("	{0[0]: .4f}	{0[1]: .4f}	".format(point))
				f.write("lineto\n")
		f.write("{1} {0} div setlinewidth\n"
				"{2[0]} {2[1]} {2[2]} setrgbcolor\n"
				"stroke\n".format(zoom, epaisseurTrait, rgb))

def affiche(nomFichier):
	os.system("evince {0}.esp 2> /dev/null &".format(nomFichier))

if __name__ == "__main__":
	from math import pi, cos, sin, floor
	
	N, a, b = 1000, 0, 1 + floor(38*pi)
	nomFichier = "polar"
	zoom, epaisseurTrait, rgb = 100, 0.4, (0,0,1)
	boite = [-1.5, -1.5, 1.5, 1.5]
	
	def f(theta):
		return 1 + cos(theta*20/19)/3
	
	l = ([f(theta) * cos(theta), f(theta) * sin(theta)] for theta in nrange(a, b, N))
	
	preambule (nomFichier, boite, zoom, 1.1)
	ajouteCourbe (nomFichier, l, boite, zoom, epaisseurTrait, rgb)
	fin (nomFichier)
	affiche(nomFichier)
