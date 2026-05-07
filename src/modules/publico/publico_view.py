class PublicoView:
    def exibir_resultado(self, response):
        print("\nREGISTRO DE PUBLICO")
        print("-" * 72)
        if not response["ok"]:
            print(f"Erro: {response['erro']}")
            return

        data = response["data"]
        print(f"Registro #{data['registro_id']} gravado com sucesso.")
        print(f"Sessao: {data['sessao_id']} - {data['filme']}")
        print(f"Cinema: {data['cinema']} | Sala: {data['sala']} | Inicio: {data['inicio']}")
        print(f"Quantidade registrada: {data['quantidade_registrada']}")
        print(f"Ocupacao atual: {data['publico_total']}/{data['capacidade']}")
        print(f"Lugares restantes: {data['lugares_restantes']}")
