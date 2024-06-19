# Importa o módulo platform, que fornece funcionalidades para acessar dados sobre a plataforma (sistema operacional, versão, etc.) em que o código está sendo executado.
import platform

# Importa o módulo psutil, que permite acesso a informações do sistema e processos em execução, como uso de CPU, memória, discos, rede, etc.
import psutil

# Importa a função get_monitors do módulo screeninfo, que permite obter informações sobre os monitores conectados ao sistema, como resolução e dimensões.
from screeninfo import get_monitors


def obter_informacoes_computador():
    # Obtém informações do sistema operacional
    sistema_operacional = platform.platform()
    
    # Obtém informações sobre a arquitetura do sistema
    arquitetura = platform.architecture()
    
    # Obtém informações sobre o processador
    processador = platform.processor()
    
    # Obtém informações sobre a CPU
    frequencia_cpu = psutil.cpu_freq().current if psutil.cpu_freq() else 'N/A'
    nucleos_fisicos = psutil.cpu_count(logical=False)
    nucleos_logicos = psutil.cpu_count(logical=True)
    
    # Obtém informações sobre a memória RAM
    memoria = psutil.virtual_memory()
    
    # Obtém informações sobre a resolução da tela
    resolucoes_telas = [(monitor.width, monitor.height) for monitor in get_monitors()]
    
    # Formata as informações
    informacoes_formatadas = {
        "Sistema Operacional": sistema_operacional,
        "Arquitetura": arquitetura[0],
        "Processador": processador,
        "Frequência Atual da CPU (MHz)": frequencia_cpu,
        "Núcleos Físicos da CPU": nucleos_fisicos,
        "Núcleos Lógicos da CPU": nucleos_logicos,
        "Memória RAM Total (GB)": round(memoria.total / (1024 ** 3), 2),
        "Resoluções das Telas": resolucoes_telas
    }
    
    return informacoes_formatadas

if __name__ == "__main__":
    informacoes_computador = obter_informacoes_computador()
    
    # Exibe as informações
    print("Informações do Computador:")
    for chave, valor in informacoes_computador.items():
        print(f"{chave}: {valor}")
