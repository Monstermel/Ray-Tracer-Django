from django import forms

class RayTracerForm(forms.Form):
    num_threads = forms.CharField(label='Numero de hilos', initial='1',  max_length=255)
    num_proporcion = forms.CharField(label='Numerador aspecto', initial='3', max_length=255)
    den_proporcion = forms.CharField(label='Denominador aspecto', initial='2', max_length=255)
    ancho_img = forms.CharField(label='Ancho de imagen', initial='400', max_length=255)
    muestras_pixel = forms.CharField(label='Muestras por pixel', initial='100', max_length=255)
    max_rayos = forms.CharField(label='Numero maximo de rayos', initial='50', max_length=255)
    x_coord = forms.CharField(label='Coordenada x de la camara', initial='13.0', max_length=255)
    y_coord = forms.CharField(label='Coordenada y de la camara', initial='2.0', max_length=255)
    z_coord = forms.CharField(label='Coordenada z de la camara', initial='3.0', max_length=255)
    R_e1 = forms.CharField(label='Valor R esfera 1', initial='0.4', max_length=255)
    G_e1 = forms.CharField(label='Valor G esfera 1', initial='0.2', max_length=255)
    B_e1 = forms.CharField(label='Valor B esfera 1', initial='0.1', max_length=255)
    R_e2 = forms.CharField(label='Valor R esfera 2', initial='0.7', max_length=255)
    G_e2 = forms.CharField(label='Valor G esfera 2', initial='0.6', max_length=255)
    B_e2 = forms.CharField(label='Valor B esfera 2', initial='0.5', max_length=255)
    ref = forms.CharField(label='Indice de refraccion', initial='1.5', max_length=255)
    rand = forms.CharField(label='Esferas aleatorias', initial='0', max_length=255)



