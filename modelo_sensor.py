class LecturaSensor:
    def __init__(self, identificador_lote, valor_temperatura, valor_humedad):
        self.identificador_lote = str(identificador_lote)
        self.valor_temperatura = float(valor_temperatura)
        self.valor_humedad = float(valor_humedad)
        self.estado_conservacion = self.evaluar_cadena_frio()

    def evaluar_cadena_frio(self):
        if self.valor_temperatura > 6.0:
            return "ALERTA: RIESGO DE DESCOMPOSICION"
        elif self.valor_temperatura < 4.0:
            return "ALERTA: RIESGO DE CONGELAMIENTO"
        return "OPTIMO"

    def convertir_a_diccionario(self):
        return {
            "identificador_lote": self.identificador_lote,
            "temperatura": self.valor_temperatura,
            "humedad": self.valor_humedad,
            "estado": self.estado_conservacion
        }
