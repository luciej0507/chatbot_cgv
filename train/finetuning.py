from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
OPENAI_TOKEN = os.getenv("OPENAI_API_KEY")
OPENAI_FILE_ID = os.getenv("OPENAI_FILE_ID")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

client = OpenAI(api_key=OPENAI_TOKEN)

ft_job = client.fine_tuning.jobs.create(
  training_file=OPENAI_FILE_ID,
  model=OPENAI_MODEL
)

# Notez absolument le modèle fine-tuné, il sera nécessaire pour l'utilisation du modèle fine-tuné
print("Fine Tune Job has been created with id ", ft_job.id)