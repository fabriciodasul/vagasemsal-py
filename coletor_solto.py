import requests


def buscar_vagas(jobName, state, offset, limit=1, sortBy="relevance"):
    url = "https://portal.gupy.io/api/job-search/jobs"

    params = {
        "jobName": jobName,
        "state": state,
        "offset": offset,
        "limit": limit,
        "sortBy": sortBy
    }

    try:
        resposta = requests.get(url, params=params)
        resposta.raise_for_status()

        resultado = resposta.json()
        vagas = resultado.get("data", [])
        total_vagas = resultado.get("pagination", {}).get("total", 0)
        print(f"--- Total de vagas encontradas: {total_vagas} --- \n")

        if not vagas:
            print("Nenhuma vaga encontrada.")
            return

        for vaga in vagas:
            titulo = vaga.get("name")
            empresa = vaga.get("careerPageName")
            cidade = vaga.get("city")
            estado = vaga.get("state")

            print(f"Vaga: {titulo}")
            print(f"Empresa: {empresa}")
            print(f"Local: {cidade} - {estado}")
            print("-" * 40)

    except Exception as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    print("Iniciando a busca de vagas de teste...")
    buscar_vagas(jobName="Caixa", state="Rio de Janeiro", offset=0, limit=10)


