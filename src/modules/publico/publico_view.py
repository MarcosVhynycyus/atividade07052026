class PublicoView:
    def exibir_publicos(self, publicos):
        print("\nREGISTROS DE PUBLICO")
        print("-" * 72)
        if not publicos:
            print("Nenhum registro de publico cadastrado.")
            return

        for publico in publicos:
            print(
                f"[{publico['id']}] Sessao {publico['sessao_id']} | "
                f"{publico['filme']} | {publico['cinema']} | {publico['inicio']}"
            )
            print(
                f"    Data: {publico['data_registro']} | "
                f"Quantidade: {publico['quantidade']}"
            )

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

    def exibir_resultado_admin(self, response):
        print("\nOPERACAO DE PUBLICO")
        print("-" * 72)
        if not response["ok"]:
            print(f"Erro: {response['erro']}")
            return

        print(response.get("mensagem", "Operacao realizada com sucesso."))
        data = response.get("data")
        if data and "quantidade" in data:
            print(f"Registro #{data['id']} | Sessao {data['sessao_id']}")
            print(f"Quantidade: {data['quantidade']} | Data: {data['data_registro']}")
            print(f"Ocupacao atual: {data['publico_total']}/{data['capacidade']}")
