# saludos/views.py

from django.shortcuts import render

def generador_carta(request):
    # 1. Verificar el método de solicitud: ¿Es GET o POST?
    
    if request.method == 'POST':
        # Si es POST, significa que el usuario envió el formulario
        
        # Obtener los datos del formulario (el 'name' de los inputs)
        nombre = request.POST.get('nombre') 
        carrera = request.POST.get('carrera')
        
        # 2. Lógica para generar la carta
        carta_generada = f"""
        Estimado/a Reclutador/a,
        
        Me dirijo a usted con gran entusiasmo para expresar mi interés en la posición de **{carrera}**. 
        
        Aunque soy un estudiante, mi nombre es **{nombre}** y estoy comprometido/a a aplicar mis conocimientos y mi deseo de aprender en su equipo.
        
        Espero tener la oportunidad de discutir cómo mis habilidades pueden beneficiar a su organización.
        
        Atentamente,
        {nombre}
        """
        
        # 3. Preparar el contexto para la plantilla de RESULTADO
        contexto = {
            'carta': carta_generada.replace('\n', '<br>'), # Reemplazamos saltos de línea por <br> para HTML
            'nombre_user': nombre
        }
        
        # Renderizar una plantilla de resultado, no la del formulario
        return render(request, 'saludos/resultado.html', contexto)

    else:
        # Si es GET, significa que es la primera vez que se visita la página
        # Simplemente muestra la plantilla del formulario
        return render(request, 'saludos/formulario.html')