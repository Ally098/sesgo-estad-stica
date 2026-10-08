import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Test de Sesgos Específicos", page_icon="📊", layout="centered")

st.title("📊 Cuestionario: Sesgos de Selección e Información")
st.write("Pon a prueba tus conocimientos identificando los sesgos exactos del temario de clase.")

# Lista de preguntas basadas únicamente en la fotografía aportada
preguntas = [
    {
        "id": 1,
        "titulo": "Pregunta 1",
        "caso": "Para evaluar el rendimiento académico general de una universidad completa, un equipo de investigación elige analizar únicamente las calificaciones de los estudiantes del último año de la carrera de Medicina.",
        "opciones": ["Sesgo de Selección", "Sesgo de Respuesta", "Sesgo de Confirmación", "Sesgo de Medición"],
        "correcta": "Sesgo de Selección",
        "explicacion": "¡Correcto! El sesgo de selección ocurre cuando los participantes elegidos para el estudio no representan fielmente a toda la población objetivo (en este caso, toda la universidad)."
    },
    {
        "id": 2,
        "titulo": "Pregunta 2",
        "caso": "Un reportero se coloca en la puerta de un supermercado ecológico a las 10:00 a.m. y pregunta a las primeras 20 personas que antes salgan si consideran que los alimentos orgánicos deberían ser más baratos.",
        "opciones": ["Sesgo de Confirmación", "Sesgo de Supervivencia", "Sesgo de Conveniencia", "Sesgo de Autoselección"],
        "correcta": "Sesgo de Conveniencia",
        "explicacion": "¡Correcto! El sesgo de conveniencia sucede al seleccionar a los sujetos que están más accesibles o son más fáciles de conseguir debido a la ubicación o el momento."
    },
    {
        "id": 3,
        "titulo": "Pregunta 3",
        "caso": "Una estación de radio abre una línea telefónica voluntaria para que los oyentes llamen y opinen sobre una nueva ley muy polémica. Solo llaman personas extremadamente enfadadas o activistas radicalmente a favor.",
        "opciones": ["Sesgo de Medición", "Sesgo de Autoselección (o participación voluntaria)", "Sesgo de Conveniencia", "Sesgo de No respuesta"],
        "correcta": "Sesgo de Autoselección (o participación voluntaria)",
        "explicacion": "¡Correcto! El sesgo de autoselección se da cuando los propios individuos deciden voluntariamente formar parte de la muestra. Suele atraer a personas con opiniones muy extremas o interesadas."
    },
    {
        "id": 4,
        "titulo": "Pregunta 4",
        "caso": "Un profesor de autoescuela analiza los factores de éxito para aprobar el examen teórico analizando únicamente los test de los alumnos que ya obtuvieron su licencia, sin revisar los registros de aquellos que abandonaron las clases tras suspender tres veces.",
        "opciones": ["Sesgo de Conveniencia", "Sesgo de Respuesta", "Sesgo de Supervivencia", "Sesgo de Confirmación"],
        "correcta": "Sesgo de Supervivencia",
        "explicacion": "¡Correcto! El sesgo de supervivencia aparece cuando solo se analizan los datos de los sujetos que 'sobrevivieron' a un proceso o filtro, ignorando por completo a los que quedaron fuera."
    },
    {
        "id": 5,
        "titulo": "Pregunta 5",
        "caso": "Una empresa quiere saber qué opinan los ciudadanos sobre el teletrabajo y decide encuestar exclusivamente a sus propios empleados porque los tienen a mano en la base de datos interna.",
        "opciones": ["Sesgo de Supervivencia", "Sesgo de Conveniencia", "Sesgo de Respuesta", "Sesgo de Confirmación"],
        "correcta": "Sesgo de Conveniencia",
        "explicacion": "¡Correcto! Es un sesgo de conveniencia porque se limita a escoger a los sujetos más accesibles y rápidos de alcanzar para el investigador."
    },
    {
        "id": 6,
        "titulo": "Pregunta 6",
        "caso": "Durante una entrevista clínica presencial, el psicólogo le pregunta al paciente cuántas horas pasa al día usando redes sociales. El paciente, por vergüenza a ser juzgado, responde que 'menos de una hora', cuando en realidad pasa cinco.",
        "opciones": ["Sesgo de No respuesta", "Sesgo de Medición", "Sesgo de Respuesta (o deseabilidad social)", "Sesgo de Conveniencia"],
        "correcta": "Sesgo de Respuesta (o deseabilidad social)",
        "explicacion": "¡Correcto! El sesgo de respuesta ocurre cuando los encuestados no contestan la verdad, sino lo que creen que es socialmente aceptable o lo que el entrevistador quiere escuchar."
    },
    {
        "id": 7,
        "titulo": "Pregunta 7",
        "caso": "Se envía una encuesta por correo sobre satisfacción vecinal. Los vecinos que están conformes ignoran la carta, mientras que el 5% de los vecinos que están en conflicto con la junta responde masivamente, alterando por completo el promedio del resultado final.",
        "opciones": ["Sesgo de No respuesta", "Sesgo de Selección", "Sesgo de Confirmación", "Sesgo de Medición"],
        "correcta": "Sesgo de No respuesta",
        "explicacion": "¡Correcto! El sesgo de no respuesta pasa cuando las personas que deciden no contestar una encuesta tienen opiniones o características muy diferentes a las de aquellos que sí responden."
    },
    {
        "id": 8,
        "titulo": "Pregunta 8",
        "caso": "Un científico cree firmemente que una planta cura el dolor de cabeza. En su estudio, resalta y anota minuciosamente los 10 casos donde los pacientes mejoraron, pero cataloga como 'olvidos o fallos externos' los 40 casos donde los pacientes siguieron igual.",
        "opciones": ["Sesgo de Respuesta", "Sesgo de Medición", "Sesgo de Confirmación", "Sesgo de Supervivencia"],
        "correcta": "Sesgo de Confirmación",
        "explicacion": "¡Correcto! El sesgo de confirmación es la tendencia del investigador a buscar, interpretar y registrar únicamente los datos que apoyan sus propias hipótesis o ideas previas."
    },
    {
        "id": 9,
        "titulo": "Pregunta 9",
        "caso": "Un estudio de salud pública utiliza tensiómetros digitales antiguos cuyas pantallas están desgastadas y provocan que los enfermeros anoten valores erróneos de presión arterial al no distinguir bien los números.",
        "opciones": ["Sesgo de No respuesta", "Sesgo de Medición (o de instrumentación)", "Sesgo de Conveniencia", "Sesgo de Autoselección"],
        "correcta": "Sesgo de Medición (o de instrumentación)",
        "explicacion": "¡Correcto! El sesgo de medición sucede cuando las herramientas, preguntas o métodos utilizados para recolectar los datos fallan, están mal diseñados o calibrados de forma incorrecta."
    },
    {
        "id": 10,
        "titulo": "Pregunta 10",
        "caso": "Una encuesta de opinión política incluye una pregunta redactada de forma confusa y con doble negación, lo que hace que los participantes se confundan y marquen opciones totalmente opuestas a lo que realmente piensan.",
        "opciones": ["Sesgo de Respuesta", "Sesgo de Confirmación", "Sesgo de Medición (o de instrumentación)", "Sesgo de Supervivencia"],
        "correcta": "Sesgo de Medición (o de instrumentación)",
        "explicacion": "¡Correcto! Si los métodos o el diseño de las preguntas confunden al participante, se introduce un sesgo de medición al distorsionar las respuestas."
    }
]

# Formulario para enviar las respuestas en bloque
with st.form("test_form"):
    respuestas_usuario = {}
    
    # Renderizar cada pregunta en la interfaz web
    for p in preguntas:
        st.subheader(p["titulo"])
        st.markdown(f"**Caso práctico:** {p['caso']}")
        
        # Selector de opciones tipo radio
        respuestas_usuario[p["id"]] = st.radio(
            "Selecciona la respuesta correcta:",
            options=p["opciones"],
            key=f"p_{p['id']}",
            index=None
        )
        st.markdown("---")
        
    # Botón de envío obligatorio para formularios en Streamlit
    enviado = st.form_submit_button("Corregir Cuestionario")

# Procesar los resultados una vez pulsado el botón
if enviado:
    st.header("📋 Resultados del Test")
    aciertos = 0
    
    for p in preguntas:
        eleccion = respuestas_usuario[p["id"]]
        st.markdown(f"### {p['titulo']}")
        
        if eleccion == p["correcta"]:
            st.success(f"✅ ¡Correcto! Tu respuesta: {eleccion}")
            st.caption(p["explicacion"])
            aciertos += 1
        elif eleccion is None:
            st.warning(f"⚠️ No respondiste a esta pregunta. La respuesta correcta era: **{p['correcta']}**")
        else:
            st.error(f"❌ Incorrecto. Tu respuesta: {eleccion}. La respuesta correcta era: **{p['correcta']}**")
            st.caption(p["explicacion"])
            
    # Cálculo exacto y proporcional de la nota final sobre 10
    nota_final = (aciertos / len(preguntas)) * 10
    st.metric(label="Puntuación Total", value=f"{aciertos} / {len(preguntas)}", delta=f"{nota_final:.1f} / 10 Nota")
    
    if nota_final >= 7.0:
        st.balloons()
        st.success("¡Excelente trabajo! Tienes un gran dominio de los sesgos de tu temario.")
    else:
        st.info("Sigue repasando los conceptos de la hoja para fijar las diferencias entre cada sesgo.")
