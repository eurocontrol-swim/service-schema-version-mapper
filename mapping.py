from jsonize.utils.mapping import json_document_to_json_document
from transformations import transformations
from pathlib import Path

input_file_path = Path('./input/OpenATM.json')
output_file_path = Path('./output/OpenATM.json')
jsonize_map_path = Path('./jsonize-mapping.json')



json_document_to_json_document(input_document=input_file_path,
                               output_document=output_file_path,
                               jsonize_map_document=jsonize_map_path,
                               transformations=transformations,
                               ignore_empty=False)
