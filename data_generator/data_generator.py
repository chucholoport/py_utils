
import pandas as pd
import numpy as np
import yaml
import os
import logging

NUMBER_OF_RECORDS = 1000
NAMES = ['Ana', 'Luis', 'Carlos', 'María', 'José', 'Laura', 'Miguel', 'Sofía']
SECOND_NAMES = ['García', 'Hernández', 'Martínez', 'López', 'González', 'Pérez', 'Ramírez', 'Torres']
GENDERS = ['M', 'F']
CAREERS = ['Ingeniería', 'Medicina', 'Derecho', 'Arquitectura', 'Psicología', 'Economía']

class DataGenerator:
    """
    Generates a CSV, JSON & YAML with students simulated data.

    Atributes:
        - file (str): Name of the output files.
        - data (pd.DataFrame): Simulated data Dataframe.
    Methods:
        - set_log(log_file): Configures logging system.
        - create_data(): Creates CSV file with simulated data.
    """
    def __init__(self, file: str = 'data'):
        
        # Inicializar atributos
        self.file = file
        self.csv = f'{self.file}.csv'
        self.json = f'{self.file}.json'
        self.yaml = f'{self.file}.yaml'
        self.data = pd.DataFrame({
            'matricula': [f"A{str(i).zfill(5)}" for i in range(NUMBER_OF_RECORDS)],
            'nombre': np.random.choice(NAMES, size=NUMBER_OF_RECORDS),
            'apellido': np.random.choice(SECOND_NAMES, size=NUMBER_OF_RECORDS),
            'edad': np.random.randint(18, 30, size=NUMBER_OF_RECORDS),
            'genero': np.random.choice(GENDERS, size=NUMBER_OF_RECORDS),
            'carrera': np.random.choice(CAREERS, size=NUMBER_OF_RECORDS),
            'cuatrimestre': np.random.randint(1, 10, size=NUMBER_OF_RECORDS),
            'promedio': np.round(np.random.uniform(6.0, 10.0, size=NUMBER_OF_RECORDS), 2)
        })
        
        # Configurar logging y crear datos
        self.set_logging()
        self.generate_data()
    
    def set_logging(self, log_file='data_generator.log'):
        """ Set up logging configuration for the DataGenerator class. """
        
        # Eliminar el archivo de log existente si existe
        if os.path.exists(log_file):
            os.remove(log_file)
            
        # Configurar el sistema de logging
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Crear un logger específico para 'estudiantes'
        self.logger = logging.getLogger('estudiantes')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)

        self.logger.info("DataCreator initialized.")
        
    def generate_data(self):
        """ Generate data and save it to CSV, JSON, and YAML files. """
        
        self.logger.debug(f"DataFrame:\n{self.data.to_string()}")
        
        # Guardar el DataFrame en un archivo CSV
        self.data.to_csv(self.csv, index=False)
        self.logger.info(f"Data file '{self.csv}' created with {NUMBER_OF_RECORDS} records.")
        print(f"Data file '{self.csv}' created with {NUMBER_OF_RECORDS} records.")
        
        # Guardar el DataFrame en un archivo JSON
        self.data.to_json(self.json, orient='records', force_ascii=False, indent=4)
        self.logger.info(f"Data file '{self.json}' created with {NUMBER_OF_RECORDS} records.")
        print(f"Data file '{self.json}' created with {NUMBER_OF_RECORDS} records.")
        
        # Guardar el DataFrame en un archivo YAML
        data_dict = self.data.to_dict(orient='records')
        with open(self.yaml, 'w', encoding='utf-8') as f:
            yaml.dump(data_dict, f, allow_unicode=True, sort_keys=False)
        self.logger.info(f"Data file '{self.yaml}' created with {NUMBER_OF_RECORDS} records.")
        print(f"Data file '{self.yaml}' created with {NUMBER_OF_RECORDS} records.")