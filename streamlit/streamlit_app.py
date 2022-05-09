import streamlit as st
import sys
import json
import uuid
import os

# Load filters folders
model_dir = os.path.join(os.path.dirname( __file__ ), '..', 'src' )
sys.path.append(model_dir) 

from SummarizationModel import SummarizationModel

#Load language model (if was not already loaded)
language_detection_model = SummarizationModel()

examples_dict = {}
examples_dict['None'] = ''
examples_dict['Titanic'] = '''Titanic es una película estadounidense dramática de catástrofe de 1997 dirigida y escrita por James Cameron y protagonizada por Leonardo DiCaprio,
Kate Winslet, Billy Zane, Kathy Bates, Gloria Stuart y Bill Paxton. La trama, una epopeya romántica, relata la relación de Jack Dawson y Rose DeWitt Bukater, dos jóvenes que se conocen y se enamoran a bordo del transatlántico RMS Titanic en su viaje inaugural desde Southampton (Inglaterra) a Nueva York (EE. UU.) en abril de 1912. Pertenecientes a diferentes clases sociales, 
intentan salir adelante pese a las adversidades que los separarían de forma definitiva, entre ellas el prometido de Rose, Caledon «Cal» Hockley (un adinerado del cual ella no está enamorada, pero su madre la ha obligado a permanecer con él para garantizar un futuro económico próspero) y el hundimiento del barco tras chocar con un iceberg.
Si bien Jack y Rose son personajes ficticios, varios otros secundarios como Margaret Brown (pasajera de primera clase), Thomas Andrews (diseñador del barco) y Edward John Smith (capitán del buque) son personas que realmente vivieron los acontecimientos históricos del hundimiento del transatlántico en 1912. También son auténticas las escenas del pecio del barco que figuran en las escenas iniciales, para las cuales se destinaron tres millones de dólares estadounidenses del presupuesto total de la producción.'''

st.set_page_config(
     page_title="In a few words",
     page_icon="📝",
)

st.title('📝 In a few words...')

option = st.sidebar.selectbox(
     'Examples',
     examples_dict.keys())

doc = st.text_area(
     "Paste your text here and we will make a summary of this",
     value=examples_dict.get(option, ''),
     height=150,
     )

if st.button(label="✨ Make me a summary!"):
     
     
     summary_doc = language_detection_model.summarize(doc)
          
st.header('Summary')     
st.write (summary_doc)


