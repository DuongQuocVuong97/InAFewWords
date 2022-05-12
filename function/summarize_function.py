import sys
import os

# Load the folder with the SummarizationModel object
model_dir = os.path.join(os.path.dirname( __file__ ), '..', 'src' )
sys.path.append(model_dir) 

# Import the model
from SummarizationModel import SummarizationModel

# You call the object and apply summarize to the text
sum_model = SummarizationModel()
def summarize(sum_model, text):
    summary = sum_model.summarize(text)
    return summary